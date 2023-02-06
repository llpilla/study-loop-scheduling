#!/usr/bin/env python3

import unittest
import sys
# Add the parent directory to the path so we can import
# code from our simulator
sys.path.append('../')

from simulator.schedulers import OpenMPDynamic, OpenMPGuided, RecursiveBipartition, Nicol
from simulator.simulator import simulate

class OpenMPDynamicTest(unittest.TestCase):
    def setUp(self):
        self.tasks = [2, 4, 6, 8, 5, 3, 9, 2, 4, 6]
        self.num_resources = 3

    def test_round_robin(self):
        dynamic = OpenMPDynamic(self.tasks, self.num_resources, 1)
        result = simulate(self.tasks, self.num_resources, dynamic)
        mapping = result[0]

        self.assertEqual(result[1], 18)
        self.assertEqual(result[2], 10)
        self.assertEqual(result[3], 9)

        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 1)
        self.assertEqual(mapping[2], 2)
        self.assertEqual(mapping[3], 0)
        self.assertEqual(mapping[4], 1)
        self.assertEqual(mapping[5], 2)
        self.assertEqual(mapping[6], 1)
        self.assertEqual(mapping[7], 2)
        self.assertEqual(mapping[8], 0)
        self.assertEqual(mapping[9], 2)

    def test_chunk2(self):
        dynamic = OpenMPDynamic(self.tasks, self.num_resources, 2)
        result = simulate(self.tasks, self.num_resources, dynamic)
        mapping = result[0]

        self.assertEqual(result[1], 18)
        self.assertEqual(result[2], 5)
        self.assertEqual(result[3], 4)

        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 0)
        self.assertEqual(mapping[2], 1)
        self.assertEqual(mapping[3], 1)
        self.assertEqual(mapping[4], 2)
        self.assertEqual(mapping[5], 2)
        self.assertEqual(mapping[6], 0)
        self.assertEqual(mapping[7], 0)
        self.assertEqual(mapping[8], 2)
        self.assertEqual(mapping[9], 2)


class OpenMPGuidedTest(unittest.TestCase):
    def setUp(self):
        self.tasks = [2, 4, 6, 8, 5, 3, 9, 2, 4, 6]
        self.num_resources = 3

    def test_chunk1(self):
        guided = OpenMPGuided(self.tasks, self.num_resources, 1)
        result = simulate(self.tasks, self.num_resources, guided)
        mapping = result[0]

        self.assertEqual(result[1], 19)
        self.assertEqual(result[2], 7)
        self.assertEqual(result[3], 5)

        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 0)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 1)
        self.assertEqual(mapping[4], 1)
        self.assertEqual(mapping[5], 2)
        self.assertEqual(mapping[6], 2)
        self.assertEqual(mapping[7], 0)
        self.assertEqual(mapping[8], 2)
        self.assertEqual(mapping[9], 1)

    def test_chunk2(self):
        guided = OpenMPGuided(self.tasks, self.num_resources, 2)
        result = simulate(self.tasks, self.num_resources, guided)
        mapping = result[0]

        self.assertEqual(result[1], 18)
        self.assertEqual(result[2], 5)
        self.assertEqual(result[3], 4)

        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 0)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 1)
        self.assertEqual(mapping[4], 1)
        self.assertEqual(mapping[5], 2)
        self.assertEqual(mapping[6], 2)
        self.assertEqual(mapping[7], 0)
        self.assertEqual(mapping[8], 0)
        self.assertEqual(mapping[9], 2)


class RBTest(unittest.TestCase):
    def setUp(self):
        self.tasks = [2, 4, 6, 8, 5, 3, 9, 1, 11, 7]

    def test_two(self):
        self.num_resources = 2
        rb = RecursiveBipartition(self.tasks, self.num_resources)
        result = simulate(self.tasks, self.num_resources, rb)
        mapping = result[0]

        self.assertEqual(result[1], 28)
        self.assertEqual(result[2], 2)
        self.assertEqual(result[3], 1)

        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 0)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 0)
        self.assertEqual(mapping[4], 0)
        self.assertEqual(mapping[5], 0)
        self.assertEqual(mapping[6], 1)
        self.assertEqual(mapping[7], 1)
        self.assertEqual(mapping[8], 1)
        self.assertEqual(mapping[9], 1)


    def test_four(self):
        self.num_resources = 4
        rb = RecursiveBipartition(self.tasks, self.num_resources)
        result = simulate(self.tasks, self.num_resources, rb)
        mapping = result[0]

        self.assertEqual(result[1], 18)
        self.assertEqual(result[2], 4)
        self.assertEqual(result[3], 3)

        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 0)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 1)
        self.assertEqual(mapping[4], 1)
        self.assertEqual(mapping[5], 1)
        self.assertEqual(mapping[6], 2)
        self.assertEqual(mapping[7], 2)
        self.assertEqual(mapping[8], 3)
        self.assertEqual(mapping[9], 3)


class NicolTest(unittest.TestCase):
    def setUp(self):
        self.tasks = [2, 4, 6, 8, 5, 3, 9, 1, 11, 7]

    def test_three(self):
        self.num_resources = 3
        nicol = Nicol(self.tasks, self.num_resources)
        result = simulate(self.tasks, self.num_resources, nicol)
        mapping = result[0]

        self.assertEqual(result[1], 20)
        self.assertEqual(result[2], 3)
        self.assertEqual(result[3], 2)

        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 0)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 0)
        self.assertEqual(mapping[4], 1)
        self.assertEqual(mapping[5], 1)
        self.assertEqual(mapping[6], 1)
        self.assertEqual(mapping[7], 1)
        self.assertEqual(mapping[8], 2)
        self.assertEqual(mapping[9], 2)


if __name__ == '__main__':
    unittest.main()
