def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                print("Warn: %s is running" % func.__name__)
            elif level == "info":
                print("Info: %s is running" % func.__name__)
            return func(*args)
        return wrapper
    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()