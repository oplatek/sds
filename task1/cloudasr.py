#!/usr/bin/env python3

import json
import logging
import os

try: # try to use python2 module
    from urllib2 import Request, urlopen, URLError, HTTPError
except ImportError: # otherwise, use python3 module
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError

import speech_recognition as sr
from speech_recognition import RequestError, UnknownValueError, WaitTimeoutError, AudioData


__author__ = 'Petr Belohlavek'


class MyRecognizer(sr.Recognizer):

    def recognize_cloudasr(self, audio_data, language='en-wiki', show_all=False):
        """
        Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the CloudASR API.

        TODO: what languages?
        The recognition language is determined by ``language``, an IETF language tag like ``"en-US"`` or ``"en-GB"``, defaulting to US English. A list of supported language codes can be found `here <http://stackoverflow.com/questions/14257598/>`__. Basically, language codes can be just the language (``en``), or a language with a dialect (``en-US``).
        Returns the most likely transcription if ``show_all`` is false (the default). Otherwise, returns the raw API response as a JSON dictionary.
        Raises a ``speech_recognition.UnknownValueError`` exception if the speech is unintelligible. Raises a ``speech_recognition.RequestError`` exception if the key isn't valid, the quota for the key is maxed out, or there is no internet connection.
        """

        assert isinstance(audio_data, AudioData), "`audio_data` must be audio data"
        assert isinstance(language, str), "`language` must be a string"

        convert_rate = 16000
        audio_data = audio_data.get_wav_data(convert_rate=convert_rate)

        url = 'https://api.cloudasr.com/recognize?lang={}'.format(language)
        request = Request(url, data=audio_data, headers={"Content-Type": "audio/x-wav; rate={0};".format(convert_rate)})

        try:
            response = urlopen(request)
        except HTTPError as e:
            raise RequestError("recognition request failed: {0}".format(getattr(e, "reason", "status {0}".format(e.code)))) # use getattr to be compatible with Python 2.6
        except URLError as e:
            raise RequestError("recognition connection failed: {0}".format(e.reason))
        response_text = response.read().decode("utf-8")

        # ignore any blank blocks
        actual_result = []
        for line in response_text.split("\n"):
            if not line: continue
            result = json.loads(line)["result"]
            if len(result) != 0:
                actual_result = result[0]
                break

        # return results
        if show_all: return actual_result
        if "alternative" not in actual_result: raise UnknownValueError()
        for entry in actual_result["alternative"]:
            if "transcript" in entry:
                return entry["transcript"]
        raise UnknownValueError() # no transcriptions available


if __name__ == '__main__':
    ''' Extract first 200 audios and save transcriptions by Google Web Speech and CloudASR into separate files.
    In addition, save the truth transcriptions.
    '''
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # r = sr.Recognizer()
    r = MyRecognizer()
    done = 1

    data_root = "/home/petr/data_voip_cs/"

    with open('result/cloudasr.txt', 'w') as cloudasr_out,\
         open('result/google.txt', 'w') as google_out,\
         open('result/truth.txt', 'w') as truth_out:

        for wav_name in os.listdir(data_root):
            if not wav_name.endswith(".wav"):
                continue

            logging.info('Processing input %d', done)

            with open("/home/petr/data_voip_cs/" + wav_name + '.trn', 'r') as trn_f,\
                 sr.WavFile("/home/petr/data_voip_cs/" + wav_name) as source:

                trn = trn_f.read().lower()[:-1]
                truth_out.write('{} ({})\n'.format(trn, done))

                audio = r.record(source)

                logging.info('\tTranslating by Google ASR')
                try:
                    google_out.write('{} ({})\n'.format(r.recognize_google(audio, language='cs-CZ').lower(),
                                                        done))
                    logging.info('\t\tSuccess')
                except Exception:
                    logging.warning('\t\tFail')
                    google_out.write('({})\n'.format(done))

                logging.info('\tTranslating by CloudASR')
                try:
                    cloudasr_out.write('{} ({})\n'.format(r.recognize_cloudasr(audio_data=audio,
                                                                               language='kams-cs-super').lower(),
                                                          done))
                    logging.info('\t\tSuccess')
                except Exception:
                    logging.warning('\t\tFail')
                    google_out.write('({})\n'.format(done))

            done += 1

    logging.info('Succeeded: %d', done)

    # import tarfile
    # with tarfile.open('/home/petr/data_voip_cs.tgz', 'r:gz') as archive:
    #
    #     for member in archive:
    #         f_name = member.name
    #         if done >= 200:
    #             break
    #
    #         if f_name.split('.')[-1] == 'wav':
    #             logging.info('Extracting .wav #%d: %s', done, done)
    #             archive.extract(f_name, '/tmp/foo/')
    #             archive.extract(f_name + '.trn', '/tmp/foo/')
    #             done += 1
