import sys
sys.stdin = open("hps.in")
sys.stdout = open("hps.out", 'w')

n = int(input())
gestures = [input().strip() for _ in range(n)]
# print(gestures)

pfH, pfP, pfS = [0], [0], [0]
hC, pC, sC = 0, 0, 0
for i in range(n):
    if gestures[i] == 'H':
        hC += 1
    elif gestures[i] == 'P':
        pC += 1
    else:
        sC += 1
    pfH.append(hC)
    pfP.append(pC)
    pfS.append(sC)

# all solo
ans = max(hC, pC, sC)
for i in range(n):
    # h-p, h-s, ps | their reverses
    hp = pfH[i + 1] - pfH[0] + pfP[n] - pfP[i]
    ph = pfP[i + 1] - pfP[0] + pfH[n] - pfH[i]

    hs = pfH[i + 1] - pfH[0] + pfS[n] - pfS[i]
    sh = pfS[i + 1] - pfS[0] + pfH[n] - pfH[i]

    ps = pfP[i + 1] - pfP[0] + pfS[n] - pfS[i]
    sp = pfS[i + 1] - pfS[0] + pfP[n] - pfP[i]
    ans = max(ans, hp, ph, hs, sh, ps, sp)
print(ans)

'''
prefix sums
try all solo, then switching at each point
pf[R + 1] - pf[L], [L, R] inclusive
'''
