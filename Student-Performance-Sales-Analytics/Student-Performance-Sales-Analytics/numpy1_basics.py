import numpy as np

# =====================================================
# STUDENT PERFORMANCE ANALYTICS SYSTEM USING NUMPY
# =====================================================

# SUBJECT NAMES
subjects = np.array([
    "Python",
    "Mathematics",
    "Statistics",
    "Computer Science",
    "Database Management"
])

# STUDENT NAMES
students = np.array([f"Student {i}" for i in range(1, 21)])

# =====================================================
# Q1. ARRAY CREATION AND DIMENSIONS
# =====================================================

marks = np.array([
    [85, 78, 92, 88, 80],
    [76, 85, 79, 90, 82],
    [95, 92, 89, 94, 96],
    [45, 55, 60, 50, 48],
    [67, 72, 70, 75, 69],
    [88, 91, 85, 89, 92],
    [32, 45, 50, 40, 38],
    [90, 87, 93, 95, 91],
    [56, 62, 58, 65, 60],
    [78, 80, 82, 75, 79],
    [92, 95, 90, 88, 94],
    [35, 28, 42, 38, 30],
    [81, 84, 86, 80, 83],
    [69, 74, 71, 68, 73],
    [98, 96, 94, 97, 99],
    [50, 48, 55, 52, 58],
    [87, 89, 91, 85, 88],
    [73, 68, 76, 70, 74],
    [40, 35, 38, 42, 45],
    [94, 90, 96, 92, 95]
])

print("\n========== Q1: ARRAY CREATION ==========")

print("\nComplete Student Marks Array:")
print(marks)

print("\nShape:", marks.shape)
print("Size:", marks.size)
print("Dimensions:", marks.ndim)
print("Data Type:", marks.dtype)

# =====================================================
# Q2. ARRAY INDEXING AND SLICING
# =====================================================

print("\n========== Q2: INDEXING AND SLICING ==========")

print("\nMarks of First 5 Students:")
print(marks[:5])

print("\nPython Marks of All Students:")
print(marks[:, 0])

print("\nMathematics and Statistics Marks of Students 5 to 10:")
print(marks[4:10, 1:3])

print("\nMarks of Last 5 Students:")
print(marks[-5:])

# =====================================================
# Q3. MATHEMATICAL OPERATIONS
# =====================================================

print("\n========== Q3: MATHEMATICAL OPERATIONS ==========")

# Total marks of each student
total_marks = np.sum(marks, axis=1)

print("\nStudent-wise Total Marks:")
for i in range(len(students)):
    print(students[i], ":", total_marks[i])

# Percentage calculation
percentage = (total_marks / 500) * 100

print("\nStudent-wise Percentage:")
for i in range(len(students)):
    print(students[i], ":", round(percentage[i], 2), "%")

# Add 5 grace marks without exceeding 100
grace_marks = np.minimum(marks + 5, 100)

print("\nMarks After Adding 5 Grace Marks:")
print(grace_marks)

# Difference between highest and lowest marks
mark_difference = np.max(marks, axis=1) - np.min(marks, axis=1)

print("\nDifference Between Highest and Lowest Marks:")
print(mark_difference)

# =====================================================
# Q4. STATISTICAL CALCULATIONS
# =====================================================

print("\n========== Q4: STATISTICAL CALCULATIONS ==========")

# Subject-wise average
subject_average = np.mean(marks, axis=0)

print("\nSubject-wise Average Marks:")
for i in range(len(subjects)):
    print(subjects[i], ":", round(subject_average[i], 2))

# Highest marks in each subject
print("\nHighest Marks in Each Subject:")
print(np.max(marks, axis=0))

# Lowest marks in each subject
print("\nLowest Marks in Each Subject:")
print(np.min(marks, axis=0))

# Overall class average
class_average = np.mean(marks)

print("\nOverall Class Average:", round(class_average, 2))

# Standard deviation
subject_std = np.std(marks, axis=0)

print("\nSubject-wise Standard Deviation:")
for i in range(len(subjects)):
    print(subjects[i], ":", round(subject_std[i], 2))

# Highest and lowest average subjects
best_subject = subjects[np.argmax(subject_average)]
lowest_subject = subjects[np.argmin(subject_average)]

print("\nHighest Average Subject:", best_subject)
print("Lowest Average Subject:", lowest_subject)

# =====================================================
# Q5. CONDITIONAL INDEXING
# =====================================================

print("\n========== Q5: CONDITIONAL INDEXING ==========")

# Students scoring above 80%
above_80 = np.where(percentage > 80)[0]

print("\nStudents Scoring Above 80%:")
for i in above_80:
    print(students[i], ":", round(percentage[i], 2), "%")

# Students failing at least one subject
failed_students = np.where(np.any(marks < 35, axis=1))[0]

print("\nStudents Failed in At Least One Subject:")
for i in failed_students:
    print(students[i])

# Students scoring above 90 in Python
python_above_90 = np.where(marks[:, 0] > 90)[0]

print("\nStudents Scoring Above 90 in Python:")
for i in python_above_90:
    print(students[i], ":", marks[i, 0])

# Students passing all subjects
passed_all = np.all(marks >= 35, axis=1)

pass_count = np.sum(passed_all)

print("\nTotal Students Passed All Subjects:", pass_count)

# =====================================================
# Q6. ARRAY MANIPULATION
# =====================================================

print("\n========== Q6: ARRAY MANIPULATION ==========")

# Sort students based on total marks in descending order
sorted_indices = np.argsort(total_marks)[::-1]

print("\nStudents Ranked by Total Marks:")
for rank, i in enumerate(sorted_indices, start=1):
    print(rank, students[i], ":", total_marks[i])

# Top 3 students
print("\nTOP 3 STUDENTS:")
for i in sorted_indices[:3]:
    print(students[i], ":", total_marks[i])

# Reshape into 3D array
marks_3d = marks.reshape(4, 5, 5)

print("\n3D Array Shape:", marks_3d.shape)
print("\nReshaped 3D Array:")
print(marks_3d)

# Flatten the original array
flattened_marks = marks.flatten()

print("\nFlattened 1D Array:")
print(flattened_marks)

# Replace marks below 35 with zero
updated_marks = np.where(marks < 35, 0, marks)

print("\nMarks Below 35 Replaced With Zero:")
print(updated_marks)
