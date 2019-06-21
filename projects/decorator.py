class NonFlask():
    def __init__(self):
        self.routes = {}
    
    def route(self, route_str):
        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

    def server(self, path):
        func = self.routes.get(path)
        if func:
            return func()
        else:
            raise ValueError('Route {} has not been registered'.format(path))

app = NonFlask()

@app.route('/')
def hello():
    return "Hello Decorator!"


print("Call hello: " + hello())
print(app.server("/"))