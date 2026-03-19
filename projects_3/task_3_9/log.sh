#!/bin/bash
log="./system.log"
if [ -f "$log" ]; then
  echo "Файл найден"
else
  echo "файл не найден"
fi
