import doctest


all_calls = {}

# A decorator function that consumes a func and check if the input was already given or not
# Input: func
# Output: string / return value of the func
# Example: isValid ("abc.def@mail.cc") => true
def lastcall(func):
    """
   >>> pow(3)
   9
   >>> pow(3)
   'I already told you that the answer is 9!'
   >>> pow(5)
   25
   >>> pow(3)
   'I already told you that the answer is 9!'
   >>> pow(5)
   'I already told you that the answer is 25!'
   >>> add(1)
   11
   >>> add(2)
   12
   >>> add(3)
   13
   >>> add(3)
   'I already told you that the answer is 13!'
   >>> add(2)
   'I already told you that the answer is 12!'
   >>> add(4)
   14
   >>> add(1)
   'I already told you that the answer is 11!'
    """

    # inner function that check if the input is in all_calls dict or not
    def wrapper(*args,**kwargs):
        if func not in all_calls.keys():
            all_calls[func] = dict()
        if args not in all_calls[func]:
            all_calls[func][args] = func(*args, **kwargs)  # there is the only line the function runs.
            return all_calls[func][args]
        return f"I already told you that the answer is {all_calls[func][args]}!"
    return wrapper


@lastcall
def add(y:float):
    return y+10

@lastcall
def pow(x:int):

    return x**2

@lastcall
def val(z:str):
    return z


if __name__ == '__main__':
    doctest.testmod()
    print(add(13))
    print(add(13))
    print(add(14))
    print(pow(13))
    print(pow(14))
    print(pow(14))

