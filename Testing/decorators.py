def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Original function executed")

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments {} and {}'.format(name,age))


display()
display_info('John',22)


#decorator_display = decorator_function(display)

#print(decorator_display.__name__)
#decorator_display()