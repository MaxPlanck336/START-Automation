from notion_client import Client
import csv
from omegaconf import OmegaConf

try:
    conf = OmegaConf.load("Synchronization/config.yaml")
except FileNotFoundError:
    print("Error: Configuration file not found.")
    exit(1)

def extract_text(property_item):
    """Extracts plain text from a Notion property item."""
    if "title" in property_item:
        return " ".join([t["text"]["content"] for t in property_item["title"] if "text" in t])
    if "rich_text" in property_item:
        return " ".join([t["text"]["content"] for t in property_item["rich_text"] if "text" in t])
    if "date" in property_item:
        return property_item["date"]["start"] if property_item["date"] else ""
    if "select" in property_item:
        return property_item["select"]["name"] if property_item["select"] else ""
    if "multi_select" in property_item:
        return ", ".join([t["name"] for t in property_item["multi_select"]])
    return ""

def write_to_csv(content, file_name="Synchronization/Notion/database_info.csv"):
    if not content.get("results"):
        print("No data to write.")
        return
    
    # Extract column names dynamically
    keys = set()
    for item in content["results"]:
        keys.update(item["properties"].keys())
    
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=sorted(keys))
        writer.writeheader()
        
        for item in content["results"]:
            row = {key: extract_text(item["properties"].get(key, {})) for key in keys}
            writer.writerow(row)

def read_db(client, database_id):
    response = client.databases.query(database_id=database_id)
    return response

def main():
    client = Client(auth=conf.notion.token)
    database_info = read_db(client, conf.notion.database_id)
    write_to_csv(database_info)
    print("Database info has been written to database_info.csv")

if __name__ == "__main__":
    main()
