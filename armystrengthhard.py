cases = int(input())
out = []
for i in range(0, cases):
    input()
    armyS = list(map(int, input().split())) 
    armyG = list(map(int, input().split()))
    armyG = sorted(armyG)
    armyM = list(map(int, input().split()))
    armyM = sorted(armyM)
    print("MechaGodzilla" if armyM[armyS[1]-1] > armyG[armyS[0]-1] else "Godzilla")
    
