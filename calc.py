def fit1(rows):
    print_fit(1, 1.62, 2749.67, 5.22, 570.85)


def fit2(rows):
    print_fit(2, 0.6, 1707.97, 5.32, 574.54)


def corelation(rows):
    pass


def do_calc(years, rows):
    countries = [c[0] for c in rows]
    print("Country: ", end="")
    print(*countries, sep=", ")
    fit1(rows)
    fit2(rows)
    corelation(rows)


def print_fit(n, a, b, rm, pop):
    print("Fit%d" % n)
    print("\t%c = %.2f X - %.2f" % ("Y" if n == 1 else "X", a, b))
    print("\tRoot-mean-square deviation: %.2f" % rm)
    print("\tPopulation in 2050: %.2f" % pop)
