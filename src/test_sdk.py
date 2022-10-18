def enc_sql(query):
    sql = query['sql']
    if "show" in sql:
        return sql+";---hiahia---"