#!/usr/bin/python3

# Author: Daniel Harvey
# Written: April 26 2018

import string
from xmlrpc.server import SimpleXMLRPCServer

class StringFunctions(object):
    def _privateFunction(self):
        # This function cannot be called through XML-RPC because it
        # starts with an '_'
        pass

    def chop_in_half(self, astr):
        return astr[0:int(len(astr)/2)]

    def repeat(self, astr, times):
        return astr * times

    def set_str(self, astr):
        self.python_string = astr

    def get_str(self):
        return self.python_string

    def set_list(self, alist):
        self.python_list = alist

    def join(self):
        return ' '.join(self.python_list)

    def longAdd(self, astr1, astr2):
        carry = 0
        sum1 = ''
        for i in range(0,max(len(astr1), len(astr2))):
            dig1 = 0
            dig2 = 0

            if i < len(astr1):
                dig1 = int(astr1[i])

            if i < len(astr2):
                dig2 = int(astr2[i])
            
            digSum = dig1 + dig2

            sum1 += str(digSum % 10)
            carry = digSum // 10

        return sum1
 

server = SimpleXMLRPCServer(("localhost", 8000), allow_none = True)
server.register_instance(StringFunctions())
server.register_function(lambda astr: '_' + astr, '_string')
server.serve_forever()
