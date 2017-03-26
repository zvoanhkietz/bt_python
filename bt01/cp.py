#!/usr/bin/python

import sys, getopt, os, shutil

def main(argv):
   src = ''
   des = ''
   try:
      opts, args = getopt.getopt(argv,"hs:d:",["src=","des="])
   except getopt.GetoptError:
      print 'test.py -s <source> -d <desination>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -s <source> -d <desination>'
         sys.exit()
      elif opt in ("-s", "--src"):
         src = arg
      elif opt in ("-d", "--des"):
         des = arg

   if os.path.exists(src):
      if os.path.isdir(des):
         shutil.copy2(src, des)
         print("Success.")
      else:
         print("Destination path '" + des + "' not exists.")      
   else:
      print("Source file: '" + src + "' not exists.")
if __name__ == "__main__":
   main(sys.argv[1:])
