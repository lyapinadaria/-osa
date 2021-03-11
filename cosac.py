# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 00:01:34 2021

@author: User
"""
from  Cosa.WhiteDwarf import *
from  Cosa import test

def main():
   %Запуск тестов
   a=test.TestFunc()
   a.test_get_Nh()
   a.test_get_Nh2()
   a.test_aprox()
   %Запуск программы
   glamurny_carlik()

if __name__ == '__main__':
    main()
