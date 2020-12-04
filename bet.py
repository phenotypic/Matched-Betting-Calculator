from tabulate import tabulate
from prettytable import PrettyTable

back_stake = float(input('\nBack stake: '))
back_odds = float(input('Back odds: '))

lay_odds = float(input('\nLay odds: '))
commission = int(input('Lay commission (%): ')) / 100


def qualifier():
    lay_stake = back_odds * back_stake / (lay_odds - commission)
    profit = lay_stake * (1 - commission) - back_stake
    return lay_stake, profit


def snr():
    lay_stake = (back_odds - 1) / (lay_odds - commission) * back_stake
    profit = lay_stake * (1 - commission)
    return lay_stake, profit


def sr():
    lay_stake = (back_odds * back_stake) / (lay_odds - commission)
    profit = lay_stake * (1 - commission)
    return lay_stake, profit


def lbr():
    refund_value = float(input('\nRefund value: '))
    lay_stake = ((back_stake * back_odds) - refund_value) / (lay_odds - commission)
    profit = lay_stake * (1 - commission)
    return lay_stake, profit


bets = [[1, 'Qualifying bet'], [2, 'Free bet (SNR)'], [3, 'Free bet (SR)'], [4, 'Lost bet refund']]
print('\n' + tabulate(bets, headers=['Option', 'Bet Type']))
method = int(input('\nSelect bet type: ')) - 1

lay_stake, profit = [qualifier, snr, sr, lbr][method]()
lay_liability = lay_stake * (lay_odds - 1)

list = PrettyTable(['Lay stake', 'Liability', 'Profit'])
list.add_row([round(lay_stake, 2), round(lay_liability, 2), round(profit, 2)])

print('\nResult for', bets[method][1] + ':')
print(list, '\n')
