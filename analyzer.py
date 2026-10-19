def win_rate(profits):
    wins = 0
    if len(profits) == 0:
        return 0
    for p in profits:
        if p > 0:
            wins += 1
    return None

if __name__ == '__main__':
    profits = []
    print(win_rate(profits))