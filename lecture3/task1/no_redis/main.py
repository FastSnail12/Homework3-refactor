def cache_function(func):
    def wrapper(*args, **kwargs):
        for key in cache:
            if key == f'{args, kwargs}':
                return cache[key]
        result = func(*args, **kwargs)
        cache[f'{args, kwargs}'] = result
        return result

    cache = {}
    return wrapper


@cache_function
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    pass
