# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]

def max_number(array):
    number = array[0]
    for i in range(len(array)):
        if array[i] > number:
            number = array[i]
    return number
max = [2,3,5,0,11,5,2]
print(max_number(max))


    
