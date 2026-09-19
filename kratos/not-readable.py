long_list_unreadable = [[[[i for i in range(j, k)] for j in range(20)] for k in range(20, 30)] for _ in range(10)]

long_list_readable = [
    [
        [
            [i for i in range(j, k)]
            for j in range(20)
        ]
        for k in range(20, 30)
    ]
    for _ in range(10)
]
