import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset with full path
df = pd.read_csv(r"E:\DMV_lab\Students_Performance_dataset.csv")


# Trim to 30 rows × 30 columns
df = df.iloc[:30, :30]

# Handle missing values
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col].fillna(df[col].median(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

# Detect outliers using IQR
outliers = {}
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outlier_rows = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    if not outlier_rows.empty:
        outliers[col] = outlier_rows.index.tolist()

print("Outliers detected:", outliers)

# Save cleaned dataset
df.to_csv(r"e:\DMV_lab\Cleaned_Students_Performance.csv", index=False)

# Bar chart (Average CGPA by Gender)
plt.figure(figsize=(8,6))
df.groupby("Gender")["What is your current CGPA?"].mean().plot(kind="bar", color=['skyblue','lightgreen'])
plt.xlabel("Gender")
plt.ylabel("Average CGPA")
plt.title("Average CGPA by Gender")
plt.legend(["Average CGPA"])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Scatter Plot: CGPA vs Attendance
plt.figure(figsize=(8,6))
plt.scatter(df["Average attendance on class"], df["What is your current CGPA?"], c="blue", alpha=0.6)
plt.xlabel("Average Attendance (%)")
plt.ylabel("Current CGPA")
plt.title("Scatter Plot: CGPA vs Attendance")
plt.legend(["Students"])
plt.tight_layout()
plt.show()


# Pie Chart: Gender distribution (first 30 rows)
plt.figure(figsize=(6,6))
gender_counts = df.iloc[:30]["Gender"].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart: Gender Distribution (First 30 Rows)")
plt.legend(gender_counts.index, title="Gender")
plt.tight_layout()
plt.show()

# Stair (Step) Chart: CGPA progression across students
plt.figure(figsize=(8,6))
plt.step(range(len(df)), df["What is your current CGPA?"], where="mid", color="green")
plt.xlabel("Student Index")
plt.ylabel("Current CGPA")
plt.title("Stair Chart: CGPA Progression")
plt.legend(["CGPA"])
plt.tight_layout()
plt.show()


# Line Chart: Average CGPA by Scholarship status
plt.figure(figsize=(8,6))
scholarship_avg = df.groupby("Do you have meritorious scholarship ?")["What is your current CGPA?"].mean()
scholarship_avg.plot(kind="line", marker="o", color="red")
plt.xlabel("Scholarship Status (Yes/No)")
plt.ylabel("Average CGPA")
plt.title("Line Chart: Average CGPA by Scholarship Status")
plt.legend(["Average CGPA"])
plt.tight_layout()
plt.show()


# Bar Chart: Average CGPA by Gender
plt.figure(figsize=(8,6))
df.groupby("Gender")["What is your current CGPA?"].mean().plot(kind="bar", color=['skyblue','lightgreen'])
plt.xlabel("Gender")
plt.ylabel("Average CGPA")
plt.title("Bar Chart: Average CGPA by Gender")
plt.legend(["Average CGPA"])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()