import csv
filepath = "student_test_scores.csv"
students = []

with open(filepath, "r", newline="") as file:
    content = csv.reader(file)
    next(content)
    for name, score in content:
        score = int(score)
        print(f"{name}: {score}")
        students.append([name, score])
        if score >= 70:
            with open("passed.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, score])
        elif score < 70:
            with open("failed.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, score])

highest = max(students, key = lambda x: x[1])
lowest = min(students, key = lambda x: x[1])
average = sum(student[1] for student in students) / len(students)

print("\n--- Class Statistics ---")
print(f"Highest Score: {highest[0]} - {highest[1]}")
print(f"Lowest Score: {lowest[0]} - {lowest[1]}")
print(f"Average Score: {average:.2f}")