TESTS = [
    {
        "matrix": [["z", "y", "z"], ["w", "v", "w"], ["u", "t", "s"]],
        "result": "z,z,v,u,s"
    },
    {
        "matrix": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        "result": "1,4,6,7,10,11,13,16"
    }
]

def solution_a(m):
    width = len(m) - 1
    cursor = 0
    l = []
    forward = True

    for row in m:
        if cursor != width - cursor:
            cursors = [cursor, (width - cursor)]
            cursors.sort()
            l.append(row[cursors[0]])
            l.append(row[cursors[1]])
        else:
            l.append(row[cursor])

        cursor += 1

    return ','.join(map(lambda x: str(x), l))

def solution_b(m):
    def op(cursor, row):
        width = len(m) - 1
        if cursor != width - cursor:
            cursors = [cursor, (width - cursor)]
            cursors.sort()
            return '{},{}'.format(row[cursors[0]], row[cursors[1]])
        else:
            return str(row[cursor])

    value = list(map(op, range(0, len(m)), m))
    return ','.join(value)

for i in TESTS:
    for func in [ solution_a, solution_b ]:
        assert(func(i["matrix"]) == i["result"])

print("Passed")
