# user defined function

# var1=11

# var2 =30

# output=(((var1*var2)*50)/100)*var1/var2

# print(output)


def my_first_function(var1,var2):
    """
    This is my first function

    parameters: None

    return: None
    """
    output=(((var1*var2)*50)/100)*var1/var2

    return output
##default and flexible fucntion
def calculate_circle_circumference(r,pi=3.14):
    output=2*pi*r
    return output

print(my_first_function(15,30))
print(my_first_function(30,10))
print(calculate_circle_circumference(7))


#flexible function

def calculate(size,weight,*args):
    print(len(args))
    output=size+weight
    return output

print(calculate(177,70))
print(calculate(177,70,7))
print(calculate(177,70,7,2))

#lambda function

def calculate_square(x):
    output=x*x
    return output

print(calculate_square(5))

result=lambda x:x*x


print(result(5))