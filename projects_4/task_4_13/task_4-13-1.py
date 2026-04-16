a = float(input())
b = float(input())
c = float(input())
d = float(input())

if a < b:
    if a < c:
        if a < d:
            print(f'Min {a}')
        else: print(f'Min {d}')
    else:
        if c < d:
            print(f'Min {c}')
        else: print(f'Min {d}')
else:
    if b < c:
        if b < d:
            print(f'Min {b}')
        else: print(f'Min {d}')
    else:
        if c < d:
            print(f'Min {c}')
        else: print(f'Min {d}')