def sum_array(array):

    '''
    Calculate the sum of elements in an array
    
    Args:
        array (array)
    
    Returns:
        int: the sum of array
        
    Examples:
        >> sum_array(1)
        1
        >> sum_array(2)
        2
        >> sum_array(3)
        6
    '''
    return array[-1] + sum_array(array[:-1]) if array else 0        # calculate sum of array recursively

def fibonacci(n):

    """
    Calculate nth term in fibonacci sequence
    
    Args:
        n (int): nth term in fibonacci sequence to calculate
    
    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    
    Examples:
        >> fibonacci(1)
        1        
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """

    if n <= 1:      # catch end of recursion
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)      # calculate nth term recursively

def factorial(n):

    '''
    Calculate the factorial of n
    
    Args:
        n (int)
    
    Returns:
        int: n factorial
        
    Examples:
        >> factorial(1)
        1
        >> factorial(2)
        2
        >> factorial(3)
        6
    '''

    if n == 0:       # catch end of recursion
        return n
    elif n == 1:
        return n
    else:
        return n * factorial(n-1)       # compute factorial recursively

def reverse(word):

    '''
    Return word in reverse
    
    Args:
        word (string): word to reverse
    
    Returns:
        string: word in reverse
    
    Examples:
        >> reverse('foo')
        'oof'
        >> reverse('bar')
        'rab'
        >> reverse('python')
        'nohtyp'
    '''
    return word[-1] + reverse(word[:-1]) if word else ''    # reverse letters in word recursively
        