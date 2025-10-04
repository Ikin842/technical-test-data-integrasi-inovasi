import json
import hashlib

def generate_id(data: dict):
    json_data = json.dumps(data, sort_keys=True)
    md5_hash = hashlib.md5(json_data.encode('utf-8')).hexdigest()
    return md5_hash

def load_query(filename, query_name):
    with open(filename, "r") as f:
        sql_file = f.read()
    queries = sql_file.split(";")
    for q in queries:
        if f"-- name: {query_name}" in q:
            return q.strip()
    raise ValueError(f"Query {query_name} not found in {filename}")