def f1()-> None:
    a = [(str(i), str(2*i)) for i in range(0, 10)]

    print(a)

    print(list(int(i[1]) for i in a))

def f2() -> None:
    from timeit import timeit
    from operator import itemgetter

    a = [(str(i), str(2*i)) for i in range(100_000)]

    t1 = timeit(
        lambda: [int(y) for _, y in a],
        number=100
    )

    t2 = timeit(
        lambda: list(map(lambda i: int(i[1]), a)),
        number=100
    )

    t3 = timeit(
            lambda: list(map(int, map(itemgetter(1),a))),
            number=100
        )

    print(f"List comprehension: {t1:.4f} s")
    print(f"Map + lambda:       {t2:.4f} s")
    print(f"Map + function:     {t3:.4f} s")

def f3() -> None:
    from timeit import repeat
    from operator import itemgetter

    a = [(str(i), str(2*i)) for i in range(100_000)]

    tests = {
        "List comprehension": lambda: [int(y) for _, y in a],
        "Map + lambda": lambda: list(map(lambda i: int(i[1]), a)),
        "Map + itemgetter": lambda: list(map(int, map(itemgetter(1), a))),
    }

    for name, func in tests.items():
        times = repeat(func, number=100, repeat=5)
        print(f"{name:22} {min(times):.4f} s")

f3()