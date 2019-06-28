from google.cloud import bigquery
from configparser import ConfigParser


parser =  ConfigParser()
parser.read('config.ini')
json_key=parser.get('default', 'url')

def search_query(title,text):

    client = bigquery.Client.from_service_account_json(json_key)

    value = {}

    # Perform a query.
    QUERY = (
        'SELECT * FROM `bigquery-public-data.hacker_news.stories` WHERE title = @title AND text = @text')
    query_params = [
        bigquery.ScalarQueryParameter("title", "STRING",title),
        bigquery.ScalarQueryParameter("text", "STRING", text),
    ]
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = query_params
    query_job = client.query(
        QUERY,
        job_config=job_config,
    )
    for row in query_job:
        print(row.title)
        value = {"articles": {"title": row.title, "URL": row.url, "text": row.text, "date": row.time_ts}}

    assert query_job.state == "DONE"

    return value