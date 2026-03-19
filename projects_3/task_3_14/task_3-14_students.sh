#!/bin/bash
FILE="students.txt"
awk '{print $1}' "$FILE"
echo
  #вывод только имен
awk '{print $2}' "$FILE"
echo
  #вывод только оценок
awk '{print NR, $1}' "$FILE"
echo
  #вывод номера строки и имени
