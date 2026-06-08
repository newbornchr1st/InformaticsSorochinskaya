import pandas as pd
df = pd.read_csv("C:/Users/User/Desktop/sorochinskaya_as/projects_6/task_6_0/wild_boars.csv")
print(df['tusk_length_cm'])
print(df['tusk_length_cm'].min())
print(df['tusk_length_cm'].max())