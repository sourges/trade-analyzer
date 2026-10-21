def win_rate(profits):
    wins = 0
    if len(profits) == 0:
        # No trades = 0 (could have used ValueError)
        return 0
    for p in profits:
        if p > 0:
            wins += 1
    return wins / len(profits)

def profit_factor(profits):
    wins = 0
    losses = 0
    if len(profits) == 0:
        return 0
    for p in profits:
        if p > 0:
            wins += p
        elif p < 0:
            losses += abs(p)
    if losses == 0:
        # No losing trades: profit factor is infinite (normal for a grid bot,
        # where every completed trade is a win), so return inf instead of crashing.
        return float('inf')
    return wins / losses



if __name__ == '__main__':
    profits = []
    #print(win_rate(profits))
    print(profit_factor(profits))