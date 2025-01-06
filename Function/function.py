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


print(my_first_function(15,30))
print(my_first_function(30,10))