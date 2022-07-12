import redis


def cache_function_redis(host, port, password):
    def cache_function(func):
        def wrapper(*args, **kwargs):
            r = redis.StrictRedis(
                host=host,
                port=port,
                password=password,
                charset="utf-8",
                decode_responses=True
            )
            value = r.get(f'{args, kwargs}')
            if value is not None:
                return value
            result = func(*args, **kwargs)
            r.set(f'{args, kwargs}', result)
            return result

        return wrapper

    return cache_function


@cache_function_redis('redis-15856.c300.eu-central-1-1.ec2.cloud.redislabs.com', 15856,
                      'FCpiNZMfHObWD9nMJ23DdbdR0PxMd6SO')
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(6))
    print(multiplier(12))
