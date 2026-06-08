import pandas as pd
df = pd.read_csv("C:/Users/User/Desktop/sorochinskaya_as/projects_6/task_6_0/wild_boars.csv")
with open('mean_values.txt', 'w', encoding='utf-8') as means:
    for col in df.columns[2:]:  
        mean_val = df[col].mean()
        means.write(f"{col}: {mean_val:.2f}\n")
