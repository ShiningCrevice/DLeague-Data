import os
import json
import pandas as pd
from tabulate import tabulate

from utils import check_raw_data, int2bin

TG = "../data/games.csv"
TR = "../data/rounds.csv"
RAW = "../raw_data"
README_T = "../assets/README_temp.md"
README = "../README.md"

players = ['LJL7', '0MRS', '5JMY', 'PARY']
base_pts_1000 = [298100, 81900, -94100, -288900]
entries_zh = ['总得点', '平均顺位', '立直率', '和了率', '放铳率',
              '连对率', '避四率', '立直后和率', '立直后铳率', '平均打点',
              '平均铳点']
entries_en = ['Total Points', 'Average Placement', 'Riichi Rate', 'Winning Rate', 'Deal-In Rate',
              'Renchan Rate', 'Avoiding 4th Place Rate', 'Riichi Win Rate', 'Riichi Deal-In Rate',
              'Average Points Per Win', 'Average Points Lost Per Deal-In']
entries_abbr = ['TP', 'AP', 'RR', 'WR', 'DIR', 'RenR', 'A4R', 'RWR', 'RDIR', 'APW', 'APD']
bonus = [20000, -20000, -40000, -60000]


def process_data():
    SID, GID, Date, E, S, W, N, Scr_E, Scr_S, Scr_W, Scr_N, Rk_E, Rk_S, Rk_W, Rk_N, Pts_E, Pts_S, Pts_W, Pts_N = [
    ], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    SID_r, GID_r, RID, Ryukyo, Richi, Agari, Hoju, Var_E, Var_S, Var_W, Var_N = [
    ], [], [], [], [], [], [], [], [], [], []
    with open(README_T, 'r') as f:
        readme = f.read()
    seasons = sorted(os.listdir(RAW), key=lambda x: int(x[1:]), reverse=True)
    for s in seasons:
        sid = int(s[1:])
        total_points = {p: 0 for p in players}
        acc_rank = {p: 0 for p in players}
        cnt_richi = {p: 0 for p in players}
        cnt_agari = {p: 0 for p in players}
        cnt_hoju = {p: 0 for p in players}
        cnt_12 = {p: 0 for p in players}
        cnt_n4 = {p: 0 for p in players}
        cnt_ra = {p: 0 for p in players}
        cnt_rf = {p: 0 for p in players}
        agari_pts = {p: 0 for p in players}
        hoju_pts = {p: 0 for p in players}
        cnt_g = 0
        cnt_r = 0

        games = sorted(os.listdir(os.path.join(RAW, s)), key=lambda x: int(x[1:-5]))
        for g in games:
            gid = int(g[1:-5])
            with open(os.path.join(RAW, s, g)) as f:
                data = json.load(f)
            if not check_raw_data(data):
                continue
            p = [data[i]['PlayerId'] for i in range(4)]
            final_score = [data[i]['Score'][-1] for i in range(4)]
            sorted_score = sorted(final_score, reverse=True)
            ranking = [sorted_score.index(s) + 1 for s in final_score]
            points_1000 = [s + bonus[sorted_score.index(s)] for s in final_score]
            points = [round(p / 1000, 1) for p in points_1000]

            SID.append(data[0]['SID'])
            GID.append(data[0]['GID'])
            Date.append(data[0]['Time'].split('_')[0])
            E.append(p[0])
            S.append(p[1])
            W.append(p[2])
            N.append(p[3])
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

            for i in range(4):
                if sid == 1 and gid <= 49:
                    total_points[p[i]] += points_1000[i] / 2
                else:
                    total_points[p[i]] += points_1000[i]
                acc_rank[p[i]] += ranking[i]
                if ranking[i] == 1 or ranking[i] == 2:
                    cnt_12[p[i]] += 1
                if ranking[i] != 4:
                    cnt_n4[p[i]] += 1
            cnt_g += 1

            score = [data[i]['Score'] for i in range(4)]
            ops = [data[i]['Operations'] for i in range(4)]
            for k in range(1, len(score[0])):
                RID.append(k)
                SID_r.append(data[0]['SID'])
                GID_r.append(data[0]['GID'])
                Ryukyo.append(int2bin(1 if all(['N' in ops[i][k] for i in range(4)]) else 0))
                Richi.append(int2bin(sum([1 << i for i in range(4) if 'R' in ops[i][k]])))
                Agari.append(int2bin(sum([1 << i for i in range(4) if 'A' in ops[i][k]])))
                Hoju.append(int2bin(sum([1 << i for i in range(4) if 'F' in ops[i][k]])))
                Var_E.append(score[0][k] - score[0][k-1])
                Var_S.append(score[1][k] - score[1][k-1])
                Var_W.append(score[2][k] - score[2][k-1])
                Var_N.append(score[3][k] - score[3][k-1])

                for i in range(4):
                    cnt_richi[p[i]] += 1 if 'R' in ops[i][k] else 0
                    cnt_agari[p[i]] += 1 if 'A' in ops[i][k] else 0
                    cnt_hoju[p[i]] += 1 if 'F' in ops[i][k] else 0
                    cnt_ra[p[i]] += 1 if 'R' in ops[i][k] and 'A' in ops[i][k] else 0
                    cnt_rf[p[i]] += 1 if 'R' in ops[i][k] and 'F' in ops[i][k] else 0
                    if 'A' in ops[i][k]:
                        agari_pts[p[i]] += score[i][k] - score[i][k-1]
                    if 'F' in ops[i][k]:
                        hoju_pts[p[i]] += score[i][k-1] - score[i][k]
                        if 'R' in ops[i][k]:
                            hoju_pts[p[i]] -= 1000
                cnt_r += 1

        statistics = {}
        for i in range(4):
            statistics[players[i]] = [
                round(
                    (total_points[players[i]] + base_pts_1000[i] / 2 if sid == 1 else total_points[players[i]]) / 1000,
                    1),
                round(acc_rank[players[i]] / cnt_g, 2),
                round(100 * cnt_richi[players[i]] / cnt_r, 2),
                round(100 * cnt_agari[players[i]] / cnt_r, 2),
                round(100 * cnt_hoju[players[i]] / cnt_r, 2),
                round(100 * cnt_12[players[i]] / cnt_g, 2),
                round(100 * cnt_n4[players[i]] / cnt_g, 2),
                round(100 * cnt_ra[players[i]] / cnt_richi[players[i]] if cnt_richi[players[i]] != 0 else 0, 2),
                round(100 * cnt_rf[players[i]] / cnt_richi[players[i]] if cnt_richi[players[i]] != 0 else 0, 2),
                round(agari_pts[players[i]] / cnt_agari[players[i]] if cnt_agari[players[i]] != 0 else 0),
                round(hoju_pts[players[i]] / cnt_hoju[players[i]] if cnt_hoju[players[i]] != 0 else 0),]
        statistics = pd.DataFrame(statistics, columns=players, index=entries_en)
        statistics.to_csv(f"../statistics/{s}.csv")
        readme += f"\n## Statistics of {s}\n\n{tabulate(statistics, headers='keys', tablefmt='github')}\n"

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

    # print(readme)
    with open(README, 'w') as f:
        f.write(readme)


if __name__ == '__main__':
    process_data()
