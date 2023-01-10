def print_function_name(function):
    def new_function(*args, **kwargs):
        if '.' in __name__:
            modname = f"{__name__}".split('.')[1]
        else:
            modname = f"{__name__}"
        print(f'{modname}/{function.__name__}')
        
        ret = function(*args, **kwargs)
        return ret
    return new_function