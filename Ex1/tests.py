import unittest
from unittest import TestCase
from main import *


class Tests(unittest.TestCase):

    #f(x:int, y:float,z)
    #g(x,y:int,z)


    def test_q1(self):
            t1=safe_call(f,5,7.0,3)
            self.assertEqual(15.0, t1)
            self.assertRaises(ValueError, safe_call, f,7.0,5,3) #Not the same parameter types
            self.assertRaises(ValueError, safe_call, f, 5,3.0,3,4) #Too many args
            self.assertRaises(ValueError, safe_call, f, 5, 3.0)  # Less than the number of args needed
            self.assertRaises(ValueError, safe_call, f, 5,"abc" ,3)#Not the same parameter types
            self.assertEqual(7.0,safe_call(g,3.0,4,7.0))
            self.assertEqual(7.0,safe_call(g,"abc", 4, 7.0))
            self.assertEqual("abc", safe_call(g,3, 4, "abc"))
            self.assertRaises(ValueError, safe_call, g, 5, "abc", 3)

    def test_q2(self):
        l1=breadth_first_search(start=(0,0),end=(2,2),neighbor_function=four_neighbor_function)
        l1_ans=[(0,0),(1,0),(2,0),(2,1),(2,2)]
        self.assertEqual(l1, l1_ans)
        l2=breadth_first_search(start=(2,2),end=(0,0),neighbor_function=four_neighbor_function)
        l2_ans=[(2,2),(1,2),(0,2),(0,1),(0,0)]
        self.assertEqual(l2, l2_ans)
        l3 = breadth_first_search(start=(0, 0), end=(1,4), neighbor_function=four_neighbor_function)
        l3_ans = [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3),(1 , 4)]
        self.assertEqual(l3, l3_ans)
        l4 = breadth_first_search(start=(-5, -3), end=(-8, -2), neighbor_function=four_neighbor_function)
        l4_ans = [(-5, -3), (-6, -3), (-7, -3), (-8, -3), (-8, -2)]
        self.assertEqual(l4, l4_ans)
        l5 = breadth_first_search(start=(-4, -3.5), end=(2, -1.5), neighbor_function=four_neighbor_function)
        l5_ans = [(-4, -3.5), (-3, -3.5), (-2, -3.5), (-1, -3.5), (0, -3.5), (1,-3.5), (2,-3.5),(2,-2.5),(2,-1.5)]
        self.assertEqual(l5, l5_ans)

    def test_q3(self):
        x={"a":5,"c":6,"b":[1,3,2,4]}
        t1=print_sorted(x)
        t1_ans = {"a":5,"b":[1,2,3,4],"c":6}
        self.assertEqual(t1, t1_ans)
        y= {"0":1,"-1":2,"1":[-3,4,1,2]}
        t2 = print_sorted(y)
        t2_ans = {"-1":2,"0":1,"1":[-3,1,2,4]}
        self.assertEqual(t2,t2_ans)




if __name__ == '__main__':
    unittest.main()