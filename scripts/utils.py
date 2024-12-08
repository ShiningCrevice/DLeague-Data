import os
import json
import pandas as pd
from tabulate import tabulate
from typing import Union
from argparse import ArgumentParser


entries_zh = ['总得点', '素点', '平均顺位', '立直率', '和了率', '放铳率',
              '连对率', '避四率', '立直后和率', '立直后铳率', '平均打点',
              '平均铳点', '一位次数', '二位次数', '三位次数', '四位次数',
              '半庄最高得点']
entries_en = [
    'Total Points', 'Raw Points', 'Average Placement', 'Riichi Rate', 'Winning Rate', 'Deal-In Rate', 'Renchan Rate',
    'Avoiding 4th Place Rate', 'Riichi Win Rate', 'Riichi Deal-In Rate', 'Average Points Per Win',
    'Average Points Lost Per Deal-In', 'First Place Count', 'Second Place Count', 'Third Place Count',
    'Fourth Place Count', 'Highest Hanchan Score']
entries_abbr = ['Pt', 'RawPt', 'AP', 'RR', 'WR', 'DIR', 'RenR', 'A4R',
                'RWR', 'RDIR', 'APW', 'APD', '1st', '2nd', '3rd', '4th', 'HHS']


def build_debug_csv(game):
    json_file = f"raw_data/{game}.json"
    with open(json_file, 'r') as fp:
        data = json.load(fp)

    cnt_r = max([len(data[i]['Score']) for i in range(4)])

    df = pd.DataFrame(
        {data[i]['PlayerId']: ["0(S)"] +
         [f"{data[i]['Score'][j+1]-data[i]['Score'][j]} " +
          f"({data[i]['Operations'][j+1]})" if j+1 < len(data[i]['Score']) and j+1 < len(data[i]['Operations']) else ""
          for j in range(cnt_r - 1)]
         for i in range(4)})

    df.to_csv(f"debug_{game.replace('/', '_')}.csv")
    print(f"Built debug csv for {game}.")


