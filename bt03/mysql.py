#!/usr/bin/python

import sys, getopt, os, shutil
import mysql.connector
from mysql.connector import errorcode

def main(argv):
   user = 'root'
   password = ''
   host = '127.0.0.1'
   database = ''
   try:
      opts, args = getopt.getopt(argv,"hu:p:h:d:",["user=","pass=","host=","db="])
   except getupt.GetoptError:
      print 'mysql.py -u <user> -p <host> -h <host> -d <database>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'mysql.py -u <user> -p <host> -h <host> -d <database>'
         sys.exit()
      elif opt in ("-u", "--user"):
         user = arg
      elif opt in ("-p", "--pass"):
         password = arg
      elif opt in ("-h", "--host"):
         host = arg
      elif opt in ("-d", "--db"):
         database = arg      
   config = {
     'user': user,
     'password': password,
     'host': host,
     'database': database,
     'raise_on_warnings': True,
   }
   try:
      con = mysql.connector.connect(**config)
   except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
      else:
         print(err)
   con.close()
if __name__ == "__main__":
   main(sys.argv[1:])
