Use Case - Melody is a music streaming app.This app generates a large amount of  data due to it's ever increasing user and song base.The data is majorly associated with the user activities such as what songs are played by user at what time.Is the user a free or a paid member etc.Melody wants us to leverage this data and build a datawarehouse from which the company's analytical team can derive useful buisness insights. The data is available in the form of JSON files in S3


For the above use case I will create a ETL pipeline which will extract data from S3 and stages it on AWS Redshift.By leveraging SQL facts and dimension tables will be created.I will then create a STAR SCHEMA datawarehouse consists of the fact and dimension tables.


Python scripts used - 

sql_queries.py - This python files consists of all sql queries required.The subsequent scipts will import from this file the queries relevant to them .

dwh.cfg - It contains all the necessary credentials and configuraion .

create_cluster.ipynb - It is jupyter notebook which will create the redshift cluster.

create_tables.py - This scripts will create the staging,fact and dimension tables in redshift .

etl.py - It will extract the data from S3 and load in into staging tables . The data in staging will be transformed loaded into facts and dimension tables .


Tables - 

Staging tables - staging_songs,staging_events 

Fact table  - songplays table

Dimension tables - users,songs,artists,time 
