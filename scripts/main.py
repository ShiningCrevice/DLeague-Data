import os
import os.path as osp
import json
import pandas as pd
from tabulate import tabulate

from utils import check_raw_data, int2bin, build_debug_csv, fix_player_id
from utils import entries_abbr as readme_entries, entries_switch

TG = "data/games.csv"
TR = "data/rounds.csv"
RAW = "raw_data"
README_T = "docs/README_temp.md"
README = "README.md"
STATS_DIR = "statistics"

players = ['LJL7', '0MRS', '5JMY', 'PARY']
players_map = {'wk': 'LJL7', 'gy': '0MRS', 'tb': '5JMY', 'cc': 'PARY'}
bonus_ml = [20000, -20000, -40000, -60000]  # MLeague马点
bonus_skis = [5000, -15000, -35000, -55000] # 最高位战马点
s1_base_pt_1000 = [298100, 81900, -94100, -288900]  # S1前期APP未开发时的初始分
n_regular_games = [0, 49, 50, 35]   # 第0项为占位，此后每项为每个赛季常规赛的场次，常规赛未结束时不用记


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
        total_pt_1000 = {p: 0 for p in players}
        raw_pt_1000 = {p: 0 for p in players}
        acc_rank = {p: 0 for p in players}
        cnt_richi = {p: 0 for p in players}
        cnt_agari = {p: 0 for p in players}
        cnt_hoju = {p: 0 for p in players}
        cnt_1 = {p: 0 for p in players}
        cnt_2 = {p: 0 for p in players}
        cnt_3 = {p: 0 for p in players}
        cnt_4 = {p: 0 for p in players}
        cnt_ra = {p: 0 for p in players}
        cnt_rf = {p: 0 for p in players}
        agari_scr = {p: 0 for p in players}
        hoju_scr = {p: 0 for p in players}
        highest_scr = {p: 0 for p in players}
        lowest_scr = {p: 1000000 for p in players}
        cnt_g = 0
        cnt_r = 0

        games = os.listdir(osp.join(RAW, s))
        unique_names = {}
        for f in games:
            b, e = osp.splitext(f)
            if b not in unique_names or e == '.json':
                unique_names[b] = f
            else:
                print(f"Waring: Duplicate file name {f} in {s}.")
        games = list(unique_names.values())
        games.sort(key=lambda x: int(osp.splitext(x)[0][1:]))
        for g in games:
            gid = int(osp.splitext(g)[0][1:])
            if osp.splitext(g)[1] == '.json': 
                file_path = osp.join(RAW, s, g)
                fix_player_id(file_path)  # 修正PlayerId
                with open(file_path) as f:
                    data = json.load(f)
                if s != 'S1':
                    legal, msg = check_raw_data(data)
                    if not legal:
                        print(f"Error in {s}/G{gid:02d}: {msg}")
                        build_debug_csv(f'{s}/G{gid:02d}')
                        continue
                    else:
                        if osp.exists(f"debug_{s}_G{gid:02d}.csv"):
                            os.remove(f"debug_{s}_G{gid:02d}.csv")
                            print(f"Removed debug_{s}_G{gid:02d}.csv.")
                p = [data[i]['PlayerId'] for i in range(4)]
                final_score = [data[i]['Score'][-1] for i in range(4)]
                sorted_score = sorted(final_score, reverse=True)
                ranking = [sorted_score.index(s) + 1 for s in final_score]
                if sid in [1, 2]:   # 使用MLeague马点的赛季
                    points_1000 = [s + bonus_ml[sorted_score.index(s)] for s in final_score]
                elif sid in [3,]:  # 使用最高位战马点的赛季
                    points_1000 = [s + bonus_skis[sorted_score.index(s)] for s in final_score]
                raw_points_1000 = [s - 25000 for s in final_score]
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
                    if gid <= n_regular_games[sid if sid < len(n_regular_games) else 0]:
                        total_pt_1000[p[i]] += points_1000[i] / 2
                    else:
                        total_pt_1000[p[i]] += points_1000[i]
                    raw_pt_1000[p[i]] += raw_points_1000[i]
                    acc_rank[p[i]] += ranking[i]
                    if ranking[i] == 1:
                        cnt_1[p[i]] += 1
                    elif ranking[i] == 2:
                        cnt_2[p[i]] += 1
                    elif ranking[i] == 3:
                        cnt_3[p[i]] += 1
                    elif ranking[i] == 4:
                        cnt_4[p[i]] += 1
                    if final_score[i] > highest_scr[p[i]]:
                        highest_scr[p[i]] = final_score[i]
                    if final_score[i] < lowest_scr[p[i]]:
                        lowest_scr[p[i]] = final_score[i]
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
                            agari_scr[p[i]] += score[i][k] - score[i][k-1]
                        if 'F' in ops[i][k]:
                            hoju_scr[p[i]] += score[i][k-1] - score[i][k]
                    cnt_r += 1
                
            elif osp.splitext(g)[1] == '.txt':
                data = []
                with open(osp.join(RAW, s, g)) as f:
                    for line in f:
                        data.append(line.strip().split())
                p = [players_map[data[i][0]] for i in range(4)]
                final_score = [int(data[i][1]) for i in range(4)]
                sorted_score = sorted(final_score, reverse=True)
                ranking = [sorted_score.index(s) + 1 for s in final_score]
                points_1000 = [s + bonus_ml[sorted_score.index(s)] for s in final_score]
                raw_points_1000 = [s - 25000 for s in final_score]
                points = [round(p / 1000, 1) for p in points_1000]

                SID.append(sid)
                GID.append(gid)
                Date.append('Unknown')
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
                    if gid <= n_regular_games[sid if sid < len(n_regular_games) else 0]:
                        total_pt_1000[p[i]] += points_1000[i] / 2
                    else:
                        total_pt_1000[p[i]] += points_1000[i]
                    raw_pt_1000[p[i]] += raw_points_1000[i]
                    acc_rank[p[i]] += ranking[i]
                    if ranking[i] == 1:
                        cnt_1[p[i]] += 1
                    elif ranking[i] == 2:
                        cnt_2[p[i]] += 1
                    elif ranking[i] == 3:
                        cnt_3[p[i]] += 1
                    elif ranking[i] == 4:
                        cnt_4[p[i]] += 1
                    if final_score[i] > highest_scr[p[i]]:
                        highest_scr[p[i]] = final_score[i]
                    if final_score[i] < lowest_scr[p[i]]:
                        lowest_scr[p[i]] = final_score[i]
                cnt_g += 1
            
            else:
                print(f"Error: Unknown file type in {s}/{g}")
                continue
        

        statistics = {}
        for i in range(4):
            statistics[players[i]] = [
                round((total_pt_1000[players[i]] + s1_base_pt_1000[i] / 2 if sid == 1
                       else total_pt_1000[players[i]]) / 1000, 1),
                round(raw_pt_1000[players[i]] / 1000, 1),
                round(acc_rank[players[i]] / cnt_g, 2),
                round(100 * cnt_richi[players[i]] / cnt_r, 2),
                round(100 * cnt_agari[players[i]] / cnt_r, 2),
                round(100 * cnt_hoju[players[i]] / cnt_r, 2),
                round(100 * (cnt_1[players[i]] + cnt_2[players[i]]) / cnt_g, 2),
                round(100 * (cnt_1[players[i]] + cnt_2[players[i]] + cnt_3[players[i]]) / cnt_g, 2),
                round(100 * cnt_ra[players[i]] / cnt_richi[players[i]] if cnt_richi[players[i]] != 0 else 0, 2),
                round(100 * cnt_rf[players[i]] / cnt_richi[players[i]] if cnt_richi[players[i]] != 0 else 0, 2),
                round(agari_scr[players[i]] / cnt_agari[players[i]] if cnt_agari[players[i]] != 0 else 0),
                round(hoju_scr[players[i]] / cnt_hoju[players[i]] if cnt_hoju[players[i]] != 0 else 0),
                cnt_1[players[i]],
                cnt_2[players[i]],
                cnt_3[players[i]],
                cnt_4[players[i]],
                highest_scr[players[i]],
                lowest_scr[players[i]]
            ]
        statistics = pd.DataFrame(statistics, columns=players, index=readme_entries)
        statistics.to_csv(osp.join(STATS_DIR, f"{s}.csv"))
        statistics = statistics.loc[entries_switch]
        if sid == len(seasons): # 只展示最新赛季的统计数据
            if sid < len(n_regular_games):  # 进入决赛
                readme += f"\n{tabulate(statistics, headers='keys', tablefmt='github')}\n"
            else:   # 常规赛未结束
                readme += f"\n{tabulate(statistics, headers='keys', tablefmt='github')}\n"

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
    print("Updated data and statistics.")

    # print(readme)
    with open(README, 'w') as f:
        f.write(readme)
    print("Updated README.")


if __name__ == '__main__':
    if os.getcwd().split('/')[-1] == 'scripts' or os.getcwd().split('\\')[-1] == 'scripts':
        os.chdir('..')
    process_data()
