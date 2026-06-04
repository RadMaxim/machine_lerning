import sqlalchemy
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, UniqueConstraint, Float, inspect


def create_table(db_conn: sqlalchemy.engine.base.Engine) -> None:
    metadata = MetaData()
    salaries_table = Table(
        'users_churn',  # замените на имя вашей таблицы
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('customer_id', String),
        Column('begin_date', DateTime),
        Column('end_date', DateTime),
        Column('type', String),
        Column('paperless_billing', String),
        Column('payment_method', String),
        Column('monthly_charges', Float),
        Column('total_charges', Float),
        Column('internet_service', String),
        Column('online_security', String),
        Column('online_backup', String),
        Column('device_protection', String),
        Column('tech_support', String),
        Column('streaming_tv', String),
        Column('streaming_movies', String),
        Column('gender', String),
        Column('senior_citizen', Integer),
        Column('partner', String),
        Column('dependents', String),
        Column('multiple_lines', String),
        Column('target', Integer),
        UniqueConstraint('customer_id', name='unique_employee_constraint')

    )
    if not inspect(db_conn).has_table(salaries_table.name):
        metadata.create_all(db_conn)

        # Добавьте primary_key и другие ограничения, если нужно

    # ваш код здесь тоже #
