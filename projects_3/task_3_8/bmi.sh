#!/bin/bash
read -p "Введите ваш вес в кг: " WEIGHT
read -p "Введите ваш рост в м: " HEIGHT
BMI=$((WEIGHT / ( HEIGHT * HEIGHT )))
echo "Ваш ИМТ: $BMI"
