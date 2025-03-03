import os
from pyairtable import Api as API
import json
with open('../config.json') as config_file:
    config = json.load(config_file)

api_key = config['airtable-token']

base_id = config['airtable-base-id']
table_id = config['airtable-table-id']

api = API(api_key)
table = api.table(base_id, table_id)

record = {
    "First Name": "Denis",
    "Surname": "Herri",
    "Gender": "Male",
    "Department": "People",
    "Batch": "WS-2024",
    "Private Email": "dennis1herri@gmail.com",
    "Member Tier": "Active",
    "University": "Technical University of Munich",
    "Study Program": "Aerospace",
    "Study Level": "B.Sc.",
    "Nationality": "Albanian",
    "Birthdate": "2003-11-15",
    "Payment Status": "Paid",
    "City of Residence": "Munich",
    "LinkedIn": "https://www.linkedin.com/in/denis-herri/",
    
    "Phone": "+491733940504",
    "Founder": "No",
    "Career Status": "Student",
    "Description": "Solving for reality..."
}

def create_table_entry(table, record):
    required_keys = [
        "Name", "Gender", "Department", "Batch", "Private Email", "Member Tier", 
        "University", "Study Program", "Nationality", "Birthday", 
        "Study Level", "Payment Status", "City of Residence", "LinkedIn"
    ]

    if all(key in record for key in required_keys):
        table.create(record)
    else:
        missing_keys = [key for key in required_keys if key not in record]
        print(f"Record is missing the following keys: {', '.join(missing_keys)}")
    
create_table_entry(table, record)

records = table.all()
print(json.dumps(records, ensure_ascii=False, indent=4))