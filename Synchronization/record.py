class Record:
    def __init__(self, firstName, surName, gender, department, batch, privateEmail, memberTier, university, studyProgram, studyLevel, nationality, birthDate, paymentStatus, city, linkedinURL, phoneNumber=None, founder=None, careerStatus=None, description=None):
        self.firstName = firstName
        self.surName = surName
        self.gender = gender
        self.department = department
        self.batch = batch
        self.privateEmail = privateEmail
        self.memberTier = memberTier
        self.university = university
        self.studyProgram = studyProgram
        self.studyLevel = studyLevel
        self.nationality = nationality
        self.birthDate = birthDate
        self.paymentStatus = paymentStatus
        self.city = city
        self.linkedinURL = linkedinURL
        self.phoneNumber = phoneNumber
        self.founder = founder
        self.careerStatus = careerStatus
        self.description = description

    def to_dict(self):
        return {
            'First Name': self.firstName,
            'Surname': self.surName,
            'Gender': self.gender,
            'Department': self.department,
            'Batch': self.batch,
            'Private Email': self.privateEmail,
            'Member Tier': self.memberTier,
            'University': self.university,
            'Study Program': self.studyProgram,
            'Study Level': self.studyLevel,
            'Nationality': self.nationality,
            'Birthdate': self.birthDate,
            'Payment Status': self.paymentStatus,
            'City': self.city,
            'LinkedIn': self.linkedinURL,
            'Phone Number': self.phoneNumber,
            'Founder': self.founder,
            'Career Status': self.careerStatus,
            'Description': self.description
        }
    