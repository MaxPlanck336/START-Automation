from notion_client import Client
import json
from omegaconf import OmegaConf

try:
    conf = OmegaConf.load("Synchronization/config.yaml")
except FileNotFoundError:
    print("Error: Configuration file not found.")
    exit(1)

def write_to_json(content, file_name="Synchronization/Notion/database_info.json"):
    content_as_json_str = json.dumps(content, indent=4)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)

def read_db(client, database_id):
    response = client.databases.query(database_id=database_id)
    return response

def main():
    client = Client(auth=conf.notion.token)
    database_info = read_db(client, conf.notion.database_id)
    write_to_json(database_info)
    print("Database info has been written to database_info.json")

if __name__ == "__main__":
    main()
