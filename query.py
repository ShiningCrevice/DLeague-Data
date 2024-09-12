import mysql.connector
import numpy as np
import pandas as pd
import argparse

HOST = 'localhost'
USER = 'root'
PASSWD = ''
DATABASE = 'sdl_data'
TABLE_G = 'games'
TABLE_R = 'rounds'

if __name__ == '__main__':
    argpar = argparse.ArgumentParser()
    argpar.add_argument('-H', '--host', dest='Host', type=str)
    argpar.add_argument('-u', '--user', dest='User', type=str)
    argpar.add_argument('-p', '--password', dest='Password', type=str)
    argpar.add_argument('-d', '--database', dest='Database', type=str)
    argpar.add_argument('-g', '--table-g', dest='Table_G', type=str)
    argpar.add_argument('-r', '--table-r', dest='Table_R', type=str)

    HOST = argpar.parse_args().Host or HOST
    USER = argpar.parse_args().User or USER
    PASSWD = argpar.parse_args().Password or PASSWD
    DATABASE = argpar.parse_args().Database or DATABASE
    TABLE_G = argpar.parse_args().Table_G or TABLE_G
    TABLE_R = argpar.parse_args().Table_R or TABLE_R

    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        database=DATABASE
    )
    cursor = db.cursor()

    qgames = "SELECT * FROM games ORDER BY gid"
    qrounds = "SELECT richi, agari, hoju, ve, vs, vw, vn " + \
              "FROM rounds WHERE gid={} ORDER BY rid"

    cursor.execute(qgames)
    games = cursor.fetchall()

    players = ["LJL7", "0MRS", "5JMY", "PARY"]
    bonus = [20000, -20000, -40000, -60000]
    base_pts = [298.1, 81.9, -94.1, -288.9]

    richi = {p: [] for p in players}
    agari = {p: [] for p in players}
    hoju = {p: [] for p in players}
    ranking = {p: [] for p in players}
    agari_pts = {p: 0 for p in players}
    hoju_pts = {p: 0 for p in players}
    rank_mat = {p: np.zeros([5, 4], dtype=int) for p in players}

    pts = {p: 0 for p in players}
    cnt = 0  # for rounds
    cntg = len(games)

    for g in games:
        # print(g)
        # exit()
        p = [g[2], g[3], g[4], g[5]]
        scr = np.array([g[6], g[7], g[8], g[9]])
        for x in range(4):
            i = np.argmax(scr)
            pts[p[i]] += (
                (scr[i] + bonus[x]) // 100 if g[0] >= 50
                else (scr[i] + bonus[x]) // 200
            )
            ranking[p[i]].append(x+1)
            rank_mat[p[i]][i][x] += 1
            rank_mat[p[i]][4][x] += 1
            scr[i] = -9999999
        # if (sum(pts.values()) != 0):
        #     print(g[0])
        # assert sum(pts.values()) == 0

        cursor.execute(qrounds.format(g[0]))
        rounds = cursor.fetchall()
        for r in rounds:
            cnt += 1
            for k in range(4):
                richi[p[k]].append(1 if r[0] & (1 << k) else 0)
                agari[p[k]].append(1 if r[1] & (1 << k) else 0)
                hoju[p[k]].append(1 if r[2] & (1 << k) else 0)
                agari_pts[p[k]] += r[k+3] if r[1] & (1 << k) else 0
                hoju_pts[p[k]] -= r[k+3] if r[2] & (1 << k) else 0

    # print(ranking)

    cnt_R = [sum(richi[p]) for p in players]
    cnt_A = [sum(agari[p]) for p in players]
    cnt_F = [sum(hoju[p]) for p in players]
    cnt_RA = [sum([richi[p][i] & agari[p][i] for i in range(cnt)])
              for p in players]
    cnt_RF = [sum([richi[p][i] & hoju[p][i] for i in range(cnt)])
              for p in players]
    cnt_12 = [ranking[p].count(1)+ranking[p].count(2) for p in players]
    cnt_n4 = [cntg-ranking[p].count(4) for p in players]

    main_data = [
        [pts[players[i]] / 10 + base_pts[i] / 2 for i in range(4)],
        [pts[players[i]] / 10 for i in range(4)],
        [sum(ranking[players[i]]) / cntg for i in range(4)],
        [cnt_R[i] / cnt * 100 for i in range(4)],
        [cnt_A[i] / cnt * 100 for i in range(4)],
        [cnt_F[i] / cnt * 100 for i in range(4)],

        [cnt_12[i] / cntg * 100 for i in range(4)],
        [cnt_n4[i] / cntg * 100 for i in range(4)],
        [cnt_RA[i] / cnt_R[i] * 100 for i in range(4)],
        [cnt_RF[i] / cnt_R[i] * 100 for i in range(4)],
        [agari_pts[players[i]] // cnt_A[i] for i in range(4)],
        [hoju_pts[players[i]] // cnt_F[i] for i in range(4)]
    ]
    main_rows = ['G2起得分', 'G15起得分', '平均顺位', '立直率', '和了率', '放铳率',
                 '连对率', '避四率', '立直后和率', '立直后铳率', '平均打点', '平均铳点']
    dlen = len(main_data)

    df = pd.DataFrame({main_rows[i]: main_data[i] for i in range(dlen)})
    for i in range(2):
        df[main_rows[i]] = df[main_rows[i]].round(1)
    for i in range(2, dlen-2):
        df[main_rows[i]] = df[main_rows[i]].round(2)

    df = df.T
    df.columns = players
    df.to_csv('statistics/statistics.csv', encoding='utf-8-sig')

    rankings = ['1位', '2位', '3位', '4位']
    orders = ['东起', '南起', '西起', '北起', '总数']
    rm = pd.DataFrame({rankings[i]: [] for i in range(4)})
    for p in players:
        t1 = pd.DataFrame({rankings[i]: [rankings[i]] for i in range(4)})
        t1.index = [p]
        t2 = pd.DataFrame(rank_mat[p])
        t2.columns = rankings
        t2.index = orders
        rm = pd.concat([rm, t1, t2])
    rm.to_csv('statistics/ranking_matrices.csv',
              encoding='utf-8-sig', header=False)

    print("Statistics saved to statistics.csv and ranking_matrices.csv")
