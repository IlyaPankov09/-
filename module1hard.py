grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list= list(students)
students_list = sorted(students_list)
print(students_list)
print(len(students)) # вычислил длину списка
set0= (sum(grades[0])/(len(grades[0])))
set1= (sum(grades[1])/(len(grades[1])))
set2= (sum(grades[2])/(len(grades[2])))
set3= (sum(grades[3])/(len(grades[3])))
set4= (sum(grades[4])/(len(grades[4])))
print(set0, set1, set2, set3, set4)
class_list = {(students_list[0]):set0, (students_list[1]):set1,(students_list[2]):set2,
              (students_list[3]):set3, (students_list[4]):set4}
print(class_list)




