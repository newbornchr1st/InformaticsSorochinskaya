import pandas as pd
df = pd.read_csv("C:/Users/User/Desktop/sorochinskaya_as/projects_6/task_6_0/wild_boars.csv")

with open('variability.txt', 'w', encoding='utf-8') as var:
    for col in df.columns[2:]:
        var.write(f"{col}:\n")
        var.write(f"Variance: {df[col].var():.2f}\n")
        var.write(f"Standart deviation: {df[col].std():.2f}\n")
        var.write(f"Coefficient of variation: {(df[col].std() / df[col].mean() * 100):.2f}%\n\n")