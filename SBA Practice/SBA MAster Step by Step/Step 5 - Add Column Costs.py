# Step 5

costCols = [4, 1, 7, 3]

ans = 0

for i in range(0, 3):
    print("Visiting Column", i)
    ans += costCols[i]
    print("Current Cost =", ans)

print("Final Cost =", ans)