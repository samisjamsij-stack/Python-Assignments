# Step 8

def minCost(initR, initC, finalR, finalC, costRows, costCols):

    ans = 0

    for i in range(initR, finalR):
        ans += costRows[i]

    for i in range(initC, finalC):
        ans += costCols[i]

    return ans

costRows = [5, 3, 2, 6]
costCols = [4, 1, 7, 3]

answer = minCost(1, 0, 3, 2, costRows, costCols)

print(answer)