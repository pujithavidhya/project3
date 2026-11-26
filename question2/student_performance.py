
# Student Performance Trend Analysis

subjects = ["Python", "Maths", "Physics", "English"]

exam1 = []
exam2 = []

print("Enter First Exam Marks:")
for subject in subjects:
    mark = int(input(subject + ": "))
    exam1.append(mark)

print("\nEnter Second Exam Marks:")
for subject in subjects:
    mark = int(input(subject + ": "))
    exam2.append(mark)

total1 = 0
total2 = 0

print("\n--- Performance Report ---")

for i in range(len(subjects)):

    total1 += exam1[i]
    total2 += exam2[i]

    difference = exam2[i] - exam1[i]

    print("\nSubject:", subjects[i])

    if difference > 0:
        print("Improved by:", difference)

    elif difference < 0:
        print("Declined by:", -difference)

    else:
        print("No change")

print("\nFirst Exam Total:", total1)
print("Second Exam Total:", total2)

if total2 > total1:
    print("Overall Performance: Improved")

elif total2 < total1:
    print("Overall Performance: Declined")

else:
    print("Overall Performance: Same")

print("\nWeak Subjects:")

for i in range(len(subjects)):
    if exam2[i] < 40:
        print(subjects[i])
