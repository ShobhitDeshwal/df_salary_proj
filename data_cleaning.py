# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:04:45 2021

@author: shobhit deshwal
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
df = df[df['Salary Estimate']!='-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)


min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+ df.max_salary)/2


# Company name text only
df['company_txt'] = df.apply(lambda x: x['Compnay Name'] if x['Rating'] <0 else x['Company Name'][:-3],axis=1)



# state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()


# age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2021-x)


# parsing of job description (python, etc.)
df['Job Description'] 

# python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

# r studion
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'exdel' in x.lower() else 0)



df_out = df

df_out.to_csv('salary_data_cleaned.csv',index=False)




















