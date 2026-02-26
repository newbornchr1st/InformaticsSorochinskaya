files = ["seq1", "seq2", "seq3", "seq4"]
data = "16.11.2008"

for name in files:
   new_name = name + f"_{data}_"  + ".fasta"
   print(f"{new_name}")