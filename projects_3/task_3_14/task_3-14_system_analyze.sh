#!/bin/bash
printf "%-35s %-10s %-10s\n" "Файловая система" "Использовано" "Статус"
printf "%-35s %-10s %-10s\n" "-----------------------------------" "----------" "----------"
df -h | awk '
NR > 1 {
    gsub(/%/, "", $5)
    usage = $5
    if (usage > 90) {
        status = "РИТИЧНО"
    } else if (usage > 70) {
        status = "Внимание"
    } else {
        status = "Норма"
    }
    printf "%-35s %-10s %-10s\n", $1, $5"%", status
    if (usage > 90) {
        print "ПРЕДУПРЕЖДЕНИЕ: Файловая система " $1 " заполнена на " $5 "%!"
    }
}
'
CRITICAL=$(df -h | awk 'NR > 1 {gsub(/%/,"",$5); if($5 > 90) count++} END {print count+0}')

if [ "$CRITICAL" -gt 0 ]; then
    echo " Найдено критических разделов: $CRITICAL"
    echo "   Рекомендуется освободить место!"
else
    echo " Все файловые системы в норме"
fi
