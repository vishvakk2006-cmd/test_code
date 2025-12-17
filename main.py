import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("data.csv")

# Calculate average marks using NumPy
data['Average'] = np.mean(data[['Math', 'Science', 'English']], axis=1)

# Assign grade using conditional statements
def assign_grade(avg):
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'Fail'

# Apply grading logic
data['Grade'] = data['Average'].apply(assign_grade)

# Filter passed students
passed_students = data[data['Grade'] != 'Fail']

# Display results
print("Student Performance Report\n")
print(data)

print("\nTotal Students:", len(data))
print("Students Passed:", len(passed_students))
print("Class Average:", round(np.mean(data['Average']), 2))
