import pandas as pd
from sqlalchemy import create_engine

# замените пользователя, пароль, хост, порт и имя базы данных на реальные учётные данные общей базы данных
conn = create_engine('postgresql://mle_ro:HI&ykgu6tj@rc1b-uh7kdmcx67eomesf.mdb.yandexcloud.net:6432/playground_common')


# определяем функцию получения данных из первичного источника
# она получает на вход объект соединения к первичному источнику
# и возвращает данные из всех таблиц, собранные в одном pandas.DataFrame
def extract(cnx) -> pd.DataFrame:
    # Использованы тройные кавычки для корректной работы многострочного SQL-запроса
    sql_query = """
    SELECT 
        c.*,
        i.internet_service,
        i.online_security,
        i.online_backup,
        i.device_protection,
        i.tech_support,
        i.streaming_tv,
        i.streaming_movies,
        p.gender,
        p.senior_citizen,
        p.partner,
        p.dependents,
        ph.multiple_lines
    FROM contracts AS c
    LEFT JOIN internet AS i ON c.customer_id = i.customer_id
    LEFT JOIN personal AS p ON c.customer_id = p.customer_id
    LEFT JOIN phone AS ph ON c.customer_id = ph.customer_id;
    """

    # Исполняем написанный запрос
    data = pd.read_sql(sql_query, cnx)

    # Гарантированно удаляем колонку 'index', если она попала в DataFrame (выполнение шага №3)
    if 'index' in data.columns:
        data = data.drop(columns=['index'])
        print(data)

    return data


import pandas as pd
import numpy as np
import sqlalchemy

def transform(data: pd.DataFrame) -> pd.DataFrame:
    # Делаем копию, чтобы не изменять исходный датасет напрямую
    transformed_data = data.copy()
    transformed_data['end_date'] = transformed_data['end_date'].replace('No', None)
    transformed_data['target'] = np.where(transformed_data['end_date'].notna(), 1, 0)

    return transformed_data


