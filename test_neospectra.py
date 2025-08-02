# test_neospectra.py
"""
Tests for NeoSpectra module.
"""

import unittest
from neospectra import NeoSpectra

class TestNeoSpectra(unittest.TestCase):
    """Test cases for NeoSpectra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeoSpectra()
        self.assertIsInstance(instance, NeoSpectra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeoSpectra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
