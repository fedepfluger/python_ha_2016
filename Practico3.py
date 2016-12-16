#!/usr/bin/env python

import threading  # Ejercicio 1
import time  # Ejercicio 1
import json  # Ejercicio 2
from datetime import datetime  # Ejercicio 3
import argparse  # Ejercicio 3

'''
Trabajo Practico numero 3
Curso de Python noviembre - diciembre 2016
Pfluger Federico Andres
'''


# Ejercicio 1 ----------


def concurrent(f):
    def inner(*args, **kwargs):
        promise = Promise(f, *args, **kwargs)
        promise.start()
        return promise
    return inner


class Promise(threading.Thread):

    def __init__(self, f, *args, **kwargs):
        super(Promise, self).__init__()
        self.f = f
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.result = self.f(*self.args, **self.kwargs)

    def get_result(self):
        if self.isAlive():
            raise Exception('result is not yet')
        return self.result


@concurrent
def function(a, b):
    time.sleep(10)
    return a + b

# Ejercicio 2 ----------


def jsonparams(f):
    def inner(sjson):
        try:
            p = json.loads(sjson)
        except:
            print('Fail: Expected JSON PARAMS: {} ').format(sjson)
            return
        if isinstance(p, dict):
            return f(**p)
        if isinstance(p, list):
            return f(*p)
    return inner


@jsonparams
def function1(a, b):
    return a + b

# Ejercicio 3 ----------


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from",
        dest='DATE',
        action='append',
        required=True)

    parser.add_argument(
        "--to",
        dest='DATE',
        action='append',
        required=True)

    args = parser.parse_args()
    (f, t) = args.DATE

    f = datetime.strptime(f, '%Y-%m-%dT%H:%M:%S.%f')
    t = datetime.strptime(t, '%Y-%m-%dT%H:%M:%S.%f')
    print('Diferencia: -{}.{} secs.'
          .format((t-f).seconds, (t-f).microseconds))

if __name__ == "__main__":
    main()
