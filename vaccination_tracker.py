""""
OOP1 Assignment - Vaccination Tracker
PROG211: Object-Oriented Programming 1

Real-world domain: Health
Digital Public Goods (DPG) focus:
- Open-source
- Inclusive and accessible
- Privacy-respecting
- Modular and reusable
"""

class Patient:
    """Represents a patient using a non-sensitive identifier."""

    total_patients = 0

    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.vaccinations = []
        Patient.total_patients += 1

    # Instance method
        """Add a vaccination record to this patient."""
        record = {
            "vaccine": "vaccine_name",
            "dose": "dose_number"
        }
        self.vaccinations.append(record)

    # Instance method
    def display_info(self):
        """Display the patient's basic vaccination information."""
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

        if self.vaccinations:
            print("Vaccinations:")
            for record in self.vaccinations:
                print(f"  - {record['vaccine']} (Dose {record['dose']})")
        else:
            print("Vaccinations: None")

    # Class method
    @classmethod
    def get_total_patients(cls):
        """Return the number of Patient objects created."""
        return cls.total_patients

    # Static method
    @staticmethod
    def is_valid_age(age):
        """Check whether an age is within a reasonable range."""
        return isinstance(age, int) and 0 <= age <= 120


class VaccinationCenter:
    """Represents a vaccination center."""

    def __init__(self, center_name, location):
        self.center_name = center_name
        self.location = location
        self.patients = []

    # Instance method
    def register_patient(self, patient):
        """Register a Patient object at this center."""
        self.patients.append(patient)

    # Instance method
    def display_patients(self):
        """Display all registered patients."""
        print(f"\nVaccination Center: {self.center_name}")
        print(f"Location: {self.location}")
        print("-" * 40)

        if not self.patients:
            print("No patients registered.")
            return

        for patient in self.patients:
            patient.display_info()
            print("-" * 40)

    # Class method
    @classmethod
    def from_default_location(cls, center_name):
        """Create a center using a default location."""
        return cls(center_name, "Freetown, Sierra Leone")

    # Static method
    @staticmethod
    def count_vaccinated(patients):
        """Count patients who have at least one vaccination."""
        return sum(1 for patient in patients if patient.vaccinations)


# Task 2: One data structure - a list of Patient objects.
def add_patient(patient_list, patient):
    """Add a Patient object to the list."""
    patient_list.append(patient)


def display_records(patient_list):
    """Display records stored in the list."""
    print("\nALL PATIENT RECORDS")
    print("=" * 40)

    for patient in patient_list:
        patient.display_info()
        print("-" * 40)


# -------------------------
# Example program execution
# -------------------------
if __name__ == "__main__":
    # Validate ages before creating objects.
    if not Patient.is_valid_age(25):
        raise ValueError("Invalid age.")

    patient1 = Patient("P001", "Mariama", 25)
    patient2 = Patient("P002", "Mohamed", 8)
    patient3 = Patient("P003", "Fatmata", 31)

    # Interaction between objects and methods.
    patient1.add_vaccination("COVID-19", 1)
    patient1.add_vaccination("COVID-19", 2)

    patient2.add_vaccination("Measles", 1)
    patient2.add_vaccination("Polio", 1)

    patient3.add_vaccination("Tetanus", 1)

    # One list data structure storing multiple Patient objects.
    patients = []
    add_patient(patients, patient1)
    add_patient(patients, patient2)
    add_patient(patients, patient3)

    # Class method example.
    print("Total Patient Objects:", Patient.get_total_patients())

    # Create a vaccination center using a class method.
    center = VaccinationCenter.from_default_location("Central Vaccination Center")

    for patient in patients:
        center.register_patient(patient)

    center.display_patients()

    # Function using the list data structure.
    display_records(patients)

    # Static method example.
    vaccinated = VaccinationCenter.count_vaccinated(patients)
    print("Patients with at least one vaccination:", vaccinated)
