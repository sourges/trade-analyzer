import sys
from analyzer import win_rate, profit_factor, max_drawdown, read_profits


def format_report(profits):
    """Turn a list of trade profits into a short text report."""
    if len(profits) == 0:
        return "No completed trades yet."

    pf = profit_factor(profits)
    if pf == float('inf'):
        pf_text = "inf (no losses)"
    else:
        pf_text = f"{pf:.2f}"

    lines = [
        f"Trades: {len(profits)}",
        f"Total profit: ${sum(profits):.2f}",
        f"Win rate: {win_rate(profits):.1%}",
        f"Profit factor: {pf_text}",
        f"Max drawdown: ${max_drawdown(profits):.2f}",
    ]
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python report.py <grid_completed_file.csv>")
        return
    filename = sys.argv[1]
    try:
        profits = read_profits(filename)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return
    print(format_report(profits))


if __name__ == '__main__':
    main()
