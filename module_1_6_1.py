grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron',}
res = sorted(students)
print(res)

average_score = {}

students_1 = sum(grades[0]) / len(grades[0])
students_2 = sum(grades[1]) / len(grades[1])
students_3 = sum(grades[2]) / len(grades[2])
students_4 = sum(grades[3]) / len(grades[3])
students_5 = sum(grades[4]) / len(grades[4])

average_score[res[0]] = students_1
average_score[res[1]] = students_2
average_score[res[2]] = students_3
average_score[res[3]] = students_4
average_score[res[4]] = students_5

print(average_score)