#!/usr/bin/python3
import sys

if len(sys.argv) <= 2:
	print ("Modo de uso: python",sys.argv[0],"10.0.0.0 80")
else:
	print ("Varrendo o host: ",sys.argv[1],"na porta",sys.argv[2])
