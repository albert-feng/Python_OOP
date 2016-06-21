#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Programer(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, key):
        # return self.name
        return self.__dict__[key]

    def __setattr__(self, key, value):
        # self.name = value
        self.__dict__[key] = value

if __name__ == '__main__':
    p = Programer('Albert', 25)
    print p.name
