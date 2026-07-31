# Step 6

def minCost():

    costRows = [5, 3, 2, 6]

    ans = 0

    for i in range(1, 3):
        ans += costRows[i]

    print(ans)

minCost()