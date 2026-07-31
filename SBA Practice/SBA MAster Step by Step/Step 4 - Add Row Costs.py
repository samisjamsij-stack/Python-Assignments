# Step 4

costRows = [5, 3, 2, 6]

ans = 0

for i in range(1, 3):
    print("Visiting Row", i)
    ans += costRows[i]
    print("Current Cost =", ans)

print("Final Cost =", ans)