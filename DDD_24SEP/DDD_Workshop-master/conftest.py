from pytest import fixture
from utilities.excel_utils import get_excel_data
from utilities.excel_utils import excel_header
from utilities.sql_utils import get_sql_data
from utilities.sql_utils import sql_header
from selenium import webdriver

Excel_file = 'data/DDD_InputFile.xlsx'
SQL_query = 'select * from test_data;'

def excel_data_source(criteria):
    data = (get_excel_data(Excel_file)
            .query(criteria)) \
        .where(get_excel_data(Excel_file).notnull(), "") \
        .values \
        .tolist()
    return data

#el approach de SQL hace parte del homework

# def sql_data_source(criteria):
#     data = (get_sql_data(SQL_query)
#             .query(criteria)) \
#         .where(get_sql_data(SQL_query).notnull(), "") \
#         .values \
#         .tolist()
#     return data

@fixture(scope="function")
def header(approach):
    if approach == "1":
        return excel_header(Excel_file)
# el approach de SQL hace parte del homework
    # elif approach == "2":
    #     return sql_header(SQL_query)

@fixture(params=[webdriver.Firefox], scope="session")
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


#*********************************************************************
#4. Filtrar datos
#Pista:
# 1 = Columna que contiene el valor para filtrar los datos del excel
# 2 = Critero de busqueda en los valores de dicha columna
# encuentre un patron que le permita obtener todos los test que
# prueban los mensajes generados por registros invalidos
#**********************************************************************

@fixture(params=excel_data_source('1.str.contains("2")'))
def data_signup_excel(request):
    data = request.param
    return data

# el approach de SQL hace parte del homework
# @fixture(params=sql_data_source('1.str.contains("2")'))
# def data_signup_sql(request):
#     data = request.param
#     return data





