


def delete_nth(order,max_e):
    new_l = []
    for i in order:
        if new_l.count(i) < max_e:
            new_l.append(i)
    return new_l

def delete_nth(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ]

def delete_nth(order,max_e):
    new = []
    [new.append(a) for a in order if new.count(a) < max_e]
    return new


