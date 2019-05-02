def fit1(rows):
    print("Y = %.2f X - %.2f" % (ax_b(rows)))
    pass


def fit2(rows):
    print_fit(2, 0.6, 1707.97, 5.32, 574.54)


def corelation(rows):
    pass


def do_calc(years, rows):
    countries = [c[0] for c in rows]
    print("Country: ", end="")
    print(*countries, sep=", ")
    fit1(str_to_nb(rows))
    fit2(rows)
    corelation(rows)


def print_fit(n, a, b, rm, pop):
    print("Fit%d" % n)
    print("\t%c = %.2f X - %.2f" % ("Y" if n == 1 else "X", a, b))
    print("\tRoot-mean-square deviation: %.2f" % rm)
    print("\tPopulation in 2050: %.2f" % pop)


def ax_b(rows):
    year = list(range(1960, 2018))
    year_sum = sum(year)
    year_2_sum = sum(map(lambda x: x * x, year))
    pop_sum = sum(rows)
    pop_year_sum = sum(map(lambda x: x[0] * x[1], zip(year, rows)))
    b = (pop_sum * year_2_sum - year_sum * pop_year_sum) / (len(year) * year_2_sum - pow(year_sum, 2)) / 1000000
    a = (len(year) * pop_year_sum - year_sum * pop_sum) / (len(year) * year_2_sum - pow(year_sum, 2)) / 1000000
    return a, b


def str_to_nb(strtab):
    return [int(value) for value in strtab[0][2:]]
