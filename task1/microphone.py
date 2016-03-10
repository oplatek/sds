#!/usr/bin/env python3

import speech_recognition as sr
import logging
import time


__author__ = 'Petr Belohlavek'


def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='en-EN')
        print(text)
    except Exception:
        pass

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    logging.info('Setting up')
    r = sr.Recognizer()
    m = sr.Microphone()

    logging.info('Adjusting for ambient noise')
    with m as source:
        r.adjust_for_ambient_noise(source)

    logging.info('Preparing for listening')
    stop_listening = r.listen_in_background(m, callback)

    logging.info('You may speak now :)')

    while True:
        time.sleep(0.1)