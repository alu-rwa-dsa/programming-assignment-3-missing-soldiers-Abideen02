# Write your code here
# Here are my number of barriers
T_Barriers = int(input())
barriers = []
for i in range(T_Barriers):
    x, y, d = map(int, input().strip().split())
    barriers.append((x, x + d))
#  here we are sorting the barriers
barriers.sort()
#and here we are initializing blocked ants counter
Ants = ba_point = 0
for barrier in barriers:
    if barrier[0] >= ba_point:
        ba_point = barrier[0]
        if ba_point < barrier[1]:
            Ants += (barrier[1] - ba_point) + 1
            ba_point = barrier[1] + 1
    elif ba_point <= barrier[1]:
        Ants += (barrier[1] - ba_point) + 1
        ba_point = barrier[1] + 1

print(Ants)