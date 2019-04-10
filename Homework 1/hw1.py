#CS351 -- HW1
#Nicholas Rahbany

def greatest_difference(nums1, nums2):
    maxlength = 0
    if len(nums1) == len(nums2):
        for index, val in enumerate(nums1):
            length = 0
            if val < nums2[index]:
                length = int(nums2[index]) - int(val)
            else:
                length = int(val) - int(nums2[index])
            if length > maxlength:
                maxlength = length
        print("Maxlength: ", maxlength)
    else:
        print("List sizes do not match")


def can_pay_with_two_coins(denoms, amount):
    """ (list of int, int) -> bool
    
    Return True if and only if it is possible to form amount, which is a 
    number of cents, using exactly two coins, which can be of any of the 
    denominatins in denoms.
    
    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 20)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    False
    """
	
	
def all_fluffy(s):
    """ (str) -> bool

    Return True iff every letter in s is fluffy. Fluffy letters are those that
    appear in the word 'fluffy'.
    
    >>> all_fluffy('fullfly')
    True
    >>> all_fluffy('firefly')
    False
    """


def digital_sum(nums_list):
    """ (list of str) -> int
    
    Precondition: s.isdigit() holds for each string s in nums_list.
    
    Return the sum of all the digits in all strings in nums_list.
    
    >>> digital_sum(['64', '128', '256'])
    34
    >>> digital_sum(['12', '3'])
    6
    """
    


def count_collatz_steps(n):
    """ (int) -> int
    
    Return the number of steps it takes to reach 1, by applying the two steps
    of the Collatz conjecture beginning from n.

    >>> count_collatz_steps(6)
    8
    """

    
    
