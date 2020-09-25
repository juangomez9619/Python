import pandas as pd

pd.set_option('display.max_colwidth', -1)


def get_excel_data(fileName):
    rows = pd.read_excel(fileName)
    return rows

def excel_header(fileName):
    data = get_excel_data(fileName)
    header_list = data.columns.tolist()
    header_map = {}
    count = 0
    for column in header_list:
        header_map[column] = count
        count += 1
    return header_map
