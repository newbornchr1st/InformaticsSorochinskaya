import pandas as pd
df = pd.read_csv("C:/Users/User/Desktop/sorochinskaya_as/projects_6/task_6_0/wild_boars.csv")
with open('mode_values.txt', 'w', encoding='utf-8') as f:
    for col in df.columns[1: ]:
        mode_val = df[col].mode()
        f.write(f"{col}: {mode_val}\n")