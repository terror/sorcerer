P, D = list(map(int, input().split()))

d = {}
for _ in range(P):
    i, A, B = list(map(int, input().split()))
    if i in d:
        d[i][0], d[i][1] = d[i][0] + A, d[i][1] + B
    else:
        d[i] = [A, B]

sA = sB = sV = 0
for key, val in sorted(d.items()):
    wA, wB, w, ans = val[0], val[1], ((val[0] + val[1]) // 2) + 1, ""
    sV += wA + wB
    if wA > wB:
        ans, wA = "A", val[0] - w
    else:
        ans, wB = "B", val[1] - w
    print("{} {} {}".format(ans, wA, wB))
    sA, sB = sA + wA, sB + wB

print("{:.10f}".format(abs(sA - sB) / sV))
