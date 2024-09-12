import os
import json
import pandas as pd
from tabulate import tabulate

from utils import check_raw_data, int2bin


def update_data(*lst):
    TG = "../data/games.csv"
    TR = "../data/rounds.csv"
    RAW = "../raw_data"
    for t in [TG, TR]:
        if not os.path.exists(t):
            with open(t, 'w'):
                pass
            print(f"Created {t}")
    tg = pd.read_csv(TG)
    tr = pd.read_csv(TR)

    def update(game: str):
        global tg, tr
        if not game.endswith(".json"):
            game += ".json"
        with open(os.path.join(RAW, game)) as f:
            data = json.load(f)
        if not check_raw_data(data):
            return

        score = [data[i]['Score'][-1] for i in range(4)]
        sorted_score = sorted(score, reverse=True)
        bonus = [20000, -20000, -40000, -60000]
        points = [s + bonus[sorted_score.index(s)] for s in score]
        points = [round(p / 1000, 1) for p in points]
        new_g = {
            'SID': data[0]['SID'],
            'GID': data[0]['GID'],
            'Date': data[0]['Time'].split('_')[0],
            'E': data[0]['PlayerId'],
            'S': data[1]['PlayerId'],
            'W': data[2]['PlayerId'],
            'N': data[3]['PlayerId'],
            'Scr-E': score[0],
            'Scr-S': score[1],
            'Scr-W': score[2],
            'Scr-N': score[3],
            'Pts-E': points[0],
            'Pts-S': points[1],
            'Pts-W': points[2],
            'Pts-N': points[3],
        }
        tg = tg.append(new_g, ignore_index=True)

        Ryukyo, Tenpai, Richi, Agari, Hoju = [], [], [], [], []
        Variants = [[], [], [], []]
        for k in range(1, len(data[0]['Score'])):
            Ryukyo.append(1 if all(['N' in data[i]['Operations'][k] for i in range(4)]) else 0)
            Tenpai.append(0 if Ryukyo[-1] == 0 else sum([1 << i for i in range(4)
                          if data[i]['Score'][k] > data[i]['Score'][k-1]]))
            Richi.append(sum([1 << i for i in range(4) if 'R' in data[i]['Operations'][k]]))
            Agari.append(sum([1 << i for i in range(4) if 'A' in data[i]['Operations'][k]]))
            Hoju.append(sum([1 << i for i in range(4) if 'F' in data[i]['Operations'][k]]))
            Variants = [[data[i]['Score'][k] - data[i]['Score'][k-1] for i in range(4)]]

    if lst:
        if len(lst) == 2 and isinstance(lst[0], int) and isinstance(lst[1], int):
            update(f"S{lst[0]}/G{lst[1]}")
        else:
            for g in lst:
                update(g)
    else:
        seasons = sorted(os.listdir(RAW), key=lambda x: int(x[1:]))
        for s in seasons:
            games = sorted(os.listdir(os.path.join(RAW, s)), key=lambda x: int(x[1:]))
            for g in games:
                update(os.path.join(s, g))
