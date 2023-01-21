import configparser 
import psycopg2 
from sql_queries import create_table_queries 


def create_table(curr,conn):
    for query in create_table_queries:
        curr.execute(query)
        conn.commit()

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    print(config)
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('Connection established')
    curr = conn.cursor()
    print('Cursor created')
    print('Creating tables')
    create_table(curr, conn)
    print('Tables created')
    conn.close()
    print('Connection closed')



if __name__ == '__main__':
    main()
    
