#!/usr/bin/env python
# coding: utf-8

# In[1]:


# open txt file

f_path=r'/Users/zhengyu/Desktop/课件-S1/python/project/student.txt'
with open(f_path,encoding = 'UTF-8') as f:
    data = f.read()
    print(data)


# In[2]:


import pandas as pd

df =  pd.read_csv('/Users/zhengyu/Desktop/课件-S1/python/project/student.txt',sep='\t')
df.to_excel('/Users/zhengyu/Desktop/课件-S1/python/project/studentframe.xlsx')

df


# In[3]:


# Display all student records

students_df=pd.DataFrame(df)
print(students_df)


# In[4]:


#Display students whose last name begins with a certain string

students_df['Last'] = students_df['Last'].str.lower()
search = input("Enter the name to search for: ")
search_name = search.lower()
mask = students_df['Last'].str.startswith(search_name)

selected_students_df = students_df[mask]
print(selected_students_df)


# In[31]:


#Display all records for students whose graduating year is a certain year  

import pandas as pd
search_year = float(input('Enter the gradyear to search for: '))
student_records = students_df.loc[students_df['GradYear'] == search_year]
print(student_records)


# In[30]:


#Display a summary report of number and percent of students in each program, for students graduating on/after a certain year

search_year = float(input('Enter the gradyear to search for: '))
search_program = input('Enter the program to seach for: ')

print(students_df.query(f'GradYear == {search_year} and DegreeProgram == "{search_program}"').groupby('GradYear')['ID'].count())

grads_certain_year = students_df.query(f'GradYear == {search_year}')
rows_year,cols_year = grads_certain_year.shape

grads_certain_program = students_df.query(f'GradYear == {search_year} and DegreeProgram == "{search_program}"')
rows_program,cols_program = grads_certain_program.shape

value = rows_program/rows_year
percentage = value*100

print("{:.2f}%".format(percentage))


# In[ ]:




