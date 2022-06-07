# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json

dict_data = {
    'name': '王大明',
    'age': 18,
    'weight': 60
}

str_data = '{ "name": "李大朋", "age": 20, "weight": 70}'


def print_hi(name):
    p = json.loads(str_data)
    print(type(p))
    print(p)

    q = json.dumps(dict_data)
    print(type(q))
    print(eval(q))

    # 輸出 JSON 檔案
    with open("output.json", "w+", encoding='UTF-8') as f:
        json.dump(dict_data, f, indent=4, ensure_ascii=False)

    # 讀取 JSON 檔案
    with open("output.json", "r", encoding='UTF-8') as g:
        h = json.load(g)
        print(type(h))
        print('名字：'+h['name'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
