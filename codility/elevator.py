def solution(A, B, M, X, Y):
    # write your code in Python 2.7
    # print (A, B, M, X, Y)
    n = len(A)
    tot_weight = 0
    temp_weight = 0
    limit_reached = False
    person_count = 0
    while A:
        for person in A:
            temp_weight = tot_weight
            tot_weight = tot_weight + person
            person_count += 1
            # print("round"+str(person_count))
            print(A)
            # print(tot_weight)
            # print(person_count)
            if (tot_weight >= Y) or (len(A)==1):
                limit_reached = True
            if (limit_reached == True) and (person_count-1 <= X):
                print("gotin")
                print(B[:person_count-1])
                print(temp_weight)
                del A[:person_count-1]
                limit_reached = False
                tot_weight = 0
                person_count = 0
                print(A)




    # pass
def get_passengers(A,B,M,X,Y):
    person_count = 0
    n = len(A)
    tot_weight = 0
    temp_weight = 0
    limit_reached = False
    for i in range(0,n):
        temp_weight = tot_weight
        tot_weight = tot_weight + A[i]
        person_count += 1
        print("round "+str(i))
        print(tot_weight)
        if (i == n-1):
            print("\nlast item")
            print("total weigh - V")
            print(tot_weight)
            break
        if (person_count == 2) and (tot_weight <= Y):
            print("\ngotin pcount")
            print("total weigh - V")
            print(tot_weight)
            print(person_count)
            tot_weight = 0
            temp_weight = 0
            person_count = 0

        if (tot_weight <= Y) and (tot_weight + A[i+1] > Y):
            print("\ngotin")
            print("total weigh - V")
            print(tot_weight)
            print(person_count)
            tot_weight = 0
            temp_weight = 0
            person_count = 0
        elif (tot_weight <= Y) and (person_count-1 < X):
            print("\ngotin 2")
            print("total weigh - V")
            print(tot_weight)
            print(person_count)
            tot_weight = 0
            temp_weight = 0
            person_count = 0




A = [60,80,40,56,79,10,23,39]
B = [2,3,4]
M = 5
X = 2
Y = 150

print (get_passengers(A,B,M,X,Y))
