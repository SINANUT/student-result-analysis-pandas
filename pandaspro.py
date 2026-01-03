import pandas as pd

students = pd.read_csv("projects/pandaspro.csv")

# print(students)

students["Total"] = students[["english","maths","science"]].sum(axis=1)

students["Average"] = students["Total"]/3

students["Result"] = students["Average"].apply(
    lambda x:"pass" if x>= 60 else "fail")

def grade(y):
    if y >= 260:
        return("A+")
    elif y >= 240:
        return("A")
    elif y >= 200:
        return("B")
    elif y >= 180:
        return("C")
    elif y>= 160:
        return("D")
    else:
        return("No Grades")
    
students["Grade"] = students["Total"].apply(grade)

students["Rank"] = students["Total"].rank(ascending=False,method="dense").astype(int)

print(students)

# print("Topper is",students[["Name","Total"]][students.Total==students.Total.max()].values[0])

topper = students[students.Total == students.Total.max()]
print("\nTopper is",topper["Name"].values[0], "with total", topper["Total"].values[0])

subject_avg = students[["english","maths","science"]].mean(axis=0)
print("\nSubject wise average :")
print(subject_avg)

print("\nsorted table on the basis of total mark :")
print(students.sort_values("Total",ascending=False)[["Name","Total"]])


subject_avg.to_csv("result_subject.csv")
students.to_csv("results.csv",index= False)