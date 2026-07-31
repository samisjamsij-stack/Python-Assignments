def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):

    ans = 0

    # Make sure rows go from smaller to larger
    if initR > finalR:
        initR, finalR = finalR, initR

    # Make sure columns go from smaller to larger
    if initC > finalC:
        initC, finalC = finalC, initC

    # Add row costs
    for i in range(initR, finalR):
        ans += costRows[i]

    # Add column costs
    for i in range(initC, finalC):
        ans += costCols[i]

    return ans


# Example Data
rows = 4
cols = 4

costRows = [5, 3, 2, 6]
costCols = [4, 1, 7, 3]

result = minCost(
    rows,
    cols,
    1,   # Start Row
    0,   # Start Column
    3,   # End Row
    2,   # End Column
    costRows,
    costCols
)

print("Minimum Cost =", result)