'''
Created by Ryan Schenck
8 March 2018
'''
import sys
import os
import gzip
import io
from optparse import OptionParser
import datetime
import time
import subprocess
from functools import wraps
import pandas as pd


def OptionParsing():
    usage = 'usage: %prog [options] -f <*.h5>'
    parser = OptionParser(usage)
    parser.add_option('-r', '--ref_genome', dest="refGenome", default="/Users/schencro/Desktop/Bioinformatics_Tools/Ref_Genomes/Ensembl/GRCh37.75/GRCh37.75.fa", help="Reference genome to be used for maf2vcf conversion.")

    (options, args) = parser.parse_args()
    return (options, parser)

def fn_timer(function):
    '''
    Use this as a wrapper at the top of any function you want to get run time information about.

    :param function: Function of interest.
    :return: A function to wrap around a function.
    '''
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("INFO: Total time running %s: %s minutes" %
               (function.__name__, str(round((t1-t0)/60.,2)))
               )
        return result
    return function_timer

def UpdateProgress(i, n, DisplayText):
    '''
    Prints a progress bar where appropriate.

    :param i: Current Step
    :param n: Total number of steps.
    :param DisplayText: A string that you want to print out that is informative.
    :return: None
    '''
    sys.stdout.write('\r')
    j = (i + 1) / n
    sys.stdout.write("[%-20s] %d%%\t INFO: %s" % ('=' * int(20 * j), 100 * j, DisplayText))
    sys.stdout.flush()

def UpdateProgressGetN(fileName):
    if fileName[len(fileName)-1]=="z":
        cmd = "gzip -cd %s | wc -l" % (fileName)
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
    else:
        cmd = "wc -l %s" % (fileName)
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
    return(int(pipe.read().decode("utf-8").lstrip(" ").split(" ")[0]))

def ProcessFiles():


def main():
    FilePath = os.path.dirname(os.path.abspath(__file__))
    now = datetime.datetime.now()
    (Options, Parser) = OptionParsing()
    allOutDir = FilePath.replace("DataGrooming","PCAWGData/")

if __name__=="__main__":
    main()