#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Programer(object):
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight


if __name__ == '__main__':
    programer = Programer('Albert', 25, 80)
    print dir(programer)
    print programer.__dict__

