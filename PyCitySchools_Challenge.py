# %%
# Add the Pandas dependency.
import pandas as pd
import os
import numpy as np

school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources","students_complete.csv")

# %%
students_data_pd = pd.read_csv(student_data_to_load)
school_data_pd = pd.read_csv(school_data_to_load) 

# %%
students_names = students_data_pd["student_name"].tolist()
students_names


# %%
students_to_fix = []

# Use an if statement to check the length of the name.
# If the name is greater than or equal to "3", add the name to the list.

for name in students_names:
    if len(name.split()) >= 3:
        students_to_fix.append(name)

# Get the length of the students whose names are greater than or equal to "3".
len(students_to_fix)

# %%
# list down the prefixes
# Add the prefixes less than or equal to 4 to a new list.

prefixes = []
for name in students_to_fix:
    if len(name.split()[0]) <= 4:
        prefixes.append(name.split()[0])

print(prefixes)

suffix = []
for name in students_to_fix:
    if len(name.split()[-1]) <= 3:
        suffix.append(name.split()[-1])

print(suffix)


# %%

# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

# Iterate through the "prefixes_suffixes" list and replace them with an empty space, "" when it appears in the student's name.
for word in prefixes_suffixes:
    students_data_pd["student_name"] = students_data_pd["student_name"].str.replace(word,"")

# %%
scorecorrection = students_data_pd.copy()
#scorecorrection["reading_score"] = scorecorrection.loc[scorecorrection["school_name"] == "Thomas High School", ["reading_score"]].fillna(np.nan, inplace = True)
#scorecorrection["reading_score"] = scorecorrection["reading_score"].fillna(np.nan, inplace = True)
#scorecorrection["math_score"] = scorecorrection["math_score"].fillna(np.nan, inplace = True)
#scorecorrection.loc[scorecorrection["school_name"] == "Thomas High School"].groupby(["reading_score"]) = np.nan

scorecorrection.loc[scorecorrection["school_name"] == "Thomas High School", ["reading_score", "math_score"]] = np.nan


# %%
# Combine the data into a single dataset.
school_data_complete_df = pd.merge(scorecorrection, school_data_pd, on=["school_name", "school_name"])
school_data_complete_df.head()


# %%
