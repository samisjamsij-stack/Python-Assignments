# Step 7

def minCost(initR, finalR, costRows):

    ans = 0

    for i in range(initR, finalR):
        ans += costRows[i]

    return ans

costRows = [5, 3, 2, 6]

result = minCost(1, 3, costRows)

print(result)