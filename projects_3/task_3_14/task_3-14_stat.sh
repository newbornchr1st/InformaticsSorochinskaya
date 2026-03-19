#!/bin/bash
FILE="students.txt"
awk '{sum += $2} END {print sum}' "$FILE"
echo
#сумма всех оценок
awk '{sum += $2; count++} END {printf "%.2f\n", sum/count}' "$FILE"
echo
#средняя оценка
awk 'BEGIN {max = 0} {if ($2 > max) max = $2} END {print max}' "$FILE"
echo
#максимальная оценка
