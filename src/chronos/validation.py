# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

import functools


def class_property(*expected_argument_types):
    def validate(func):      
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            check = [type(args[-1]).__name__ == expected_argument_type for expected_argument_type in expected_argument_types]
            if not any(check):
                raise TypeError(f"arg {args[-1]} does not match {expected_argument_types}")
            return func(*args, **kwargs)
        return wrapper
    return validate