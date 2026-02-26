nutrient_name = input("Название питательной среды:")
agar_concentration = input("Концентрация агара (%):")
temperature = input("Температура стерилизации:")
name = nutrient_name.upper()
with open("recipe.txt", "w", encoding="utf-8") as recipe:
 recipe.write(f"{name}\n {agar_concentration}\n {temperature}\n")
print(f"Название питательной среды: {name}\n Концентрация агара (%): {agar_concentration}\n Температура стерилизации: {temperature}")
print("Файл 'recipe.txt' успешно сформирован!")