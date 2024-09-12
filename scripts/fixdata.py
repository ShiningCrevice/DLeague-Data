import json
import pandas as pd


def build_csv(json_file):
    with open(json_file, 'r') as fp:
        data = json.load(fp)

    cnt_r = len(data[0]['Score'])

    df = pd.DataFrame(
        {data[i]['PlayerId']: ["0(S)"] +
         [f"{data[i]['Score'][j+1]-data[i]['Score'][j]} " +
          f"({data[i]['Operations'][j+1]})" for j in range(cnt_r - 1)]
         for i in range(4)})

    df.to_csv('debug.csv')


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
