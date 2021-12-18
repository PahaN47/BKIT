import unittest
from computer import computer
from microprocessor import microprocessor
from cmlink import cmlink
import main

computers = [
    computer("Computer Sergey"),
    computer("Amazing Computer 3000"),
    computer("The Box")
]

microprocessors = [
    microprocessor("intel core i3", 10000, computers[0].getid()),
    microprocessor("intel core i5", 15000, computers[1].getid()),
    microprocessor("intel core i7", 30000, computers[2].getid()),
    microprocessor("intel xeon", 600000, computers[2].getid())
]


# список для третьего задания. связи в первых двух заданиях отличаются
# и никак не связаны с третьим заданием. 
# в третьем задании поле id микропроцессора игнорируется
cmlinks = [
    cmlink(computers[0].getid(), microprocessors[0].getid()),
    cmlink(computers[1].getid(), microprocessors[0].getid()),
    cmlink(computers[1].getid(), microprocessors[1].getid()),
    cmlink(computers[2].getid(), microprocessors[0].getid()),
    cmlink(computers[2].getid(), microprocessors[1].getid()),
    cmlink(computers[2].getid(), microprocessors[2].getid()),
    cmlink(computers[2].getid(), microprocessors[3].getid())
]

class rk2_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(main.task1(computers, microprocessors), 
        { 
            'Amazing Computer 3000': ['intel core i5'] 
        })

    def test2(self):
        self.assertEqual(main.task2(computers, microprocessors),
        [ 
            ('The Box', 600000),
            ('Amazing Computer 3000', 15000), 
            ('Computer Sergey', 10000)
        ])
    
    def test3(self):
        self.assertEqual(main.task3(computers, microprocessors, cmlinks),
        [
            ('Computer Sergey', 'intel core i3'), 
            ('Amazing Computer 3000', 'intel core i3'), 
            ('Amazing Computer 3000', 'intel core i5'), 
            ('The Box', 'intel core i3'), 
            ('The Box', 'intel core i5'), 
            ('The Box', 'intel core i7'), 
            ('The Box', 'intel xeon'),
        ])

if __name__ == "__main__":
    unittest.main()