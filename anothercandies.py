test_cases = int(input())
for _ in range(0, test_cases):
    input()
    kids = int(input())
    total = 0
    for i in range(kids):
        total += int(input())
    can_do = "YES" if total % kids == 0 else "NO"
    print(can_do)
