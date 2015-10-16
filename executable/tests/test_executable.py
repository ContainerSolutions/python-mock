#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from executable import ExecutableService

import unittest
import unittest.mock as mock

class ExecutableTestCase(unittest.TestCase):

  @mock.patch('subprocess.call')
  def test_cmdExists(self, mock_subprocess):
    reference = ExecutableService()

    mock_subprocess.call.return_value = 0

    self.assertTrue(reference.exists("docker"))


if __name__ == '__main__':
    unittest.main()

