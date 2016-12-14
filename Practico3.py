#!/usr/bin/env python

import threading  # Ejercicio 1
import time  # Ejercicio 1
import json  # Ejercicio 2
import sys  # Ejercicio 3
from datetime import datetime  # Ejercicio 3

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


if __name__ == "__main__":
    if sys.argv[1] != '--from':
        print('--from ir required')
        exit(0)
    try:
        f = datetime.strptime(sys.argv[2], '%Y-%m-%dT%H:%M:%S.%f')
    except:
        print('Fail from DATE format')
        exit(0)
    if sys.argv[3] != '--to':
        print('--to ir required')
        exit(0)
    try:
        t = datetime.strptime(sys.argv[4], '%Y-%m-%dT%H:%M:%S.%f')
    except:
        print('Fail to DATE format')
        exit(0)
    print('Diferencia: -{}.{} secs.'
          .format((t-f).seconds, (t-f).microseconds))
