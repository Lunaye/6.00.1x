# Problem 3


def convert_to_mandarin(us_num):
    '''
    us_num: a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    if len(us_num) == 1 or us_num == '10':
        return trans[us_num]

    teens = ['11', '12', '13', '14', '15', '16', '17', '18', '19']

    if us_num in teens:
        return 'shi ' + trans[us_num[1]]

    first = trans[us_num[0]]
    if us_num[1] == '0':
        return first + ' shi'
    else:
        sec = trans[us_num[1]]
        return first + ' shi ' + sec

# Problem 7


def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    def function_generator(L, x):
        k = len(L) - 1
        sum = 0
        for number in L:
            sum += number * x ** k
            k -= 1
        return sum

    def function(x, l=L):
        return function_generator(l, x)

    return function
