class decorator_class(object):
    def __init__(self,original_function):
        self.original_function = original_function
    def __call__(self, *args, **kwargs):
        print('call executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print("Original function executed")

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments {} and {}'.format(name,age))


display()
display_info('John',22)