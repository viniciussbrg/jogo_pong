import sys
import re

in_path     = sys.argv[1]
out_path    = sys.argv[2] if len(sys.argv) > 2 else None

if out_path is None:
    out_path = in_path + ".bin"

in_file = open(in_path, "r")
chr_dat = [x[:4] for x in in_file.read().split("\n") if x]
in_file.close()

out_data = []

if len(chr_dat) % 8 != 0:
    raise ValueError(f"Malformed character(s)!\nSize is {len(chr_dat)}")

for i in range(0, len(chr_dat), 8):
    if len(chr_dat[i]) % 4 != 0:
        raise ValueError(f"Malformed character(s)!\nSize is {len(chr_dat[i])}")
    for j in range(4):
        chr_col = "".join([r[3-j] for r in chr_dat[i:i+8]])
        chr_col = re.sub("[Oo\\_\\ \\.]", "0", re.sub("[\\#Xx\\*]", "1", chr_col))
        print(f"{[r[3-j] for r in chr_dat[i:i+8]]} -> {chr_col}")
        out_data.append(int(chr_col, 2))
    print("")
 
out_file = open(out_path, "wb")
out_file.write(bytearray(out_data))
out_file.close()        
