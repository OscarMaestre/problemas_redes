#!/usr/bin/env python3
#coding=utf-8

import random

class GeneradorProblemasSubredes(object):
    @staticmethod
    def generar_problema(num_bits_red, num_bits_subred, num_bits_host):
        assert 32 == (num_bits_red + num_bits_subred + num_bits_host )
        pass
    
    @staticmethod
    def generar_problema_azar ():
        num_bits_red    =   random.randint(4, 10)
        num_bits_subred =   random.randint(2,5)
        num_bits_host   =   32 - num_bits_red - num_bits_subred