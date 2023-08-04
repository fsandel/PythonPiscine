def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print (f'List : {type(object)}')
    elif isinstance(object, tuple):
        print (f'Tuple : {type(object)}')
    elif isinstance(object, set):
        print (f'Set : {type(object)}')
    elif isinstance(object, dict):
        print (f'Dict : {type(object)}')
    elif isinstance(object, str):
        print (f'Brian is in the kitchen : {type(object)}')
    else:
        print ('Type not found')
    return 42


# $>python tester.py | cat -e
# List : <class 'list'>$
# Tuple : <class 'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# Brian is in the kitchen : <class 'str'>$
# Type not found$
# 42$