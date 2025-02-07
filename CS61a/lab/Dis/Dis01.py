def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i=1
    while i<=n:
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
        i+=1
    return None

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    from math import sqrt
    if n==1:
        return False
    i=2
    while i<=sqrt(n):
        if n%i==0:
            return False
        
        i += 1
    return True
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while n > 0:
        x = n % 10
        n = n // 10
        if not has_digit(n,x):
            i += 1
    return i

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n != 0:
        if n%10==k: return True
        n = n // 10
    return False
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.run_docstring_examples(unique_digits,globals(),True)