import configparser 

config = configparser.ConfigParser()
config.read_file(open('dwh.cfg'))

print(config['S3'])