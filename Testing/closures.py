# def outer_func(msg):
#     message = msg
#     def inner_func():
#         print(message)
#     return inner_func
#
# hii_func = outer_func('Hii')
# hello_func = outer_func('Hello')
#
# hii_func()
# hello_func()



import logging
logging.basicConfig(filename='/home/dibya/PycharmProjects/PythonEssentials/Testing/example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(a, b):
    return a + b
def sub(a, b):
    return a - b

add_logger = logger(add)
sub_logger = logger(sub)

# add_logger(4,5)
# sub_logger(10,4)
def mul(a,b):
    return a * b
mul_logger = logger(mul)
mul_logger(5,4)