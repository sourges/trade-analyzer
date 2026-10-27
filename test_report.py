from report import format_report
import unittest


class TestFormatReport(unittest.TestCase):

    def test_mixed_trades(self):
        profits = [1.4652, -0.5, 0.2]
        expected = ("Trades: 3\n"
                    "Total profit: $1.17\n"
                    "Win rate: 66.7%\n"
                    "Profit factor: 3.33\n"
                    "Max drawdown: $0.50")
        answer = format_report(profits)
        self.assertEqual(answer, expected)

    def test_all_wins(self):
        profits = [0.18, 0.21]
        expected = ("Trades: 2\n"
                    "Total profit: $0.39\n"
                    "Win rate: 100.0%\n"
                    "Profit factor: inf (no losses)\n"
                    "Max drawdown: $0.00")
        answer = format_report(profits)
        self.assertEqual(answer, expected)

    def test_empty(self):
        profits = []
        expected = "No completed trades yet."
        answer = format_report(profits)
        self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()
