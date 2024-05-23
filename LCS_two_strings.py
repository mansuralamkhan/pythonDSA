def lcs(x, y):
    m = len(x)
    n = len(y)

    dp = [[0] * (n+1) for _ in range(m+1)]

    traceback = [[0] * (n+1) for _ in range(m +1 )]

    for i in range(1, m + 1):
        for j in range(1, n +1):
            if x[i-1] == y[j-1]:
               dp[i][j] = dp[i-1][j-1] + 1
               traceback[i][j] = 1
            else:
                if dp[i -1][j] >= dp[i][j-1]:
                    dp[i][j] == dp[i - 1][j]
                    traceback[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1]
                    traceback[i][j] = 2

    lcs = ""
    i, j, = m, n
    while i > 0 and j > 0:
        if traceback[i][j] == 1:
            lcs = x[i-1] + lcs
            i -= 1
            j -= 1

        elif traceback[i][j] == 0:
            i -= 1
        else:
            j -= 1
    return lcs

string1 = "ABC"
string2 = "BCDGEAGAGAG"

print("LCS:", lcs(string1, string2))