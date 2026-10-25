from analyzer import win_rate, profit_factor, max_drawdown, read_profits
import unittest
import os

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

THREE_ROWS = """time,exchange,pair,side,entry_price,exit_price,amount,entry_cost,exit_cost,fees,profit
2026-10-25 10:00:00,kraken,CRV/USD,long,0.36964,0.38077,165.02,60.998,62.8347,0.3715,1.4652
2026-10-25 11:00:00,kraken,CRV/USD,short,0.38077,0.36964,160.2,61.0,59.2,0.36,-0.5
2026-10-25 12:00:00,kraken,CRV/USD,long,0.35884,0.36964,170.0,61.0,62.8,0.37,0.2
"""

class ReadProfitsTest(unittest.TestCase):

    def setUp(self):
        self.filename = 'test_trades.csv'
        self.header_file = 'test_header_only.csv'
        with open(self.filename, 'w', newline='') as f:
            f.write(THREE_ROWS)

    def test_read_three_row(self):
        expected = [1.4652, -0.5, 0.2]
        profits = read_profits(self.filename)
        self.assertEqual(profits, expected)

    def test_header_only(self):
        # write a file that has ONLY the column names, no trades
        header = THREE_ROWS.splitlines()[0]
        with open(self.header_file, 'w', newline='') as f:
            f.write(header)

        expected = []
        profits = read_profits(self.header_file)
        self.assertEqual(profits, expected)
    
    def test_win_rate_file(self):
        expected = 2/3
        profits = read_profits(self.filename)
        answer = win_rate(profits)
        self.assertAlmostEqual(answer, expected)

    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            read_profits('no_such_file.csv')
    
    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        if os.path.exists(self.header_file):
            os.remove(self.header_file)

    

if __name__ == '__main__':
    unittest.main()