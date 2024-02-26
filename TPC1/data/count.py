#!/usr/bin/python3
'''
NAME
   count = Calculates word frequency in a text

SYNOPSIS
   count [options] input_files
   options: 
        -m 20 : Show 20 most common words
        -a : Order alfabetically
        -n : Order by occurences

Description:
'''

from jjcli import *
from collections import Counter
import sys
import re

cl = clfilter("anm:",doc=__doc__)     ## option values in cl.opt dictionary

def tokeniza(texto):
    pal = re.findall(r'\w+(?:\-\w+)?|[,;.:—_?!]+',texto)
    return pal

def imprime(lista,mode):
    if mode:
        for p,n in lista:
            print(f"{p} --> {n}")
    else:
        for p,n in lista:
            print(f"{n} <-- {p}")

#with open(sys.argv[1], "r") as f:
#    txt = f.read()

for txt in cl.text():    ## process one file at the time
    lista = tokeniza(txt)
    ocorr = Counter(lista)
    if "-m" in cl.opt:
        #print(ocorr.most_common(int(cl.opt.get("-m"))))
        imprime(ocorr.most_common(int(cl.opt.get("-m"))),True)
    elif "-a" in cl.opt:
        imprime(sorted(ocorr.items()),True)
    elif "-n" in cl.opt:
        imprime(ocorr.most_common(),False)
    else:
        imprime(ocorr.items(),True)