# test_tidemeld.py
"""
Tests for TideMeld module.
"""

import unittest
from tidemeld import TideMeld

class TestTideMeld(unittest.TestCase):
    """Test cases for TideMeld class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TideMeld()
        self.assertIsInstance(instance, TideMeld)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TideMeld()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
