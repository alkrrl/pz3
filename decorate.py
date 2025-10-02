import time
import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Вызвана функция {func.__name__} с аргументами {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} выполнилась за {end - start:.6f} сек")
        return result
    return wrapper


def validate_range(min_value, max_value):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(x):
            if x < min_value or x > max_value:
                raise ValueError(f"Значение {x} вне допустимого диапазона [{min_value}, {max_value}]")
            return func(x)
        return wrapper
    return decorator
