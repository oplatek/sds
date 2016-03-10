#!/usr/bin/env python3

import json
import logging
import os
import tarfile

try: # try to use python2 module
    from urllib2 import Request, urlopen, URLError, HTTPError
except ImportError: # otherwise, use python3 module
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError

import speech_recognition as sr
from speech_recognition import RequestError, UnknownValueError, WaitTimeoutError, AudioData


__author__ = 'Petr Belohlavek'


def recognize_cloudasr(audio_data, url, port, lang='en-wiki', show_all=False):
    ''' `speech_recognition`-like function wrapping CloudASR interface.
    :param audio_data: Raw `*.wav` file.
    :param url: Address of the CloudASR service containing full protocol etc. Must not contain backslash as the last
                chracter. Example: http://localhost
    :param port: Port of the CloudASR service. Example: 8000
    :param lang: Language to be processed. it must be supported by the running CloudASR server. Currently supported
                 lamnguages are: en-wiki, en-voxforge, en-towninfo, cs, cs-alex and dnn-example
    :param show_all: If True, return the whole response object, otherwise return the most probable answer.
    :return: The most probable answer or the whole response object.
    '''

    assert isinstance(lang, str), "`language` must be a string"

    url = "{}:{}/recognize?lang={}".format(url, port, lang)
    request = Request(url, data=audio_data, headers={"Content-Type": "audio/x-wav; rate={0};".format(16000)})

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

    r = sr.Recognizer()
    done = 0

    with tarfile.open('/home/petr/data_voip_cs.tgz', 'r:gz') as archive,\
         open('result/cloudasr.txt', 'w') as cloudasr_out,\
         open('result/google.txt', 'w') as google_out,\
         open('result/truth.txt', 'w') as truth_out:

        for member in archive:
            f_name = member.name
            if done >= 200:
                break

            if f_name.split('.')[-1] == 'wav':
                real_wav_f = '/tmp/'+f_name
                logging.info('Extracting .wav #%d: %s', done, real_wav_f)
                archive.extract(f_name, '/tmp/')

                logging.info('Extracting .trn #%d', done)
                trn = archive.extractfile(f_name + '.trn')

                logging.info('Writing the truth utterance')
                truth_out.write(trn.read().decode("utf-8").lower())

                logging.info('Recognising .wav by CloudASR')
                with open(real_wav_f, 'rb') as wav:
                    cloudasr_out.write('{}\n'.format(recognize_cloudasr(audio_data=wav.read(), url='http://localhost', port=8000, lang='cs').lower()))

                logging.info('Recognising .wav by Google Web Speech')
                with sr.WavFile(real_wav_f) as source:
                    try:
                        audio = r.record(source)
                        google_out.write('{}\n'.format(r.recognize_google(audio, language='cs-CZ').lower()))
                    except Exception:
                        logging.error('Google failed')
                        google_out.write('\n')

                os.remove(real_wav_f)

                done += 1
