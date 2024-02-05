def things(*args):
    for arg in args:
        print(arg)


things('table', 'wheel', 'window', 'phone')


def things2(first_thing, *args):
    print(first_thing)
    print(args[0])
    for arg in args:
        print(arg)


things2('table', 'wheel', 'window', 'phone')


def attendance_list(school_class='1a', **kwargs):
    print('Class ' + school_class)
    for last_name in kwargs.keys():
        print(last_name)
    print(kwargs.get('Doe'))


attendance_list('1a', Doe=1, Smith=2, Brown=3)

