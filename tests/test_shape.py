#!/usr/bin/env python

# Copyright (c) CTU  - All Rights Reserved
# Created on: 5/1/20
#     Author: Vladimir Petrik <vladimir.petrik@cvut.cz>

import numpy as np
import unittest
import sys

sys.path.append('lib')

from pyphysx import *


class SceneTestCase(unittest.TestCase):

    def test_local_pose(self):
        shape = Shape.create_sphere(1., Material())
        shape.set_local_pose([0, 2, 1])
        p, q = shape.get_local_pose()
        np.testing.assert_almost_equal(p, [0, 2, 1])
        np.testing.assert_almost_equal(q, [0, 0, 0, 1])

        shape.set_local_pose([0, 2, 1], [1, 0, 0, 1])
        p, q = shape.get_local_pose()
        np.testing.assert_almost_equal(p, [0, 2, 1])
        np.testing.assert_almost_equal(q, np.array([1, 0, 0, 1]) / np.sqrt(2))  # quaternion is always normalized

    def test_convex_mesh(self):
        points = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
        s = Shape.create_convex_mesh_from_points(points, Material(), scale=0.5)
        self.assertEqual(s.get_shape_data().shape[0], 4)  # 4 trianglular faces
        points = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0.5]])
        s = Shape.create_convex_mesh_from_points(points, Material(), scale=0.5)
        self.assertEqual(s.get_shape_data().shape[0], 6)  # additional 3 faces but one is removed from previous shape


if __name__ == '__main__':
    unittest.main()