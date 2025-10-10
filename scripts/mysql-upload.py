import json
import mysql.connector
import argparse

from utils import build_csv, fix_player_id


HOST = 'localhost'
USER = 'root'
PASSWD = ''
DATABASE = 'sdl_data'
TABLE_G = 'games'
TABLE_R = 'rounds'


def parse(records):
    """Return two lists of tuples, one for the game and the other for rounds.
    ### RECORDS must be in order of E-S-W-N! ###
    GAME includes GID, Date, E, S, W, N, Scr_{E,S,W,N}.
    ROUNDS includes GID, RID Ryukyo, Tenpai, Richi, Agari, Hoju, V{E,S,W,N}.

    Args:
        records (4-list of dicts): Every dict is from a json of record.
    """
    assert len(records) == 4, 'records amount error'

    gid = records[0]['GID']
    assert gid == records[1]['GID'] and gid == records[2]['GID'] and \
        gid == records[3]['GID'], 'GID inconsistency'
    date = records[0]['Time'].split('_')[0]
    player = [records[i]['PlayerId'] for i in range(4)]
    scr = [records[i]['Score'] for i in range(4)]
    assert sum([scr[i][-1] for i in range(4)]) == 100000, \
        'scores inconsistency'
    ops = [records[i]['Operations'] for i in range(4)]
    n = len(scr[0])
    assert n == len(scr[1]) and n == len(scr[2]) and n == len(scr[3]) \
        and n == len(ops[0]) and n == len(ops[1]) and n == len(ops[2]) and \
        n == len(ops[3]), 'number of rounds inconsistency'

    game = (gid, date, player[0], player[1], player[2], player[3],
            scr[0][-1], scr[1][-1], scr[2][-1], scr[3][-1])

    rounds = []
    for k in range(1, n):
        Ryukyo = 1 if (all(['N' in ops[i][k] for i in range(4)])) else 0
        Tenpai = 0 if Ryukyo == 0 else \
            sum([1 << i for i in range(4) if scr[i][k] > scr[i][k-1]])
        Richi = sum([1 << i for i in range(4) if 'R' in ops[i][k]])
        Agari = sum([1 << i for i in range(4) if 'A' in ops[i][k]])
        Hoju = sum([1 << i for i in range(4) if 'F' in ops[i][k]])
        V = [scr[i][k]-scr[i][k-1] for i in range(4)]
        rounds.append((gid, k, Ryukyo, Tenpai, Richi, Agari, Hoju,
                       V[0], V[1], V[2], V[3]))

    print("data parsed")

    return game, rounds


def upload(game, rounds):
    """Upload GAME and ROUNDS to mysql database above."""
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        database=DATABASE
    )
    cursor = db.cursor()

    # delete the possible repeated items
    gid = game[0]
    sql_del1 = f"delete from {TABLE_G} where gid={gid}"
    cursor.execute(sql_del1)
    sql_del2 = f"delete from {TABLE_R} where gid={gid}"
    cursor.execute(sql_del2)

    sql_game = f"insert into {TABLE_G} values {game}"
    cursor.execute(sql_game)
    sql_rounds = f"insert into {TABLE_R} values " \
        + "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(sql_rounds, rounds)

    db.commit()

    print("data commited")


if __name__ == '__main__':
    argpar = argparse.ArgumentParser()
    argpar.add_argument('File', help='Filename required.')
    argpar.add_argument('-H', '--host', dest='Host', type=str)
    argpar.add_argument('-u', '--user', dest='User', type=str)
    argpar.add_argument('-p', '--password', dest='Password', type=str)
    argpar.add_argument('-d', '--database', dest='Database', type=str)
    argpar.add_argument('-g', '--table-g', dest='Table_G', type=str)
    argpar.add_argument('-r', '--table-r', dest='Table_R', type=str)

    file_path = argpar.parse_args().File
    HOST = argpar.parse_args().Host or HOST
    USER = argpar.parse_args().User or USER
    PASSWD = argpar.parse_args().Password or PASSWD
    DATABASE = argpar.parse_args().Database or DATABASE
    TABLE_G = argpar.parse_args().Table_G or TABLE_G
    TABLE_R = argpar.parse_args().Table_R or TABLE_R

    fix_player_id(file_path)

    with open(file_path, mode='r') as fp:
        records = json.load(fp)

        # print(records)

        try:
            game, rounds = parse(records)
        except AssertionError as e:
            print(e)
            build_csv(argpar.parse_args().File)
            exit(1)

        # print(game)
        # print(rounds)

        upload(game, rounds)
