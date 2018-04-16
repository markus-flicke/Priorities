import sys
sys.path.append('/Users/m/code/python/trello')
from Trello import *
import pandas as pd
import argparse
Token = 'f703bd1e4f4fab4295e8a7a98b16067ff76315d90337b69020ab9b23b177873d'

parser = argparse.ArgumentParser(description='Token please')
parser.add_argument('Token', metavar='T', type=str, nargs='+',
                    help='Trello Token')
args = parser.parse_args()
Token = args.Token[0]

t = Trello(Token)
cards = t.get_cards()
df = pd.DataFrame(columns=['name', 'complexity', 'days', 'importance'])
for card in cards:
    raw_name = card['name']
    try:
        name, complexity = raw_name.split('#')
    except:
        raise AssertionError("Complexity value required")

    if not card['badges']['due'] == None:
        days = abs((pd.to_datetime(card['badges']['due']) - pd.datetime.now()) / pd.Timedelta(1.0, unit='D'))
    else:
        days = None
    importance = int(card['labels'][0]['name'])
        # IMPORTANCE.index(card['labels'][0]['name']) + 1

    df = df.append({'name': name, 'complexity': complexity, 'days': days, 'importance': importance}, ignore_index=True)

print(df)
df.to_csv('trello', index = False)