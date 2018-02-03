students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("student.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("cant save the file")


def read_file(student):
    try:
        f = open("student.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("cant read the file")


while True:
    user_option = raw_input("Do you want to add student. enter yes if you want to:")
    if user_option == "yes":
        student_name = raw_input("enter name:")
        student_id = raw_input("enter id:")
        add_student(student_name, student_id)
    else:
        break
print_students_titlecase()