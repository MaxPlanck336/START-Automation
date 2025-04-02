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
    api_call = f"{server}/api/v2/tables/{table_id}/records"
    print(data)
    response = requests.post(
        api_call,
        headers={'xc-token': xc_token},
        json=data.dict()
    )
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))
    return response.json()