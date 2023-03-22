import pandas
from parser import parse


# ссылка на страницу
URL = "https://www.lamoda.ru/c/3039/clothes-topyi-muzhskie/"
# количество товаров в категории
ITEMS = 350
# название Excel файла, который будет сформирован
FILENAME = './data.xlsx'


if __name__ == '__main__':
    data = parse(URL, ITEMS)
    df = pandas.DataFrame(data)
    df.to_excel(FILENAME, index=False)
