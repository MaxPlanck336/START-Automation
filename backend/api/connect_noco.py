import requests
import json
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()

# Load environment variables from .env file
load_dotenv()
# Load environment variables

xc_token = os.getenv("xc_token") # NocoDB Tokne - Denis Herri
server = os.getenv("server") # START Munich DB Server
table_id = os.getenv("table_id") # Members Table ID

class Data(BaseModel):
    text: str

@app.get("/get_records")
# Read all records from a table.
async def get_all_records():
    api_call = f"{server}/api/v2/tables/{table_id}/records"
    response = requests.get(
        api_call,
        headers={'xc-token': xc_token}
    )
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))
    return response.json()

@app.post("/create_record")
# Create a new record in a table.
def create_record(data: Data = Body(...)):
    entries = data['data'].split(';')
    
    def rearrange_date(date_str):
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        month_num = month_map[[date_str][4:7]]
        day = date_str[9:11]
        year = date_str[12:16]
        time = date_str[17:25]
        return f"{year}-{month_num}-{day} {time}+00:00"

    fields = ["Name", "Last modified", "E-Mail", "Membership", "Department", "Batch", "City", "Pronouns", "Birthday", "LinkedIn", "Nationality", "Study Program", "University", "Study Level", "Private E-Mail"]
    
    entries_formatted = [""] * len(fields)
    entries_formatted[0] = entries[0]
    entries_formatted[1] = rearrange_date(entries[1])
    entries_formatted[2] = entries[2]
    entries_formatted[3] = entries[3]
    entries_formatted[4] = entries[4]
    entries_formatted[5] = entries[5][1:]
    entries_formatted[6] = "SS" if entries[6] == "Summersemester" else "WS" if entries[6] == "Wintersemester" else entries[6] + entries[7]
    entries_formatted[7] = entries[8]
    entries_formatted[8] = entries[9]
    entries_formatted[9] = rearrange_date(entries[11])
    entries_formatted[10] = entries[12]
    entries_formatted[11] = entries[13]
    entries_formatted[12] = entries[14]
    entries_formatted[13] = entries[15]
    entries_formatted[14] = entries[16]
    entries_formatted[15] = entries[17]

    api_call = f"{server}/api/v2/tables/{table_id}/records"
    print(data)
    response = requests.post(
        api_call,
        headers={'xc-token': xc_token},
        json=entries_formatted.dict()
    )
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))
    return response.json()