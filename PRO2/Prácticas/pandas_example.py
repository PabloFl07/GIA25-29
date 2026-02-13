import random
import pandas

"""
This code generates a list of employees and then uses the
pandas library to summarize some data according to certain
columns of interest.
"""

#We create a list of lists with the information for each employee
employees_info = []
for _ in range(100):
    #We represent an employee as a list of 4 elements [Job,sex,age,salary]
    employees_info.append([random.choice(["Developer","Sales","Systems","Manager"]),
                           random.choice(['male','female']),
                           random.randint(18,66),
                           random.randint(1000,3000)])

#This prints the list of lists with all the information
print (employees_info)

#We create the pandas DataFrame, the basic structure in pandas library
#to manage data. The first parameter is the input data (our list of lists)
#and the second parameter 'columns' is used to specify an identifier for each
#column
data = pandas.DataFrame(employees_info, columns=["Job","Sex","Age","Salary"])

#Summary of the full data
print (data)

"""
Now, we can use pandas functions to get a better understanding of the data
in an easy and quick way.
"""

#For instance, we can group data by sex using the function 'groupby' to
#know the mean salary for male and female employees.
#'groupby' receives the column IDs that we want to use for grouping, and then a diccionary
# of the target columns and the metrics that we want to compute. 
#More info about the groupby column: 
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
group_col = "Sex"
target_col = "Salary"
data_salary = data.groupby(group_col).agg({target_col :["mean","std"]})
print ("##############################")
print ("   Salary grouped by sex      ")
print ("##############################\n")
print (data_salary)

#We also can group data by job
group_col = "Job"
target_col = "Salary"
data_salary = data.groupby(group_col).agg({target_col :["mean","std"]})
print ("##############################")
print ("   Salary grouped by job      ")
print ("##############################\n")
print (data_salary)

#We can group data by multiple columns, e.g., by job and sex
group_col = ["Job","Sex"]
target_col = "Salary"
data_salary = data.groupby(group_col).agg({target_col :["mean","std"]})
print ("##############################")
print (" Salary grouped by (job,sex)  ")
print ("##############################\n")
print (data_salary)

#Grouping data by job and sex, but now sorted by salary.
#To do so, we first do the groupby and then use the function sort_values
#to specify the column(s) we want to use to sort the data
group_col = ["Job","Sex"]
target_col = "Salary"
data_salary = data.groupby(group_col).agg({target_col :["mean","std"]})
print ("##############################")
print (" Salary grouped by (job,sex)  ")
print ("  (sorted by (salary,mean))   ")
print ("##############################\n")
data_salary.sort_values(by=(target_col, "mean"), ascending=False, inplace=True)
print (data_salary)

