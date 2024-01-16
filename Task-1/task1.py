def solution(food, people):
    for start in range(len(food)):
        left = 0
        for i in range(len(food)):
            current = (start + i) % len(food)
            left+= food[current] - people[current]
            
            if left< 0:
                break
        else:
            return start
    return -1
#checing with the given test cases
food1 = [1, 2, 3, 4, 5]
people1 = [3, 4, 5, 1, 2]
output1 = solution(food1, people1)
print(output1)

food2 = [1, 2]
people2 = [5, 6]
output2 = solution(food2, people2)
print(output2)
