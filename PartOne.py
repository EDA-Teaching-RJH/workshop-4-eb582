def change_case(name):
    res=[name[0].lower()]
    for c in name[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
    
    return ''.join(res)

name = input("Whats your name? ")
name = name.replace(" ","")
print(change_case(name), end="")