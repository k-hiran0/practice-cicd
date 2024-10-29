import unittest
from main import is_even 

class TestIsEven(unittest.TestCase):
    def test_even(self):
        # 偶数の場合のテスト
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(100))

    def test_odd(self):
        # 奇数の場合のテスト
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(99))
        self.assertFalse(is_even(-3))

    def test_negative_even(self):
        # 負の偶数の場合のテスト
        self.assertTrue(is_even(-4))

    def test_negative_odd(self):
        # 負の奇数の場合のテスト
        self.assertFalse(is_even(-5))

if __name__ == "__main__":
    unittest.main()
