# EX1.Create function to sum numbers in array [1,2,3,4,5,6]
def sum(number):
    sum = 0
    for i in range(len(number)):
        if number[i] !=",":
            sum += int(number[i])
    return sum
number_input = input("enter number: ")
print(sum(number_input))








