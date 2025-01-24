seats = [3,20,17,2,12,15,17,4,15,20]
students = [10,13,14,15,5,2,3,14,3,18]
count=0
seats.sort()
students.sort()
for i in range (len(students)):
    if students[i] !=seats[i]:
        if (students[i]+1)==seats[i] or (students[i]-1)==seats[i]:
            count+=1
        else:
            if seats[i]>students[i]:
                a=seats[i]-students[i]
                count+=a
            else:
                a=students[i]-seats[i]
                count+=a 
print(count)

