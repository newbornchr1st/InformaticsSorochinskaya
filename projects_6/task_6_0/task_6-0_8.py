import pandas as pd
df = pd.read_csv("C:/Users/User/Desktop/sorochinskaya_as/projects_6/task_6_0/wild_boars.csv")

std_tusk = df.groupby('gender')['tusk_length_cm'].std()
mean_tusk = df.groupby('gender')['tusk_length_cm'].mean()

with open('tusk_length.txt' , 'w', encoding='utf-8') as tusks:
    tusks.write(f'Coefficient of tusk length variation: {(std_tusk / mean_tusk * 100)}')