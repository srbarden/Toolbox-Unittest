import unittest


def removeNeg(numbers):
    new_numbers = list()
    for i in numbers:
        if i > 0:
            new_numbers += [i]
    return new_numbers


def sort(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers


class TestFunctions(unittest.TestCase):
    def test_removeNeg(self):
        numbers = [-1, 2, -2, 0, 1]
        self.assertEqual(numbers.removeNeg(), [2, 0, 1])

    def test_sort(self):
        numbers = [2, 0, 1]
        self.assertEqual(numbers.sort(), [0, 1, 2])


if __name__ == '__main__':
    numbers = [-2, -1, 2, 1]
    rn = removeNeg(numbers)
    sorted_rn = sort(rn)

    unittest.main()
