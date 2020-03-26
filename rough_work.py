import inspect
import moment

x = moment.now().strftime("%d%m%y_%H%M%S")
print(x)

def whoami():
    return inspect.stack()[1][3]

def myFunc():
    print(whoami())

myFunc()


