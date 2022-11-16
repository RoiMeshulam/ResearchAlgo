import doctest

# A class 'List' , it is similar to the regular list of Python but allows to get items in the syntax of a two-dimensional array

class List(list):
    def __getitem__(self, index):

        """
       >>> mylist = List([[[8.9,6,[1, 2, 3], 4, 44],['a','b','c',55]],[[17,28,39,4],[10,11,12,123]],[[130,140,150,151],[16,17,18,188]]])
       >>> mylist[0,0,2,2] == 3
       True
       >>> mylist[0,0,2,2] == 3
       True
       >>> mylist[1,0,2] == 39
       True
       >>> mylist[0,1] == ['a','b','c',55]
       True
       >>> mylist[0,1,2] == 'c'
       True
       """


        if not isinstance(index, int):
            output = list(self)
        else:
            return list(self)[index]
        for key in index:
            output = output[key]
        return output





if __name__ == '__main__':
    doctest.testmod()
    # # Example
    mylist = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])
    # Should print 66
    print(mylist[0,1,3])
    # Should print [[1, 2, 3, 33], [4, 5, 6, 66]]
    print(mylist[0])