#!/usr/bin/env python

import unittest

import graceful_trees as gt

class GracefulTreesTest(unittest.TestCase):
  def setUp(self):
    self.mnstar_33 =\
        (1, [
          (10, [(2, [(9, [])])]),
          (7,  [(5, [(6, [])])]),
          (4,  [(8, [(3, [])])]),
          ])

  def tearDown(self):
    pass

  def test_graceful_mnstar(self):
    m = 5
    n = 4
    gt.print_graceful_mnstar(
        gt.graceful_mnstar(m, n)
    )
    print()
    gt.print_graceful_mnstar(
        gt.graceful_mnstar_edges(
            gt.graceful_mnstar(m, n)
        )
    )

if __name__ == '__main__':
  unittest.main()
