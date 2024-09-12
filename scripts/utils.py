import os
import json


def check_raw_data(data):
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


if __name__ == '__main__':
    add_SID(2)
