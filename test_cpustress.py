#!/usr/bin/python

from multiprocessing import cpu_count
from os import system

def stress_cpu():
    print "Running CPU stress..."
#    system(str('yes > /dev/null & '* cpu_count())[:-2])

stress_cpu()




