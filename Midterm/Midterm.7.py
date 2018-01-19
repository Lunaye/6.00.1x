def dict_interdiff(d1, d2):
    interdiff = ()
    newd1 = {}
    newd2 = {}

    for key in d1:
        if key in d2:
            val = d1[key] = (f(d1[key], d2[key]))
            newd1[key] = val
        else:
            newd2[key] = d1.get(key)

    for key in d2:
        if key not in d1:
            newd2[key] = d2.get(key)

    return (newd1, newd2)
