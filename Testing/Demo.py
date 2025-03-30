class Demo:
    def __init__(self):
        self.age = 10
        self.name = 'Brad'

obj = Demo()
print(obj.age)
print(obj.name)

print('\nGetattr : ', getattr(obj,'age','Not Found'))
setattr(obj,'mark',100)

print(obj.mark)


def cube(num):
    return num * num * num

def square(num):
    return num * num

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result
#
# squares = my_map
# print(squares(cube,[1,2,3,4,5]))

# def logger(msg):
#
#     def log_message():
#         print('Message:',msg)
#     return log_message
#
# log_hi= logger('hii')
# log_hi()

# def html_tag(tag):
#     def wrap_text(text):
#         print('\n<{0}>{1}</{0}>'.format(tag, text))
#     return wrap_text
#
# print_h = html_tag('h1')
# print_h('Hello')
#
# print_p = html_tag('p')
# print_p('This is a paragraph')
