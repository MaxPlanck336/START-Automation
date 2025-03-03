import os
from pyairtable import Api as API
import json
from record import Record
with open('../config.json') as config_file:
    config = json.load(config_file)



api_key = config['airtable-token']

base_id = config['airtable-base-id']
table_id = config['airtable-table-id']

api = API(api_key)
table = api.table(base_id, table_id)

record = Record(
    firstName="Denis",
    surName="Herri",
    gender="Male",
    department="People",
    batch="WS-2024",
    privateEmail="dennis1herri@gmail.com",
    memberTier="Active",
    university="Technical University of Munich",
    studyProgram="Aerospace",
    studyLevel="B.Sc.",
    nationality="Albanian",
    birthDate="2003-11-15",
    paymentStatus="Paid",
    city="Munich",
    linkedinURL="https://www.linkedin.com/in/denis-herri/",
    phoneNumber="+491733940504",
    founder="No",
    careerStatus="Student",
    description="Solving for reality..."
).to_dict()

table.create(record)

records = table.all()
print(json.dumps(records, ensure_ascii=False, indent=4))