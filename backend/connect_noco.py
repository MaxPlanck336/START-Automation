import requests
import json

xc_token = 'WLNYNV4V-J6K6h4Jv80oS02AtrBG2IvMnCpuP9OD' # NocoDB Tokne - Denis Herri
server = "https://ndb.startmunich.de" # START Munich DB Server
table_id = "muyzu5ovo0jdiks" # Members Table ID


# Read all records from a table.
def get_all_records(table_id, server, token):
    api_call = f"{server}/api/v2/tables/{table_id}/records"
    response = requests.get(
        api_call,
        headers={'xc-token': token}
    )
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))
    return response.json()

def create_record(table_id, server, token, data):
    api_call = f"{server}/api/v2/tables/{table_id}/records"
    response = requests.post(
        api_call,
        headers={'xc-token': token},
        json=data
    )
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))
    return response.json()

# sample_data = {
#     "Name": "Sample User",
#     "Last modified": "2024-06-17 12:32:00+00:00",
#     "E-Mail": "sample_user@startmunich.de",
#     "Membership": "Active",
#     "Department": "Finance & Operations",
#     "Batch": "SS24",
#     "City": "Munich",
#     "Pronouns": "he/him",
#     "Birthday": "2003-11-15",
#     "LinkedIn": "https://www.linkedin.com/in/sample_user/",
#     "Nationality": "German",
#     "Study Program": "Computer Science",
#     "University": "Technical University of Munich",
#     "Study Level": "Bachelor",
#     "Private E-Mail": "sample_user@personal.com"
# }

# get_all_records(table_id, server, xc_token)
# create_record(table_id, server, xc_token, sample_data)