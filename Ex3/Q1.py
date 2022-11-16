import doctest
import re

# A regular expression that will decide which email address is valid and which is not
regex = r'([A-Za-z0-9]+[-_.])*[A-Za-z0-9]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}'

# A function that consumes an email address and return true if it is valid and false if it is not valid email
# Input: string
# Output: boolean
# Example: isValid ("abc.def@mail.cc") => true
def isValid(email):

    if re.match(regex,email):
        return True
    else:
        return False


# A function that consumes a file path and prints two lists: valid email addressees and invalid email addressees
# Input: string
# Output: void
def printEmails(file):
    """
       :param email: email
       :return if email is valid True
               else False


       >>> isValid('abc.def@mail.cc')
       True
       >>> isValid('abc.def@mail-archive.com')
       True
       >>> isValid('abc.def@mail.org')
       True
       >>> isValid('abc.def@mail.com')
       True
       >>> isValid('aabc.def@mail.c')
       False
       >>> isValid('abc.def@mail#archive.com')
       False
       >>> isValid('abc.def@mail')
       False
       >>> isValid('abc.def@mail..com')
       False
       >>> isValid('abc-d@mail.com')
       True
       >>> isValid('abc.def@mail.com')
       True
       >>> isValid('abc@mail.com')
       True
       >>> isValid('abc_def@mail.com')
       True
       >>> isValid('abc-@mail.com')
       False
       >>> isValid('abc..def@mail.com')
       False
       >>> isValid('.abc@mail.com')
       False
       >>> isValid('abc#def@mail.com')
       False
       >>> isValid('abc-def.efgfg@mail.com')
       True
       >>> isValid('def.abc-aaa@mail.com')
       True
       >>> isValid('def.abc.cef@mail.com')
       True
       >>> isValid('abc.def_def@msmail.co.il')
       True
       >>> isValid('abc.abc..abc@mail.com')
       False
       >>> isValid('abc.abc-abc@mail.c')
       False
       >>> isValid('aaa.aaa-aa@a@mail.com')
       False
       >>> isValid('bbb.ccc-abc@msmail.l')
       False
       >>> isValid('abc_def+qwe@ma-il-com')
       False
       >>> isValid('abc_def+aaa@')
       False
       >>> isValid('abc_def.com')
       False
       """

    validmails = []
    invalidmails = []

    with open(file) as file:
        allrows = list(file.read().split('\n'))
        for row in allrows:
            allstrings = list(row.split(" "))
            for word in allstrings:
                if '@' in word:
                    if isValid(word):
                        validmails.append(word)
                    else:
                        invalidmails.append(word)

    print("valid emails: " + str(validmails))
    print("invalid emails: " + str(invalidmails))


if __name__ == '__main__':
    doctest.testmod()
    printEmails('file.txt')
