classmates = ["Enian", "Arjon", "Jack", "Matteo", "Louis"]

print("Number of classmates: ", len(classmates))
print("First classmate: ", classmates[0])
print("Last classmate: ", classmates[-1])
print("First three: ", classmates[:3])

classmates.append("John")
print("After adding John: ", classmates)

classmates.remove("Jack")
print("After removing jack: ", classmates)

classmates.sort()
print("Sorted in alphabetical order: ", classmates)

classmates.reverse()
print("Reversed: ", classmates)


teacher = {"name" : "Mr.Smith", "Subject" : "python", "experience" : 5}

print("Teacher profile: ", teacher)


print("Subject: ", teacher["Subject"])
print("Experience: ", teacher.get("experience", "not found"))
teacher["experience"] = 6
teacher["email"] = "smith@gmail.com"
teacher.pop("experience")
print("Updated teacher profile: ", teacher)



roll_numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie", "David", "Eva"]
student_directory = dict(zip(roll_numbers, names))
print("Student directory: ", student_directory)
print("Student at Roll 3: ", student_directory[3])



