import time
from functools import wraps
from collections import OrderedDict

def cached(max_size=None, seconds=None):
    if not isinstance(max_size, int):
        max_size = None

    if not isinstance(seconds, int):
        seconds = None

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            now = time.time()

            if seconds is not None:
                keys_to_delete = [keys for keys, (_, time) in cache.items() if now - time > seconds]
                for keys in keys_to_delete:
                    del cache[keys]

            if key in cache:
                result, _ = cache[key]
                return result

            result = func(*args, **kwargs)
            cache[key] = (result, now)

            if max_size is not None:
                while len(cache) > max_size:
                    cache.popitem(last=False) 

            return result

        return wrapper

    return decorator


@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2

print(slow_function(2)) 
print(slow_function(2))
time.sleep(15)
print(slow_function(2))