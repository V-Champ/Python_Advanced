# student directory
class student:
    def __init__(
        self, ad_no, name, class_section, gender, dob, blood_gp, contact, address
    ):
        self.ad_no = ad_no
        self.name = name
        self.class_section = class_section
        self.gender = gender
        self.dob = dob
        self.blood_gp = blood_gp
        self.contact = contact
        self.address = address


    def display(self):
        print(f"{self.ad_no:<10} {self.name:<20} {self.class_section:<10} {self.dob:<20}\
               {self.gender:<15} {self.blood_gp:<20} {self.contact:<20} {self.address:<120}")

# get number of students:
num_students = int(input("Enter the number of students"))

students = []

# input details for each student
for i in range(num_students):
    ad_no = input("\nAdmission Number: ")
    name = input("Name: ")
    class_section = input("Class & Section: ")
    dob = input("Date of Birth (DD-MM-YYYY): ")
    gender = input("Gender: ")
    blood_gp = input("Blood Group: ")
    contact = input("Contact Number: ")
    address = input("Address: ")
    student_obj = student(
        ad_no, name, class_section, gender, dob, blood_gp, contact, address
    )

    students.append(student_obj)


# Display all student details
print("\n{:<10} {:<20} {:<10} {:<20} {:<15} {:<20} {:<20} {}".format(
        "Adm No", "Name", "Class", "DOB","Gender", "BloodGrp", "Contact", "Address"
    )
)
print("-" * 150)

for student in students:
    student.display()
