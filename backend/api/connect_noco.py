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


class Record(BaseModel):
    Name: str
    Last_modified: str
    E_Mail: str
    Membership: str
    Department: str
    Batch: str
    City: str
    Pronouns: str
    Birthday: str
    LinkedIn: str
    Nationality: str
    Study_Program: str
    University: str
    Study_Level: str
    Private_E_Mail: str

# Sample JSON data
sample_record_json = {
    "Name": "John Doe",
    "Last_modified": "2023-10-01 15:45:00+00:00",
    "E_Mail": "john.doe@startmunich.de",
    "Membership": "Active",
    "Department": "Marketing",
    "Batch": "WS23",
    "City": "Munich",
    "Pronouns": "they/them",
    "Birthday": "1998-07-20",
    "LinkedIn": "https://www.linkedin.com/in/johndoe/",
    "Nationality": "American",
    "Study_Program": "Business Administration",
    "University": "Ludwig Maximilian University of Munich",
    "Study_Level": "Master",
    "Private_E_Mail": "john.doe@example.com"
}

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
def create_record(record: Record = Body(...)):
    api_call = f"{server}/api/v2/tables/{table_id}/records"
    response = requests.post(
        api_call,
        headers={'xc-token': xc_token},
        json=record.dict()
    )
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))
    return response.json()

# sample_record = Record(**{
#     "Name": "tester 1",
#     "Last_modified": "2024-06-17 12:32:00+00:00",
#     "E_Mail": "sample_user@startmunich.de",
#     "Membership": "Active",
#     "Department": "Finance & Operations",
#     "Batch": "SS24",
#     "City": "Munich",
#     "Pronouns": "he/him",
#     "Birthday": "2003-11-15",
#     "LinkedIn": "https://www.linkedin.com/in/sample_user/",
#     "Nationality": "German",
#     "Study_Program": "Computer Science",
#     "University": "Technical University of Munich",
#     "Study_Level": "Bachelor",
#     "Private_E_Mail": "sample_user@personal.com"
# })