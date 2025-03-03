from Synchronization import record
import csv
from Synchronization.record import Record
from datetime import datetime

class NotionParser:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def parse(self):
        records = []
        with open(self.csv_file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = self._convert_row_to_record(row)
                records.append(record)
        return records

    def _convert_row_to_record(self, row):
        return Record(
            firstName=row['firstName'],
            surName=row['surName'],
            gender=row['gender'],
            department=row['department'],
            batch=row['batch'],
            privateEmail=row['privateEmail'],
            memberTier=row['memberTier'],
            university=row['university'],
            studyProgram=row['studyProgram'],
            studyLevel=row['studyLevel'],
            nationality=row['nationality'],
            birthDate=self._parse_date(row['birthDate']),
            paymentStatus=row['paymentStatus'],
            city=row['city'],
            linkedinURL=row['linkedinURL'],
            phoneNumber=row.get('phoneNumber'),
            founder=row.get('founder'),
            careerStatus=row.get('careerStatus'),
            description=row.get('description')
        )

if __name__ == "__main__":
    parser = NotionParser("Synchronization/Notion/Members — Global DB cff2c0dd913c423a9b47f257d0de94b8_all.csv")
    records = parser.parse()
    for record in records:
        print(record.to_dict())