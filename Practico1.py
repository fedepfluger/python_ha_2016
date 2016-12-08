#!/usr/bin/env python

'''
Trabajo Practico numero 1
Curso de Python noviembre - diciembre 2016
Pfluger Federico Andres
'''

# 1.1 Facturas


def facturas(nfac):
    if nfac > 12:
        nfac = 'muchas'
    return 'Cantidad de facturas: ' + str(nfac)

# 1.2 Ambos


def ambos(s):
    if len(s) > 1:
        return s[0:2] + s[-2:]
    else:
        return ''

# 1.3 Fix


def fix(s):
    return s[0] + s[1:].replace(s[0], '*')

# 1.4 Mezclar


def mezclar(a, b):
    return b[0] + a[1:] + " " + a[0] + b[1:]

# 2.1 Macheos


def macheos(ls):
    return len([x for x in ls
               if(len(x) > 2) and(x[len(x) - 1] == x[len(x) - 2])])

# 2.2 Front_x


def front_x(ls):
    ls1 = sorted([x for x in ls if (x[0] == 'x')or(x[0] == 'X')])
    ls2 = sorted([x for x in ls if (x[0] != 'x')and(x[0] != 'X')])
    return ls1 + ls2

# 2.3 Sort_last


def sort_last(lt):
    return sorted(lt, key=lambda x: x[len(x)-1])

# 2.4.1 Tablas de multiplicar


def tablas_multiplicar(nro):
    return range(nro, 11*nro, nro)

# 3.1 Mapeo


def mapeo(s):
    return {k: v for k, v in zip(s, range(0, len(s)))}

# 3.2 Busqueda reversa


def busqueda_reversa(dic, val):
    return dic.keys()[dic.values().index(val)]

# 4.1 Invitados


def invitados(dic):
    return [key for key, val in dic.items() if val == 'Asistira']

# 4.2 Justificar


def justificar(s):
    return '{:>80}'.format(s)

# 5.1 Puerta


class Puerta():

    def __init__(self, num1, num2, num3):
        self.combinacion = [num1, num2, num3]
        self.myestado = 'cerrada'

    def abrir(self, num1, num2, num3):
        if self.combinacion == [num1, num2, num3]:
            self.myestado = 'abierta'
        return self.myestado

    def cerrar(self, num1, num2, num3):
        if self.combinacion == [num1, num2, num3]:
            self.myestado = 'cerrada'
        return self.myestado

    def estado(self):
        return self.myestado

    def cambiar_combinacion(self, num1, num2, num3,
                            newnum1, newnum2, newnum3):
        if self.combinacion == [num1, num2, num3]:
            self.combinacion = [newnum1, newnum2, newnum3]
        return

    pass

# 5.2 Jerarquia de Clases


class Estudiante():
    name = ''
    matricula = 1

    def __init__(self, name, matricula):
        self.name = name
        self.matricula = matricula

    def getname(self):
        return self.name

    def getmatricula(self):
        return self.matricula

    def __str__(self):
        return self.name + ' ' + str(self.matricula)
    pass


class Estudiante_Ocacional(Estudiante):

    def __init__(self, name, matricula):
        Estudiante.__init__(self, name, matricula)

    pass


class Estudiante_Verano(Estudiante_Ocacional):

    def __init__(self, name, matricula):
        Estudiante_Ocacional.__init__(self, name, matricula)

    pass


class Estudiante_Curso(Estudiante_Ocacional):

    def __init__(self, name, matricula):
        Estudiante_Ocacional.__init__(self, name, matricula)

    pass


class Estudiante_Tecnicatura(Estudiante):

    def __init__(self, name, matricula):
        Estudiante.__init__(self, name, matricula)

    pass


class Estudiante_Licenciatura(Estudiante):

    def __init__(self, name, matricula):
        Estudiante.__init__(self, name, matricula)

    pass


class Estudiante_Empleados(Estudiante_Curso):

    def __init__(self, name, matricula):
        Estudiante_Curso.__init__(self, name, matricula)
        self.nombre = name

    pass

# 5.3 Triangulo


class Triangulo():

    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def es_rectangulo(self):
        return (self.v1**2 == self.v2**2 + self.v3**2 or
                self.v2**2 == self.v1**2 + self.v3**2 or
                self.v3**2 == self.v1**2 + self.v2**2)

    def es_escaleno(self):
        return (self.v1 != self.v2 != self.v3)

    def es_isosceles(self):
        return (self.v1 == self.v2 != self.v3 or
                self.v1 == self.v3 != self.v2 or
                self.v2 == self.v3 != self.v1)

    def es_equilatero(self):
        return (self.v1 == self.v2 == self.v3)

    pass

# 5.4 Una Persona


class Persona():

    def __init__(self, dni, name, ap1, ap2='no posee'):
        self.nombrepila = name
        self.apellido1 = ap1
        self.apellido2 = ap2
        self.dni = dni

    def __str__(self):
        return (self.nombrepila + ' ' +
                self.apellido1 + ' ' +
                self.apellido2 + ' DNI: ' + str(self.dni))

    def getname(self):
        return (self.nombrepila + ' ' +
                self.apellido1 + ' ' + self.apellido2)

    def getdni(self):
        return self.dni

# 5.5 Genelogia

    def setpadre(self, padre):
        self.padre = padre

    def setmadre(self, madre):
        self.madre = madre

    def getpadre(self):
        return self.padre

    def getmadre(self):
        return self.madre
    pass


class Personas():

    def __init__(self, *listpersona):
        self.mylist = listpersona

    def __str__(self):
        s = '('
        for c in self:
            s = s + str(c) + ', '
        s = s.rstrip(', ') + ')'
        return s

    def __iter__(self):
        self.current = 0
        return self

    def next(self):
        if self.current < len(self.mylist):
            self.current += 1
            return self.mylist[self.current-1]
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.mylist[index]

    def __len__(self):
        return len(self.mylist)

    pass
# python_ha_2016
