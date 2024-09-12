import os
import json
import pandas as pd
from tabulate import tabulate

from utils import check_raw_data, int2bin

TG = "../data/games.csv"
TR = "../data/rounds.csv"
RAW = "../raw_data"


def process_raw():
    SID, GID, Date, E, S, W, N, Scr_E, Scr_S, Scr_W, Scr_N, Rk_E, Rk_S, Rk_W, Rk_N, Pts_E, Pts_S, Pts_W, Pts_N = [
    ], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    SID_r, GID_r, RID, Ryukyo, Tenpai, Richi, Agari, Hoju, Var_E, Var_S, Var_W, Var_N = [
    ], [], [], [], [], [], [], [], [], [], [], []
    seasons = sorted(os.listdir(RAW), key=lambda x: int(x[1:]))
    for s in seasons:
        games = sorted(os.listdir(os.path.join(RAW, s)), key=lambda x: int(x[1:-5]))
        for g in games:
            with open(os.path.join(RAW, s, g)) as f:
                data = json.load(f)
            if not check_raw_data(data):
                continue
            final_score = [data[i]['Score'][-1] for i in range(4)]
            sorted_score = sorted(final_score, reverse=True)
            ranking = [sorted_score.index(s) + 1 for s in final_score]
            bonus = [20000, -20000, -40000, -60000]
            points = [s + bonus[sorted_score.index(s)] for s in final_score]
            points = [round(p / 1000, 1) for p in points]

            SID.append(data[0]['SID'])
            GID.append(data[0]['GID'])
            Date.append(data[0]['Time'].split('_')[0])
            E.append(data[0]['PlayerId'])
            S.append(data[1]['PlayerId'])
            W.append(data[2]['PlayerId'])
            N.append(data[3]['PlayerId'])
            Scr_E.append(final_score[0])
            Scr_S.append(final_score[1])
            Scr_W.append(final_score[2])
            Scr_N.append(final_score[3])
            Rk_E.append(ranking[0])
            Rk_S.append(ranking[1])
            Rk_W.append(ranking[2])
            Rk_N.append(ranking[3])
            Pts_E.append(points[0])
            Pts_S.append(points[1])
            Pts_W.append(points[2])
            Pts_N.append(points[3])

            score = [data[i]['Score'] for i in range(4)]
            ops = [data[i]['Operations'] for i in range(4)]
            for k in range(1, len(score[0])):
                RID.append(k)
                SID_r.append(data[0]['SID'])
                GID_r.append(data[0]['GID'])
                Ryukyo.append(1 if all(['N' in ops[i][k] for i in range(4)]) else 0)
                Tenpai.append(0 if Ryukyo[-1] == 0 else sum([1 << i for i in range(4) if score[i][k] > score[i][k-1]]))
                Richi.append(sum([1 << i for i in range(4) if 'R' in ops[i][k]]))
                Agari.append(sum([1 << i for i in range(4) if 'A' in ops[i][k]]))
                Var_E.append(score[0][k] - score[0][k-1])
                Var_S.append(score[1][k] - score[1][k-1])
                Var_W.append(score[2][k] - score[2][k-1])
                Var_N.append(score[3][k] - score[3][k-1])
                Hoju.append(sum([1 << i for i in range(4) if 'F' in ops[i][k]]))

    tg = pd.DataFrame({
        'SID': SID,
        'GID': GID,
        'Date': Date,
        'E': E,
        'S': S,
        'W': W,
        'N': N,
        'Scr-E': Scr_E,
        'Scr-S': Scr_S,
        'Scr-W': Scr_W,
        'Scr-N': Scr_N,
        'Rk-E': Rk_E,
        'Rk-S': Rk_S,
        'Rk-W': Rk_W,
        'Rk-N': Rk_N,
        'Pts-E': Pts_E,
        'Pts-S': Pts_S,
        'Pts-W': Pts_W,
        'Pts-N': Pts_N
    })
    tg.sort_values(by=['SID', 'GID'], ascending=[False, False], inplace=True)
    tg.to_csv(TG, index=False)

    tr = pd.DataFrame({
        'SID': SID_r,
        'GID': GID_r,
        'RID': RID,
        'Ryukyo': Ryukyo,
        'Tenpai': Tenpai,
        'Richi': Richi,
        'Agari': Agari,
        'Hoju': Hoju,
        'Var-E': Var_E,
        'Var-S': Var_S,
        'Var-W': Var_W,
        'Var-N': Var_N
    })
    tr.sort_values(by=['SID', 'GID', 'RID'], ascending=[False, False, False], inplace=True)
    tr.to_csv(TR, index=False)


