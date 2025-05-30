# Day 24 - Hospital System using OOP

# define patient class
class Patient:
    def __init__(self, name, age, disease):  # constructor for patient
        self.name = name
        self.age = age
        self.disease = disease
        self.diagnosis = 'Pending'

    def update_diagnosis(self, new_diagnosis):  # update diagnosis
        self.diagnosis = new_diagnosis

    def show_details(self):  # display patient info
        print(f'{self.name} | Age: {self.age} | Disease: {self.disease} | Diagnosis: {self.diagnosis}')

# define hospital class
class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):  # admit new patient
        self.patients.append(patient)
        print(f'Patient {patient.name} admitted.')

    def show_all_patients(self):  # show all patients
        if not self.patients:
            print('No patients found.')
        for patient in self.patients:
            patient.show_details()

    def update_diagnosis(self, name, diagnosis):  # update a patient diagnosis
        for patient in self.patients:
            if patient.name == name:
                patient.update_diagnosis(diagnosis)
                print(f'Diagnosis updated for {name}')
                return
        print('Patient not found.')

    def discharge_patient(self, name):  # remove a patient
        for patient in self.patients:
            if patient.name == name:
                self.patients.remove(patient)
                print(f'Patient {name} discharged.')
                return
        print('Patient not found.')

# sample usage
p1 = Patient("Ali", 30, "Fever")
p2 = Patient("Usman", 45, "Cough")

h = Hospital()
h.add_patient(p1)
h.add_patient(p2)
h.show_all_patients()
h.update_diagnosis("Ali", "Viral Fever")
h.discharge_patient("Usman")
h.show_all_patients()
