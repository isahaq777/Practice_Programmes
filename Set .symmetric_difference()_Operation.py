#Your task is to find the total number of people who have use to either the English or the French newspaper but not both.
n1,s1=input("Enter the number of students who have subscribed to the English newspaper: "),set(input("Enter the space separated list of student roll numbers who have subscribed to the English newspaper: ").split())
n2,s2=input("ENter the number of students who have subscribed to the French newspaper: "),set(input("Enter the space separated list of student roll numbers who have subscribed to the French newspaper: ").split())
print(len(s1.symmetric_difference(s2)))