def do_statistics(SID: int):
    tg = pd.read_csv(TG)
    tg = tg[tg['SID'] == SID]
    tr = pd.read_csv(TR)
    tr = tr[tr['SID'] == SID]

    players = ['LJL7', '0MRS', '5JMY', 'PARY']
    main_rows = ['赛季总得分', '平均顺位', '立直率', '和了率', '放铳率',
                 '连对率', '避四率', '立直后和率', '立直后铳率', '平均打点', '平均铳点']
    stats = [[], [], [], []]
    base_pts = [298.1, 81.9, -94.1, -288.9] if SID == 1 else [0, 0, 0, 0]

    richi = {p: [] for p in players}
    agari = {p: [] for p in players}
    hoju = {p: [] for p in players}
    agari_pts = {p: 0 for p in players}
    hoju_pts = {p: 0 for p in players}

    for r in tr.itertuples():
        print(r)
        g = tg[tg['GID'] == r['GID']]
        p = [g['E'], g['S'], g['W'], g['N']]
        d = ['E', 'S', 'W', 'N']
        for k in range(4):
            richi[p[k]].append(1 if r['Richi'] & (1 << k) else 0)
            agari[p[k]].append(1 if r['Agari'] & (1 << k) else 0)
            hoju[p[k]].append(1 if r['Hoju'] & (1 << k) else 0)
            agari_pts[p[k]] += r[f'Var-{d[k]}'] if r['Agari'] & (1 << k) else 0
            hoju_pts[p[k]] -= r[f'Var-{d[k]}'] if r['Hoju'] & (1 << k) else 0

    for i in range(4):
        stats[i].append(tg[tg['E'] == players[i]]['Pts-E'].sum()
                        + tg[tg['S'] == players[i]]['Pts-S'].sum()
                        + tg[tg['W'] == players[i]]['Pts-W'].sum()
                        + tg[tg['N'] == players[i]]['Pts-N'].sum()
                        + base_pts[i])  # 总得分
        stats[i].append((tg[tg['E'] == players[i]]['Rk-E'].sum()
                        + tg[tg['S'] == players[i]]['Rk-S'].sum()
                        + tg[tg['W'] == players[i]]['Rk-W'].sum()
                        + tg[tg['N'] == players[i]]['Rk-N'].sum()) / len(tg))  # 平均顺位
        stats[i].append(sum(richi[players[i]]) / len(tr))  # 立直率
        stats[i].append(sum(agari[players[i]]) / len(tr))  # 和了率
        stats[i].append(sum(hoju[players[i]]) / len(tr))  # 放铳率
        stats[i].append(tg[tg['E'] == players[i]]['Rk-E'].count(1) + tg[tg['E'] == players[i]]['Rk-E'].count(2) +
                        tg[tg['S'] == players[i]]['Rk-S'].count(1) + tg[tg['S'] == players[i]]['Rk-S'].count(2) +
                        tg[tg['W'] == players[i]]['Rk-W'].count(1) + tg[tg['W'] == players[i]]['Rk-W'].count(2) +
                        tg[tg['N'] == players[i]]['Rk-N'].count(1) + tg[tg['N'] == players[i]]['Rk-N'].count(2)
                        / len(tg))  # 连对率
        stats[i].append(len(tg) - tg[tg['E'] == players[i]]['Rk-E'].count(4)
                        - tg[tg['S'] == players[i]]['Rk-S'].count(4)
                        - tg[tg['W'] == players[i]]['Rk-W'].count(4)
                        - tg[tg['N'] == players[i]]['Rk-N'].count(4))  # 避四率
        stats[i].append(sum([richi[players[i]][j] & agari[players[i]][j]
                        for j in range(len(tr))]) / sum(richi[players[i]]))  # 立直后和率
        stats[i].append(sum([richi[players[i]][j] & hoju[players[i]][j]
                        for j in range(len(tr))]) / sum(richi[players[i]]))  # 立直后铳率
        stats[i].append(agari_pts[players[i]] / sum(agari[players[i]]))  # 平均打点
        stats[i].append(hoju_pts[players[i]] / sum(hoju[players[i]]))  # 平均铳点

    stats = pd.DataFrame(stats, columns=main_rows, index=players)
    stats.to_csv(f"../statistics/S{SID}.csv")


if __name__ == '__main__':
    do_statistics(1)
