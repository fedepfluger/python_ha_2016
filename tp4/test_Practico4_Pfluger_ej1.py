#!/usr/bin/env python

from grupos_personas import Group, Person
import unittest
from mock import MagicMock

'''
Trabajo Practico numero 4 parte 1 UNITTEST
Curso de Python noviembre - diciembre 2016
Pfluger Federico Andres
'''


class TestGroupofPeople(unittest.TestCase):

    def setUp(self):
        self.p0 = MagicMock(spec=Person)
        self.p1 = MagicMock(spec=Person)
        self.p2 = MagicMock(spec=Person)

    def test_new2(self):
        self.group0 = Group([self.p0, self.p1])
        self.assertEqual(repr(self.group0), '<Group with 2 people>')
        self.assertItemsEqual(self.group0, [self.p0, self.p1])

    def test_new3(self):
        self.group = Group([self.p0, self.p1, self.p2])
        self.assertEqual(repr(self.group), '<Group with 3 people>')
        self.assertItemsEqual(self.group, [self.p0, self.p1, self.p2])

    def test_equal(self):
        self.group0 = Group([self.p0, self.p1])
        self.group1 = Group([self.p1, self.p0])
        self.assertEqual(self.group0, self.group1)

    def test_noequal(self):
        self.group0 = Group([self.p0, self.p1])
        self.group2 = Group([self.p1, self.p2])
        self.assertNotEqual(self.group0, self.group2)

    def test_addperson(self):
        self.group0 = Group([self.p0, self.p1])
        self.group1 = self.group0 + self.p2
        self.assertItemsEqual(self.group1, [self.p0, self.p1, self.p2])

    def test_substractperson(self):
        self.group1 = Group([self.p0, self.p1,  self.p2])
        self.group2 = self.group1 - self.p2
        self.assertItemsEqual(self.group2, [self.p0, self.p1])

    def test_addgroup(self):
        self.group0 = Group([self.p0, self.p1])
        self.group1 = Group([self.p0, self.p2])
        self.group2 = self.group0 + self.group1
        self.assertItemsEqual(self.group2, [self.p0, self.p1, self.p2])

    def test_substractgroup(self):
        self.group0 = Group([self.p0, self.p1])
        self.group1 = Group([self.p0, self.p2])
        self.group2 = self.group0 - self.group1
        self.assertItemsEqual(self.group2, [self.p1])

    def test_len(self):
        self.group0 = Group([self.p0, self.p1])
        self.assertEqual(len(self.group0), 2)

    def test_len0(self):
        self.group0 = Group([])
        self.assertEqual(len(self.group0), 0)

    def test_true(self):
        self.group0 = Group([self.p0, self.p1])
        self.assertTrue(self.group0)

    def test_false(self):
        self.group0 = Group([])
        self.assertFalse(self.group0)

    def test_in(self):
        self.group0 = Group([self.p0, self.p1])
        self.assertIn(self.p0, self.group0)

    def test_notin(self):
        self.group0 = Group([self.p0, self.p1])
        self.assertNotIn(self.p2, self.group0)

# edad promedio no implementado

    def tearDown(self):
        self.p0 = None
        self.p1 = None
        self.p2 = None

if __name__ == '__main__':
    unittest.main()
