def solution():
    line = input().split()
    if int(line[0]) == 0:
        return None
    numCategories = int(line[1])
    takenCourses = input().split()
    answer = "yes"
    for i in range(numCategories):
        line = input().split()
        numCategoryCourses = int(line[0])
        categoryCreditsRequired = int(line[1])
        matches = 0
        for j in range(2, numCategoryCourses + 2):
            if line[j] in takenCourses:
                matches += 1
        if matches < categoryCreditsRequired:
            answer = "no"
    return answer

while True:
    response = solution()
    if not response:
        break
    print(response)
    
