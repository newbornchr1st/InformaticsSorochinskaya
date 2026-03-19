#!/bin/bash

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo " Ошибка: недостаточно прав"
        echo "   Пожалуйста, запустите скрипт от имени root"
        exit
    else
        echo " Продолжение работы..."
    fi
}
