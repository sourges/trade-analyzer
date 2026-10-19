from analyzer import win_rate
import unittest

class TestWinRate(unittest.TestCase):

    def test_mixed_trades(self):
        profits = [2, -1, 3, -1]
        expected = 0.5
        answer = win_rate(profits)
        self.assertEqual(answer, expected)

    def test_all_wins(self):
        profits = [5, 5, 5]
        expected = 1
        answer = win_rate(profits)
        self.assertEqual(answer, expected)

    def test_all_losses(self):
        profits = [-1, -2]
        expected = 0
        answer = win_rate(profits)
        self.assertEqual(answer, expected)

    def test_zero_profit_is_not_a_win(self):
        profits = [0, 1]
        expected = 0.5
        answer = win_rate(profits)
        self.assertEqual(answer, expected)

    def test_empty_list_returns_zero(self):
        profits = []
        expected = 0
        answer = win_rate(profits)
        self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()