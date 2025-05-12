# It is clearly seen that self and obj is referring to the same object

class check_:
    def __init__(self):
        print("Address of self = ",id(self))

obj = check_()
print("Address of class object = ",id(obj))
