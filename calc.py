from math import sqrt

def fit(n, years, rows, f):
    a = b = 0
    for row in rows:
        ab = f(years, row)
        a += ab[0]
        b += ab[1]
    r = rmsd(n, years, rows[0], a, b)
    if n == 1:
        print_fit(1, a, b, r, a * 2050 + b)
    else:
        print_fit(2, a, b, r, (2050 - b) / a)


def do_calc(countries, years, values):
    print("Country: ", end="")
    print(*countries, sep=", ")
    fit(1, years, values, ax_b)
    fit(2, years, values, ay_b)


def print_fit(n, a, b, rm, pop):
    print("Fit%d" % n)
    if n == 1:
        print("\tY = %.2f X %c %.2f" % (a / 1000000, ("-" if b < 0 else "+"), abs(b / 1000000)))
    else:
        print("\tX = %.2f Y %c %.2f" % (a * 1000000, ("-" if b < 0 else "+"), abs(b)))
    print("\tRoot-mean-square deviation: %.2f" % (rm / 1000000))
    print("\tPopulation in 2050: %.2f" % (pop / 1000000))


def rmsd(n, years, val, a, b):
    residual_sum = 0
    if n == 1:
        residual_sum = sum(map(lambda x: pow(x[1] - (a * x[0] + b), 2), zip(years, val)))
        # for i in range(0, len(years)):
        #     y_circumflex = a * years[i] + b
        #     residual = pow(val[i] - y_circumflex, 2)
        #     residual_sum += residual
    else:
        residual_sum = sum(map(lambda x: pow(x[1] - ((x[0] - b) / a), 2), zip(years, val)))
        # for i in range(0, len(years)):
        #     x_circumflex = (years[i] - b) / a
        #     residual = pow(val[i] - x_circumflex, 2)
        #     residual_sum += residual
    return sqrt(residual_sum / (len(years)))


def ax_b(years, val):
    year_sum = sum(years)
    year_2_sum = sum(map(lambda x: x * x, years))
    pop_sum = sum(val)
    pop_year_sum = sum(map(lambda x: x[0] * x[1], zip(years, val)))
    b = (pop_sum * year_2_sum - year_sum * pop_year_sum) / (len(years) * year_2_sum - pow(year_sum, 2))
    a = (len(years) * pop_year_sum - year_sum * pop_sum) / (len(years) * year_2_sum - pow(year_sum, 2))
    return a, b


def ay_b(years, val):
    year_sum = sum(years)
    pop_2_sum = sum(map(lambda x: x * x, val))
    pop_sum = sum(val)
    pop_year_sum = sum(map(lambda x: x[0] * x[1], zip(years, val)))
    b = (year_sum * pop_2_sum - pop_sum * pop_year_sum) / (len(years) * pop_2_sum - pow(pop_sum, 2))
    a = (len(years) * pop_year_sum - pop_sum * year_sum) / (len(years) * pop_2_sum - pow(pop_sum, 2))
    return a, b

