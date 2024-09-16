import os
import json


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


if __name__ == '__main__':
    add_SID(2)
