import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Dept":["IT","HR","IT","HR"],
    "Salary":[50000,40000,60000,45000]
}
df=pd.DataFrame(data)
print(df)
avg_salary=df.groupby("Dept")["Salary"].mean()
print(avg_salary)
#highest paid 
highest_paid=df.loc[df.groupby("Dept")["Salary"].idxmax()]
print("highest paid employee:")
print(highest_paid)
#count employees per dept
emp_count=df.groupby("Dept")["Name"].count()
print("employees count per dept:")
print(emp_count)
#sort dep by avg salary
sorted_avg_salary=avg_salary.sort_values(ascending=False)
print("dept sorted by avg salary")
print(sorted_avg_salary)
