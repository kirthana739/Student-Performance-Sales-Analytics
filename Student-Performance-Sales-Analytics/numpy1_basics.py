
import numpy as np
marks = np.array([
    [80, 75, 90],
    [60, 85, 70],
    [95, 90, 85]
])

students = np.array(["kirthana", "rikki", "khushi"])
subjects = np.array(["Python", "Java", "Statistics"])
print("\nComplete Student Marks Array:")
print(marks)
print("\nNumber of Dimensions:", marks.ndim)
print("Shape of Array:", marks.shape)
print("Total Number of Elements:", marks.size)
print("Data Type:", marks.dtype)
print("Total Marks of All Students:", np.sum(marks))
student_total = np.sum(marks, axis=1)

print("\nStudent-wise Total Marks:")
for i in range(len(students)):
    print(students[i], ":", student_total[i])
student_average = np.mean(marks, axis=1)
print("\nStudent-wise Average Marks:")
for i in range(len(students)):
    print(students[i], ":", round(student_average[i], 2))
subject_total = np.sum(marks, axis=0)
print("\nSubject-wise Total Marks:")
for i in range(len(subjects)):
    print(subjects[i], ":", subject_total[i])
subject_average = np.mean(marks, axis=0)
print("\nSubject-wise Average Marks:")
for i in range(len(subjects)):
    print(subjects[i], ":", round(subject_average[i], 2))
