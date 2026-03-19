#!/bin/bash
FILE="students.txt"
awk '$2 > 80 {print $1, $2}' "$FILE"
echo    
   #выше 80
awk '$2 < 70 {print $1, $2}' "$FILE"
echo
   #ниже 70
head -n 1 "$FILE"
echo
   #первая строка файла