def fix_GT61(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        def update_values(obj):
            flag = False
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if value == "GT61":
                        obj[key] = "0MRS"
                        flag = True
                    else:
                        update_values(value)
            elif isinstance(obj, list):
                for index in range(len(obj)):
                    if obj[index] == "GT61":
                        obj[index] = "0MRS"
                        flag = True
                    else:
                        update_values(obj[index])
            return flag

        if update_values(data):
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print(f"Fixed GT61 to 0MRS in {file_path}")

    except Exception as e:
        print(f"Error occurred while fixing {file_path}:\n{e}")


def check_raw_data(data: list[dict]) -> tuple[bool, str]:
    """Check if the raw data of a game is legal.

    Args:
        data (list[dict]): a list of 4 player's data in order.

    Returns:
        (legal, massage) (tuple[bool, str]): `legal` is `True` if the data is legal, otherwise False.
        `massage` is the reason why the data is illegal. If `legal` is `True`, `massage` is an empty string.
    """
    if len(data) != 4:
        return False, f"Data amount should be 4, but got {len(data)}."
    sid = set([data[i]['SID'] for i in range(4)])
    if len(sid) != 1:
        return False, f"Inconsistent SIDs: {sid}."
    gid = set([data[i]['GID'] for i in range(4)])
    if len(gid) != 1:
        return False, f"Inconsistent GIDs: {gid}."
    scores = [data[i]['Score'] for i in range(4)]
    n_scores = set([len(s) for s in scores])
    if len(n_scores) != 1:
        return False, f"Inconsistent numbers of rounds in scores: {n_scores}."
    final_sum = sum([s[-1] for s in scores])
    if final_sum != 100000:
        return False, f"Sum of scores should be 100000, but got {final_sum}."
    operations = [data[i]['Operations'] for i in range(4)]
    n_operations = set([len(op) for op in operations])
    if len(n_operations) != 1:
        return False, f"Inconsistent numbers of rounds in operations: {n_operations}."
    if n_scores != n_operations:
        return False, f"Inconsistent numbers of rounds between scores({n_scores}) and operations({n_operations})."
    n = len(scores[0])
    for k in range(1, n):
        agari = sum([1 for i in range(4) if 'A' in operations[i][k]])
        if agari > 1:
            return False, f"More than one player claimed agari in round {k}."
        hoju = sum([1 for i in range(4) if 'F' in operations[i][k]])
        if hoju > 1:
            return False, f"More than one player claimed hoju in round {k}."
        for i in range(4):
            if 'A' in operations[i][k] and scores[i][k] <= scores[i][k-1]:
                return False, f"Player {i} claimed agari but score decreased in round {k}."
            if 'F' in operations[i][k] and scores[i][k] >= scores[i][k-1]:
                return False, f"Player {i} claimed hoju but score increased in round {k}."
    return True, ""


def int2bin(n: int) -> str:
    return bin(n)[2:].zfill(4)


def add_SID(SID: int):
    dir = f"../raw_data/S{SID}"
    files = sorted(os.listdir(dir), key=lambda x: int(x[1:-5]))
    for f in files:
        with open(os.path.join(dir, f)) as file:
            data = json.load(file)
        for i in range(4):
            data[i]['SID'] = SID
        with open(os.path.join(dir, f), 'w') as file:
            json.dump(data, file)
    print(f"Added SID for Season {SID}.")


def generate_abbr_reference():
    table = {}
    table['Abbreviation'] = entries_abbr
    table['English'] = entries_en
    table['Chinese'] = entries_zh
    with open('docs/abbr_reference.md', 'w', encoding='utf-8') as f:
        f.write(f"# Abbreviations\n\n{tabulate(table, headers='keys', tablefmt='github')}\n")


def is_raw_data_piece(data: Union[dict, str]) -> bool:
    """Checks if the given dictionary represents a valid raw data piece.

    Args:
        data (dict): The dictionary to check.

    Returns:
        bool: True if the dictionary is a valid raw data piece, False otherwise.

    Examples:
        >>> is_raw_data_piece({
        ...     'SID': 123,
        ...     'GID': 456,
        ...     'Time': '2023-10-01T12:00:00Z',
        ...     'PlayerId': 'ABCD',
        ...     'Score': [10, 20],
        ...     'Operations': ['op1', 'op2']
        ... })
        True

        >>> is_raw_data_piece({
        ...     'SID': '123',
        ...     'GID': 456,
        ...     'Time': '2023-10-01T12:00:00Z',
        ...     'PlayerId': 'ABCD',
        ...     'Score': [10, 20],
        ...     'Operations': ['op1', 'op2']
        ... })
        False
    """
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            return False
    if not isinstance(data, dict):
        return False
    if not ('SID' in data and isinstance(data['SID'], int)):
        return False
    if not ('GID' in data and isinstance(data['GID'], int)):
        return False
    if not ('Time' in data and isinstance(data['Time'], str)):
        return False
    if not ('PlayerId' in data and isinstance(data['PlayerId'], str)
            and len(data['PlayerId'])) == 4:
        return False
    if not ('Score' in data and isinstance(data['Score'], list)
            and len(data['Score']) > 0 and isinstance(data['Score'][0], int)):
        return False
    if not ('Operations' in data and isinstance(data['Operations'], list)
            and len(data['Operations']) > 0 and isinstance(data['Operations'][0], str)):
        return False
    return True


def get_newest_game():
    newest_sid = 0
    newest_gid = 0
    for sid in range(1, 10):
        dir = f"raw_data/S{sid}"
        if not os.path.exists(dir):
            continue
        files = sorted(os.listdir(dir), key=lambda x: int(x[1:-5]))
        for f in files:
            gid = int(f[1:-5])
            if gid > newest_gid:
                newest_sid = sid
                newest_gid = gid
    return f"S{newest_sid}/G{newest_gid}"


if __name__ == '__main__':
    if os.getcwd().split('/')[-1] == 'scripts' or os.getcwd().split('\\')[-1] == 'scripts':
        os.chdir('..')

    arg_parser = ArgumentParser()
    arg_parser.add_argument('--game', '-g', type=str, help='The game to build csv.', default=None)
    arg_parser.add_argument('--abbr', '-a', action='store_true', help='Generate abbreviation reference.', default=False)
    args = arg_parser.parse_args()

    if args.game:
        build_debug_csv(args.game)
    elif args.abbr:
        generate_abbr_reference()
    else:
        build_debug_csv(get_newest_game())
