
import sys
import time


def hello():
   return "Hello World!"

if __name__ == "__main__":
   print(hello())
   temp=sys.argv[1]
   print(temp)

   # read file
   f = open(temp, "r")
   print(f.read())
   

   time.sleep(99999999)