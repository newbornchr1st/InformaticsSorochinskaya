import pandas as pd
df = pd.read_csv("C:/Users/User/Desktop/sorochinskaya_as/projects_6/task_6_0/wild_boars.csv")

gender_75 = df.groupby('gender')['length_cm'].quantile(0.75)
gender_25 = df.groupby('gender')['length_cm'].quantile(0.25)

with open('iqr_length_values.txt', 'w', encoding='utf-8') as iqr:
    iqr.write(str(gender_75 - gender_25))