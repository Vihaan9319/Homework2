student_data = {"ID1": {"name": "Rian", "class": "V", "Subjects": "english, math, science"},
                "ID2": {"name": "Aarav", "class": "VI", "Subjects": "english, math, History"},
                "ID3": {"name": "Saurya", "class": "IV", "Subjects": "english, math, coding"},
                "ID4": {"name": "Nathan", "class": "XI", "Subjects": "Algebra-1, english, AP Science"}}
print("Full student data: ")
print(student_data)
print("ID1:")
print(student_data.get("ID1", "Not found"))
print("ID5:")
print(student_data.get("ID5", "Not found"))
student_data["ID5"] = {"name": "Dave", "class": "VII", "Subjects": "english, math, science"}
print("Added record: ")
print(student_data.get("ID5", "Not found"))
print("New data report:")
print(student_data)
student_data["ID2"]["Subjects"] = "math, coding, history"
print("Second student's subject changed report:")
print(student_data.get("ID2", "Not found"))
cleaned_data = {}
seen_records = []
print(student_data)
for id, details in student_data.items():
    if details not in seen_records:
        seen_records.append(details)
        cleaned_data[id] = details
student_data = cleaned_data
print(f"Cleaned record: {student_data}")
cleaned_data.pop("ID4")
print()
print(f"After removing ID4: {student_data}")
print(f"The length of the data is {len(student_data)}")
print("===========FINAL STUDENT SUBJECT RECORD=============")
for id, details in student_data.items():
    print(f"{id} : {details}")
print("====================================================")