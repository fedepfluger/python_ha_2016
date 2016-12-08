#!/usr/bin/env python

'''
Trabajo Practico numero 2
Curso de Python noviembre - diciembre 2016
Pfluger Federico Andres
'''


class Persona(object):

    def __init__(self, name, age):
        self._name = str(name)
        self._age = age

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '<Persona ' + self._name + '>'

    def __add__(self, other):
        return Grupo({self, other})

    def __eq__(self, other):
        return (self._name == other._name and
                self._age == other._age)

    def __ne__(self, other):
        return not (self == other)

    def nombre(self):
        return self._name

    def edad(self):
        return self._age

    pass


class Grupo(object):

    def __init__(self, *args):
        self._group = set(*args)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '<Grupo ' + str(len(self._group)) + ' personas>'

    def __add__(self, other):
        l = [other]
        if isinstance(other, Grupo):
            l = list(other._group)
        return Grupo(list(self._group) + l)

    def __eq__(self, other):
        return self._group == other._group

    def __ne__(self, other):
        return not (self == other)

    def __sub__(self, other):
        s = {other}
        if isinstance(other, Grupo):
            s = other._group
        return Grupo(self._group - s)

    def __iter__(self):
        self.current = 0
        return self

    def next(self):
        if self.current < len(self._group):
            self.current += 1
            return list(self._group)[self.current-1]
        else:
            raise StopIteration

    def __len__(self):
        return len(self._group)

    def __nonzero__(self):
        return (len(self._group) > 0)

    def edad_promedio(self):
        try:
            return (sum([x.edad() for x in list(self._group)]) /
                    float(len(self._group)))
        except ZeroDivisionError:
            print('Traceback (most recent call last):')
            return 'EmptyGroupError: grupo vacio'
    pass
