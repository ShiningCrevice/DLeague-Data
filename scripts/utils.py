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
    return True


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
    print(f"Add SID for Season {SID}.")


if __name__ == '__main__':
    add_SID(2)
