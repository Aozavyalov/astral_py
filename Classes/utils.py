def check_value(val, val_type, val_name, condition=True):
    if not (isinstance(val, val_type) and condition):
        raise ValueError(f"{val_name} can't be {val}!")

def check_int_args(method):
    def wrapper(self, *args, **kwargs):
        for i, a in enumerate(args):
            check_value(a, int, f'{i} argument', a > 0)
        for k in kwargs:
            check_value(kwargs[k], int, k, kwargs[k] > 0)
        return method(self, *args, **kwargs)
    return wrapper
