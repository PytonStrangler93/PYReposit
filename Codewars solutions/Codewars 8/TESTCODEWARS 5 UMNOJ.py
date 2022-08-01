def paperwork(n, m):
    # Happy Coding! ^_^
    if n > 0 and m > 0:
        return n * m
    else:
        return (n, m), 0, f"Failed at Paperwork{n, m}"


paperwork = lambda a,b: a*b if min(a,b)>0 else 0
