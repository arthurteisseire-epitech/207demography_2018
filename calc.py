def fit1(rows):
    pass


def fit2(rows):
    pass


def corelation(rows):
    pass


def do_calc(rows):
    countries = [c[0] for c in rows]
    print("Country: ", end="")
    print(*countries, sep=", ")
    fit1(rows)
    fit2(rows)
    corelation(rows)
