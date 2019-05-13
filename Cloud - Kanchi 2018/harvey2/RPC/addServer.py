#!/usr/bin/python3

# Author: Daniel Harvey
# Written: April 26 2018

import string, socket
from xmlrpc.server import SimpleXMLRPCServer

_DEBUG = False

class LongAdd(object):

    def add(self, astr1, astr2):
        carry = 0
        sum1 = ''

        for i in range(1,max(len(astr1), len(astr2)) + 1):
            dig1 = 0
            dig2 = 0
            
            if _DEBUG:
                print("i: %2d" % (i))

            if (i - 1) < len(astr1):
                dig1 = int(astr1[-i])

            if (i - 1) < len(astr2):
                dig2 = int(astr2[-i])
            
            digSum = dig1 + dig2 + carry
            
            sum1 += str(digSum % 10)
            carry = digSum // 10
            
            if _DEBUG:
                print("d1: %2d d2: %2d c: %2d s: %2d" % (dig1, dig2, carry, digSum % 10))

        if carry != 0:
            sum1 += str(carry)

        return sum1[::-1]

#adder = LongAdd()
#print(adder.add('196','4900'))

server = SimpleXMLRPCServer((socket.gethostname(), 8000), allow_none = True)
server.register_instance(LongAdd())
server.register_function(lambda astr: '_' + astr, '_string')
server.serve_forever()
