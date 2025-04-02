import requests
import os

from api.connect_noco import Record

endpoint_url = "https://start-9kxwqj7z5-maxplanck336s-projects.vercel.app/create_record"

payload = {
    "Name": formData[0],
    "Last_modified": new Date().toISOString(),
    "E_Mail": formData[1],
    "Membership": formData[2],
    "Department": formData[3],
    "Batch": formData[4],
    "City": formData[5],
    "Pronouns": formData[6],
    "Birthday": formData[7],
    "LinkedIn": formData[8],
    "Nationality": formData[9],
    "Study_Program": formData[10],
    "University": formData[11],
    "Study_Level": formData[12],
    "Private_E_Mail": formData[13]
}

response = requests.post(endpoint_url, json=payload, headers={"xc-token": "WLNYNV4V-J6K6h4Jv80oS02AtrBG2IvMnCpuP9OD",
                     "Content-Type": "application/json"})

print(response.status_code)
print(response.json())
print(response.text)