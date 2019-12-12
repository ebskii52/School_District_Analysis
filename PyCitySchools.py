# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Add the Pandas dependency.
import pandas as pd

# Files to load
#school_data_to_load = "Resources/schools_complete.csv"
#student_data_to_load = "Resources/students_complete.csv"

#or
import os
school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources","students_complete.csv")


# %%
# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)# Define the function "say_hello" so it prints "Hello!" when called.
def say_hello():
    print("Hello!")
student_data_df = pd.read_csv(student_data_to_load)
# Determine if there are any missing values in the school data.
school_data_df.count()


# %%
# Determine if there are any missing values in the school data.
school_data_df.isnull()


# %%
# Determine if there are any missing values in the student data.
student_data_df.notnull().sum()


# %%
# Determine data types for the school DataFrame.
school_data_df.dtypes

school_data_df.dtypes


# %%
# Put the student names in a list.
student_names = student_data_df["student_name"].tolist()
student_names


# %%
# Create a new list and use it for the for loop to iterate through the list.
students_to_fix = []

# Use an if statement to check the length of the name.
# If the name is greater than or equal to "3", add the name to the list.

for name in student_names:
    if len(name.split()) >= 3:
        students_to_fix.append(name)

# Get the length of the students whose names are greater than or equal to "3".
len(students_to_fix)


# %%
print(students_to_fix)


# %%
# Add the prefixes less than or equal to 4 to a new list.
prefixes = []
for name in students_to_fix:
    if len(name.split()[0]) <= 4:
        prefixes.append(name.split()[0])

##print(prefixes)

set(prefixes)


# %%
# Add the prefixes less than or equal to 4 to a new list.
suffix = []
for name in students_to_fix:
    if len(name.split()[-1]) <= 3:
        suffix.append(name.split()[-1])

print(suffix)


# %%
set(suffix)


# %%
# Strip "Mrs." from the student names
for name in students_to_fix:
    print(name.replace("Dr. ", ""))


# %%
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

# Iterate through the "prefixes_suffixes" list and replace them with an empty space, "" when it appears in the student's name.
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

##student_data_df["student_name"].tail(20)

# Put the cleaned students' names in another list.
student_names = student_data_df["student_name"].tolist()
student_names


# %%
# Create a new list and use it for the for loop to iterate through the list.
students_fixed = []

# Use an if statement to check the length of the name.

# If the name is greater than or equal to 3, add the name to the list.

for name in student_names:
    if len(name.split()) >= 3:
        students_fixed.append(name)

# Get the length of the students' names that are greater than or equal to 3.
len(students_fixed)


# %%
# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()


# %%
# Get the total number of students.
student_count = school_data_complete_df.count()
student_count


# %%
# Calculate the total number of schools.
school_count = school_data_df["school_name"].count()
school_count


# %%
# Calculate the total number of schools
school_count_2 = len(school_data_complete_df["school_name"].unique())
school_count_2


# %%
# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget


# %%
# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# %%
# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# %%
passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70


# %%
# Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
#passing_math["student_name"].count()
len(passing_math)


# %%
# Get all the students that are passing reading in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
len(passing_reading)


# %%
# Calculate the total number of schools.
student_count = student_data_df["Student ID"].count()

# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()

# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()

# Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count) * 100

# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count) * 100

# Calculate the overall passing percentage.
overall_passing_percentage = (passing_math_percentage + passing_reading_percentage ) / 2

overall_passing_percentage


# %%
# Adding a list of values with keys to create a new DataFrame.
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df


# %%
# Define the function "say_hello" so it prints "Hello!" when called.
def say_hello():
    print("Hello!")

# %%
# Call the function.
say_hello()

# %%
# Define the function "say_something" so it prints whatever is passed as the variable when called.
def say_something(something):
    print(something)

# Call the function.
say_something("Hello World")


# %%
# Define a function that calculates the percentage of students that passed both # math and reading and prints the passing percentage to the output when the
# function is called.
def passing_math_percent(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100

passing_math_count = 29370
total_student_count = 39170

# Call the function.
passing_math_percent(passing_math_count, total_student_count)


# %%
# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

district_summary_df["Total Students"]




# %%
# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)

district_summary_df["Average Math Score"]

# %%
# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df# %%


# %%
