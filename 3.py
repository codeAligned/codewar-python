def tickets(people):
    print(people)
    print(123)
    count25 = 0
    count50 = 0
    count100 = 0
    for i in people:
        if i == 25:
            count25 += 1
        elif i == 50:
            count50 += 1
            count25 -= 1
        elif i == 75:
            count25 += 1
        elif i == 100:
            count100 += 1
            if count50 > 0:
                count25 -= 1
                count50 -= 1
            else:
                count25 -= 3
        elif i == 125:
            count25 += 1
        elif i == 150:
            count50 += 1
            count25 -= 1
        elif i == 175:
            count25 += 1
        if count100 < 0 or count50 < 0 or count25 < 0:
            return "NO"
    return 'YES'


