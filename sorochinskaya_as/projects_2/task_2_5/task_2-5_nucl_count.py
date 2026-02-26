print("=== Анализ последовательности ДНК ===")

nucl = input("Введите последовательность ДНК: ")

print("Последовательность в верхнем регистре: ", nucl.upper())
print("Подсчёт нуклеотидов:")
print("A: ", nucl.upper().count("A"), "\nT: ", nucl.upper().count("T"))
print("G: ", nucl.upper().count("G"), "\nC: ", nucl.upper().count("C"))
print("Общая длина: ", len(nucl))