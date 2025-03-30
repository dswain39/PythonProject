def my_logger(orgi_func):

    import logging
    logging.basicConfig(filename='/home/dibya/PycharmProjects/PythonEssentials/Testing/{}.log'.format(orgi_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {} and kwargs: {}'.format(args, kwargs)
        )
        return orgi_func(*args, **kwargs)
    return wrapper

@my_logger
def display_info(name,age):
    print('display_info ran with arguments {} and {}'.format(name,age))

#display_info('Hank',40)
#display_info('Tom',99)
display_info('Alex',22)



