from unittest.mock import MagicMock

import unittest
from production import ProductionClass

thing = ProductionClass()
thing.run = MagicMock(return_value=3)
returned = thing.run(2)
thing.run.assert_called_with(2)
assert returned == 3

if __name__ == '__main__':
    unittest.main()
