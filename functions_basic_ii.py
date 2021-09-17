#Countdown
def countdown(number):
    resultado = []
    for i in range(number,-1,-1):
        resultado.append(i)
    return resultado

print(countdown(5))

#Print and return

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

#First plus length

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

#Values greater than second

def values_greater_than_second(num_list):
    if len(num_list)<2:
        return False
    else:
        new_list = []
        total=0
        for num in num_list:
                if num >num_list[1]:
                    total+=1
                    new_list.append(num)
        print(total)
        return new_list



print(values_greater_than_second([5,2,3,2,1,4]))

print(values_greater_than_second([3]))

#This Length, That Value

def length_and_value(size, value):
    vector = []
    for i in range(0,size):
        vector.append(value)
    return vector

print(length_and_value(4,7))
print(length_and_value(6,2))