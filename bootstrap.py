from types import GeneratorType

def bootstrap(f, stack=[]):
    def g(*a, **kw):
        if stack: return f(*a, **kw)
        to = f(*a, **kw)
        while True:
            if type(to) is GeneratorType:
                stack.append(to); to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return g
