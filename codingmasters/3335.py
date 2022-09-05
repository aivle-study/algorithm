from typing import List, Tuple

def sosuzum(n: int, m: int = 1, limit: int = 0) -> Tuple[int, List[int], List[int]]:
    q = m // n
    m = (m % n) * 10

    divivi = m
    divivi_list = []
    digit_list = []

    while True:
        if divivi in divivi_list:
            break
        divivi_list.append(divivi)
        digit = divivi // n
        divivi = (divivi % n) * 10
        digit_list.append(digit)

    idx = divivi_list.index(divivi)


    non_cyc = digit_list[:idx]
    cyc = digit_list[idx:]
    return q, non_cyc, cyc


def sosuzum_repr(n: int, m: int = 1, limit: int = 0) -> str:

    q, non_cyc, cyc = sosuzum(n, m, limit)
    s = f"{q}." + "".join(map(str, non_cyc)) + "{" + "".join(map(str, cyc)) + "}"

    return s

a,b=input().split()
a,b=int(a),int(b)
arr=sosuzum_repr(b,a)

if arr.count('{0}')==1:
    print(a/b)
else:
    print(arr)