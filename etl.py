import configparser
import psycopg2
from sql_queries import copy_table_queries,insert_table_queries


def load_staging_tables(curr,conn):
    for query in copy_table_queries:
        curr.execute(query)
        conn.commit()

def insert_tables(curr,conn):
    for query in insert_table_queries:
        curr.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('Connection established')
    curr = conn.cursor()
    print('Cursor created')
    load_staging_tables(curr, conn)
    print('Staging tables created')
    insert_tables(curr,conn)
    print('Data inserted into the tables')
    conn.close()
    print('Connection closed') 

if __name__ == '__main__':
    main()
    