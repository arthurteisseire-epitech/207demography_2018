def fit1(years, rows):
    ab = ax_b(years, rows)
    print_fit(1, ab[0], ab[1], 5.32, 574.54)
    pass


def fit2(rows):
    print_fit(2, 0.6, 1707.97, 5.32, 574.54)


def corelation(rows):
    pass


def do_calc(countries, years, values):
    print("Country: ", end="")
    print(*countries, sep=", ")
    fit1(years, values[0])
    fit2(values)
    corelation(values)


def print_fit(n, a, b, rm, pop):
    print("Fit%d" % n)
    print("\t%c = %.2f X %c %.2f" % ("Y" if n == 1 else "X", a, ("-" if b < 0 else "+"), abs(b)))
    print("\tRoot-mean-square deviation: %.2f" % rm)
    print("\tPopulation in 2050: %.2f" % pop)


def ax_b(years, val):
    year_sum = sum(years)
    year_2_sum = sum(map(lambda x: x * x, years))
    pop_sum = sum(val)
    pop_year_sum = sum(map(lambda x: x[0] * x[1], zip(years, val)))
    b = (pop_sum * year_2_sum - year_sum * pop_year_sum) / (len(years) * year_2_sum - pow(year_sum, 2)) / 1000000
    a = (len(years) * pop_year_sum - year_sum * pop_sum) / (len(years) * year_2_sum - pow(year_sum, 2)) / 1000000
    return a, b


def tab_mean(tab):
    pass

