import pandas as pd
df = pd.read_csv("C:/Users/User/Desktop/sorochinskaya_as/projects_6/task_6_0/wild_boars.csv")
with open('median_values.txt', 'w', encoding='utf-8') as med:
    for col in df.columns[2:]:
        cont = df[col].median()
        med.write(f"{col}: {cont:.2f}\n")