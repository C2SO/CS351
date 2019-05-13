#!/usr/bin/python3

# Author: Daniel Harvey
# Written: April 26 2018

import string, socket
from xmlrpc.server import SimpleXMLRPCServer

_DEBUG = False

class LongMultiply(object):

    def multiply(self, astr1, astr2):
        subProducts = []

        for i in range(1,len(astr2)+1):
            dig1 = int(astr2[-i])
            carry = 0
            i2 = len(subProducts)
            subProducts.append('')            
            subProducts[i2] += '0'*(i-1)

            for j in range(1,len(astr1)+1):
                dig2 = int(astr1[-j])

                digProduct = dig1 * dig2

                subProducts[i2] += str((digProduct + carry) % 10)
                carry = (digProduct + carry) // 10
                
                if _DEBUG:
                    print("d1: %2d d2: %2d r: %2d c: %2d p: %2d" 
                        % (dig1, dig2, digProduct % 10, carry, 
                        int(subProducts[i2][len(subProducts[i2])-1])))
            else:
                if carry != 0:
                    subProducts[i2] += str(carry)
                
                if _DEBUG:
                    print("d1: -- d2: -- r:  0 c:  0 p: %2d" % (carry))

            subProducts[i2] = subProducts[i2][::-1]
        
        # Find the sum of  sub-products
        product = subProducts[0]
        for i in range(1,len(subProducts)):
            if _DEBUG:
                print("Product: %30s\nNext Sub: %29s" % (product, subProducts[i]))
            
            product = self._add(product, subProducts[i])

        return product

    def _add(self, astr1, astr2):
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



#longMultiplier = LongMultiply()
#print(longMultiplier.multiply('98','2000'))

server = SimpleXMLRPCServer((socket.gethostname(), 8001), allow_none = True)
server.register_instance(LongMultiply())
server.register_function(lambda astr: '_' + astr, '_string')
server.serve_forever()
