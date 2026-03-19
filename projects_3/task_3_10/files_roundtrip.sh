#!/bin/bash
for file in *.fasta
  if [ ! -s "$file" ]; then
    continue
  fi
  sequence=$(grep -v "^>" "$file" | tr -d '\n' | tr -d '[:space:]')
  count_a=$(echo "$sequence" | grep -io "A" | wc -l)
  count_t=$(echo "$sequence" | grep -io "T" | wc -l)
  count_g=$(echo "$sequence" | grep -io "G" | wc -l)
  count_c=$(echo "$sequence" | grep -io "C" | wc -l)
  printf "%-20s %-8s %-8s %-8s %-8s\n" "$file" "$count_a" "$count_t" "$count_g" "$count_c"
done
