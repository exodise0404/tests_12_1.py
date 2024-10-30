import unittest



class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 10

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj1 = Runner('Объект1')
        for i in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 100)


    def test_run(self):
        obj2 = Runner('Объект2')
        for i in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    def test_challenge(self):
        obj3 = Runner('Объект3')
        obj4 = Runner('Объект4')
        for i in range(10):
            obj3.run()
            obj4.walk()
        self.assertEqual(obj3.distance, obj4.distance)

if __name__ == "__main__":
    unittest.main()