#!/usr/bin/python

import sys, getopt, os, shutil

def main(argv):
   inputData = ''
   try:
      opts, args = getopt.getopt(argv,"hs:",["string="])
   except getopt.GetoptError:
      print 'test.py -s <string>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -s <string>'
         sys.exit()
      elif opt in ("-s", "--string"):
         inputData = arg
   arr = inputData.split(' ')
   print(sorted(arr))
if __name__ == "__main__":
   main(sys.argv[1:])
