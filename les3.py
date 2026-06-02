import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task


@task()
def extract() -> pd.DataFrame:
    hook = PostgresHook('source_db')
    conn = hook.get_conn()
    sql_query = f"""
        select
            c.customer_id, c.begin_date, c.end_date, c.type, c.paperless_billing, c.payment_method, c.monthly_charges, c.total_charges,
            i.internet_service, i.online_security, i.online_backup, i.device_protection, i.tech_support, i.streaming_tv, i.streaming_movies,
            p.gender, p.senior_citizen, p.partner, p.dependents,
            ph.multiple_lines
        from contracts as c
        left join internet as i on i.customer_id = c.customer_id
        left join personal as p on p.customer_id = c.customer_id
        left join phone as ph on ph.customer_id = c.customer_id
    """
    data = pd.read_sql(sql_query, conn)

    conn.close()

    return data