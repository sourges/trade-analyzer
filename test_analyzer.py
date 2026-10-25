from analyzer import win_rate, profit_factor, max_drawdown
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

    def test_profit_factor(self):
        profits = [2, -1, 3, -1]
        expected = 2.5
        answer = profit_factor(profits)
        self.assertEqual(answer, expected)

    def test_positive_negative_profit_factor(self):
        profits = [3, -1]
        expected = 3
        answer = profit_factor(profits)
        self.assertEqual(answer, expected)

    def test_double_negative_profit_factor(self):
        profits = [-1, -2]
        expected = 0
        answer = profit_factor(profits)
        self.assertEqual(answer, expected)

    def test_zero_is_no_win_or_loss_profit_factor(self):
        profits = [4, 0, -2]
        expected = 2
        answer = profit_factor(profits)
        self.assertEqual(answer, expected)

    def test_no_losses_is_infinite(self):
        profits = [5, 5]
        expected = float('inf')
        answer = profit_factor(profits)
        self.assertEqual(answer, expected)

    def test_empty_profit_factor(self):
        profits = []
        expected = 0
        answer = profit_factor(profits)
        self.assertEqual(answer, expected)

    def test_max_drawdown_basic(self):
        profits = [2, -1, 3, -1]
        expected = 1
        answer = max_drawdown(profits)
        self.assertEqual(answer, expected)

    def test_max_drawdown_empty(self):
        profits = []
        expected = 0
        answer = max_drawdown(profits)
        self.assertEqual(answer, expected)

    def test_max_drawdown_no_losses(self):
        profits = [1, 2, 3]
        expected = 0
        answer = max_drawdown(profits)
        self.assertEqual(answer, expected)

    def test_max_drawdown_loss_first(self):
        profits = [-1, -2]
        expected = 3
        answer = max_drawdown(profits)
        self.assertEqual(answer, expected)

    def test_max_drawdown_losses_in_a_row(self):
        profits = [3, -2, -2, 1]
        expected = 4
        answer = max_drawdown(profits)
        self.assertEqual(answer, expected)

    def test_max_drawdown_recovery_not_new_high(self):
        profits = [5, -2, -2, 4, -6, 1]
        expected = 6
        answer = max_drawdown(profits)
        self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()