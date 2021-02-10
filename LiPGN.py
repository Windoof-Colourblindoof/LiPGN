from pip._internal import main as pipmain

pipmain(['install', 'python-lichess'])

import lichess.api
from lichess.format import SINGLE_PGN
from datetime import datetime
import re

with open('User.txt', 'r') as f:
   User = f.read()

DATET = datetime.now()
now = DATET.strftime("%m.%d.%Y %H;%M;%S")
pgn = lichess.api.user_games(User, max=1, format=SINGLE_PGN)
pgnNew = re.sub(r'([0-9]+\.+\s)', '\n\\1', pgn)

with open(now + '.pgn', 'w') as f:
   f.write(pgnNew)