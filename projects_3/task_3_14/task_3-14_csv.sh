#!/bin/bash
FILE="data.csv"
#названия товаров
awk -F',' '{print $2}' "$FILE"
echo
#товары дороже 20
awk -F',' '$3 > 20 {print $2, "-", $3}' "$FILE"
echo
#общая стоимость всех товаров
awk -F',' '{sum += $3} END {print sum}' "$FILE"
echo