print("\nHighest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
topper_index = np.argmax(student_total)
print("\nClass Topper:", students[topper_index])
print("Topper's Total Marks:", student_total[topper_index])
best_subject_index = np.argmax(subject_average)
print("\nBest Performing Subject:", subjects[best_subject_index])
print("Highest Subject Average:", round(subject_average[best_subject_index], 2))
arr = np.arange(1, 25)
print("\nOriginal Array:")
print(arr)
arr_2d = arr.reshape(4, 6)
print("\n2-D Array (4 Rows and 6 Columns):")
print(arr_2d)
arr_3d = arr.reshape(2, 3, 4)
print("\n3-D Array (2, 3, 4):")
print(arr_3d)
print("\nShape of 2-D Array:", arr_2d.shape)
print("Shape of 3-D Array:", arr_3d.shape)
print("\nDimensions of 2-D Array:", arr_2d.ndim)
print("Dimensions of 3-D Array:", arr_3d.ndim)

# Print total number of elements
print("\nTotal Elements in 2-D Array:", arr_2d.size)
print("Total Elements in 3-D Array:", arr_3d.size)
print("\nSum of 2-D Array:", np.sum(arr_2d))
print("Average of 2-D Array:", np.mean(arr_2d))
print("Maximum Value:", np.max(arr_2d))
print("Minimum Value:", np.min(arr_2d))
print("\nRow-wise Sum:", np.sum(arr_2d, axis=1))
print("Column-wise Sum:", np.sum(arr_2d, axis=0))
sales = np.array([
    [[100, 200], [150, 250], [180, 300]],
    [[120, 220], [170, 270], [200, 350]]
])
branches = np.array(["Branch 1", "Branch 2"])
months = np.array(["January", "February", "March"])
products = np.array(["Product 1", "Product 2"])
print("\nSales Data:")
print(sales)
print("\nNumber of Dimensions:", sales.ndim)
print("Shape of Array:", sales.shape)
print("Total Number of Elements:", sales.size)
print("Total Sales of Company:", np.sum(sales))
print("Average Sales:", np.mean(sales))
branch_sales = np.sum(sales, axis=(1, 2))

print("\nBranch-wise Total Sales:")
for i in range(len(branches)):
    print(branches[i], ":", branch_sales[i])

best_branch = np.argmax(branch_sales)
print("\nBest Performing Branch:", branches[best_branch])
month_sales = np.sum(sales, axis=(0, 2))
print("\nMonth-wise Total Sales:")
for i in range(len(months)):
    print(months[i], ":", month_sales[i])
best_month = np.argmax(month_sales)
print("\nHighest Sales Month:", months[best_month])
product_sales = np.sum(sales, axis=(0, 1))
print("\nProduct-wise Total Sales:")
for i in range(len(products)):
    print(products[i], ":", product_sales[i])
best_product = np.argmax(product_sales)
print("\nHighest Selling Product:", products[best_product])
print("\nHighest Individual Sale:", np.max(sales))
print("Lowest Individual Sale:", np.min(sales))
numbers = np.arange(1, 61)
numbers_3d = numbers.reshape(3, 4, 5)
print("\n3-D Array (3, 4, 5):")
print(numbers_3d)
print("\nNumber of Dimensions:", numbers_3d.ndim)
print("Shape of Array:", numbers_3d.shape)
print("Total Number of Elements:", numbers_3d.size)
print("Data Type:", numbers_3d.dtype)
numbers_2d = numbers_3d.reshape(12, 5)
print("\n2-D Array (12 Rows and 5 Columns):")
print(numbers_2d)
print("\nOriginal Array Elements:", numbers_3d.size)
print("Reshaped Array Elements:", numbers_2d.size)
print("Both Arrays Have Same Number of Elements:",
      numbers_3d.size == numbers_2d.size)
print("\nSum of All Elements:", np.sum(numbers_3d))
print("Average of All Elements:", np.mean(numbers_3d))
print("Maximum Element:", np.max(numbers_3d))
print("Minimum Element:", np.min(numbers_3d))
print("All Elements Are Positive:", np.all(numbers_3d > 0))
print("Any Element Greater Than 50:", np.any(numbers_3d > 50))
print("\nAvailable Students:")
for student in students:
    print(student)
selected_student = input("\nEnter student name: ").strip()
student_index = np.where(students == selected_student)[0]
if len(student_index) > 0:
    index = student_index[0]
    print("\nStudent:", students[index])
    print("Subject-wise Marks:")
    for i in range(len(subjects)):
        print(subjects[i], ":", marks[index, i])
    print("Total Marks:", np.sum(marks[index]))
    print("Average Marks:", np.mean(marks[index]))
else:
    print("Invalid student name!")
print("\nAvailable Subjects:")
for subject in subjects:
    print(subject)
selected_subject = input("\nEnter subject name: ").strip()
subject_index = np.where(subjects == selected_subject)[0]
if len(subject_index) > 0:
    index = subject_index[0]
    print("\nSelected Subject:", subjects[index])
    for i in range(len(students)):
        print(students[i], ":", marks[i, index])
    print("Highest Mark:", np.max(marks[:, index]))
    print("Lowest Mark:", np.min(marks[:, index]))
    print("Average Mark:", np.mean(marks[:, index]))
else:
    print("Invalid subject name!")


zero_d = np.array(10)
print("\n0-D Array:", zero_d)
print("Dimensions:", zero_d.ndim)

print("\n1-D Indexing:", arr[0])
print("1-D Slicing:", arr[1:6])


print("\n2-D Indexing:", arr_2d[0, 1])
print("2-D Slicing:")
print(arr_2d[0:2, 0:3])


print("\n3d Indexing:", numbers_3d[0, 0, 0])
print("3-D Slicing:")
print(numbers_3d[0, :, :])
# ==========================================
# QUESTION 1: 2-D ARRAY OPERATIONS
# ==========================================

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])
print("\nElement at row 0, column 2:")
print(arr[0, 2])
print("\nEntire Third Row:")
print(arr[2, :])
print("\nEntire Second Column:")
print(arr[:, 1])
print("\nFirst Two Rows:")
print(arr[:2, :])
print("\nFirst Three Columns:")
print(arr[:, :3])
arr = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ],
    [
        [130, 140, 150],
        [160, 170, 180]
    ]
])

print("\nFirst Element of First Block:")
print(arr[0, 0, 0])

print("\nSecond Row of Second Block:")
print(arr[1, 1, :])

print("\nAll Elements of First Block:")
print(arr[0, :, :])

print("\nFirst Row from All Three Blocks:")
print(arr[:, 0, :])

print("\nSecond Column from All Blocks:")
print(arr[:, :, 1])

print("\nLast Two Blocks Completely:")
print(arr[1:, :, :])