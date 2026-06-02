from airflow.decorators import dag
import pendulum

@dag(
    schedule='@weekly', # Ровно в 09:00 каждый вторник (2 — это вторник в Cron)
    start_date=pendulum.datetime(2023, 12, 19,9,0, tz="UTC"), # С недели от 18 декабря 2023 года
    tags=["new_product"] # Тег для фильтрации
)
def build_new_product_report():
    # код DAG #
    pass
