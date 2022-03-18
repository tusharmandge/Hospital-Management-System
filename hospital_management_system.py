class Patient:
    symptoms=[]
    bills=[]
    def __init__(self, id, name, gender, age):
        self.patients_name = name
        self.patients_gender = gender
        self.patients_id = id
        self.patients_age = age

    def getpatientsid(self):
        return self.patients_id

    def getpatientsname(self):
        return self.patients_name

    def getpatientsgender(self):
        return self.patients_gender

    def getpatientsage(self):
        return self.patients_age

    def getpatientssymptoms(self):
        return self.symptoms

    def getpatientsbill(self):
        return self.bills

class symptoms:

    def __init__(self,id,symptoms_list,date):
        self.symptoms_id=id
        self.patients_symptoms_list=symptoms_list
        self.date=date
    def getsymptomssid(self):
        return self.symptoms_id 
    def getpatientssymptomslist(self):
        return self.patients_symptoms_list  
    def getdate(self):
        return self.date

class bill:
    def __init__(self,id,bills_list,date):
        self.bills_id=id
        self.patients_bills_list=bills_list
    def getpatientsbillsid(self):
        return self.bills_id     
    def getpatientsbillslist(self):
        return self.patients_bills_list  

patients_list = []
def true():
        
    while True:
        print("What you want you to do?\t")
        print("1.Add patients data\t")
        print("2.Show all patientss\t")
        print("3.Search patients\t")
        print("4.Delete patientss data by patients id\t")
        print("5.Edit patients data by patients id\t")
        print("6.Show patients bills by patient id")
        print("7.add patients symptoms by id")
        print("8.show patients symptoms by patient id")

        user_input = input("Enter your Choice")

        if user_input == "1":
            patients_id = len(patients_list) + 1
            patients_name = input("Enter patients name")
            patients_gender = input("Enter patients gender")
            patients_age = input("Enter patients age")
            _patient = Patient(
                patients_id,
                patients_name,
                patients_gender,
                patients_age
            )
            patients_list.append(_patient)

        elif user_input == "2":
            for patient in patients_list:
                print("Patient Id:", patient.getpatientsid())
                print("Name:", patient.getpatientsname())
                print("Gender:", patient.getpatientsgender())
                print("Age", patient.getpatientsage())
                print("Symptoms", patient.getpatientssymptoms())

        elif user_input == "3":
            show_patiets_data = int(input("Enter Patient id"))
            for patient in patients_list:
                if show_patiets_data == patient.getpatientsid():
                    print("Patient Id:", patient.getpatientsid())
                    print("Name:", patient.getpatientsname())
                    print("Gender:", patient.getpatientsgender())
                    print("Age", patient.getpatientsage())
                    print("Symptoms", patient.getpatientssymptoms())
                    print("Bill", patient.getpatietsbill())

        elif user_input == "4":
            remove_patients_data = int(input("Enter patients id"))
            for patient in patients_list:
                if remove_patients_data == patient.getpatientsid():
                    patients_list.remove[patient]

        elif user_input == "5":
            counter = 0
            edit_patients_data = int(input("Enter Patients id to Edit"))
            for i in patients_list:
                if edit_patients_data == i.getpatientsid():
                    patients_id = len(patients_list) + 1
                    patients_name = input("Enter patients name")
                    patients_gender = input("Enter patients gender")
                    patients_age = input("Enter patients age")
                    patients_symptoms = input("Enter patients symptoms\t Mild/Hard")
                    patients_bill = input("Enter estimated bill")
                    _patient = Patient(
                        patients_id,
                        patients_name,
                        patients_gender,
                        patients_age,
                        patients_symptoms,
                        patients_bill,
                    )
                    patients_list[counter] = _patient
                    counter = counter + 1
        elif user_input == "6":
            show_patients_bill = int(input("Enter patient Id to view bill"))
            for i in patients_list:
                if show_patients_bill == i.getpatientsid():
                    for bills in i.getpatientsbill():
                        print(bills.getpatientsbillsid())
                        print(bills.getpatientsbillslist())             

        elif user_input=="7":
            access_patient=int(input("Enter patient id"))
            for patient in patients_list:
                if access_patient==patient.getpatientsid():
                    add_patients_symptoms=input("Enter Symptoms")
                    date=input("Enter date")
                    _symptoms=symptoms(str(patient.patients_id) + "_"+str(len(patient.symptoms)),add_patients_symptoms,date )
                    add_patients_bills=input("Add patients bill by symptoms")
                    patient.symptoms.append(_symptoms)
                    _bills=bill(str(patient.patients_id)+"_"+str(len(patient.bills)),add_patients_bills,date)
                    patient.bills.append(_bills)
        elif user_input=="8":
            show_patiets_symptoms=int(input("Enter Patients ID"))
            for i in patients_list:
                if show_patiets_symptoms==i.getpatientsid():
                    for symptom in i.getpatientssymptoms():
                        print(symptom.getsymptomssid())
                        print(symptom.getpatientssymptomslist())
                        print(symptom.getdate())
        else:
            break
