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