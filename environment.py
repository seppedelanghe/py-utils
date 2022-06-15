import os, logging

def read_dotenv(path: str = '.env'):
    with open(path, 'r') as env_file:
        for line in env_file.readlines():
            try:
                line = line.replace('\n', '')
                key, value = line.split('=')
                os.environ[key] = value
            except Exception as e:
                logging.error(f"Failed to read env file line. Line: {line}.\n" + str(e))
                continue