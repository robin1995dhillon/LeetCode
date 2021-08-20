def numRescueBoats(people, limit):
    people.sort()  # O(N)
    print(people)
    left = 0
    right = len(people) - 1
    boats = 0
    while left <= right:
        if left == right:
            boats += 1
            break
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            boats += 1
        else:
            right -= 1
            boats += 1

    print(boats)


limit = 3  # weight
people = [3, 2, 1, 2]
numRescueBoats(people, limit)
