V_solution = int(input("Введите нужный объем будущего раствора (мл): "))
salt_mass = V_solution * 0.009

with open ("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    recipe.write(23*"-")
    recipe.write(f"\nОбщий объем:\t{V_solution} мл\nМасса соли:\t{salt_mass:.2f} г\nОбъем воды:\t{V_solution} мл")