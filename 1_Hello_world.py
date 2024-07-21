class Helloworld:
    def __init__(self, message):
        self.message = message
    def method(self):
        print (self.message)
        

instance = Helloworld("Hello World")
instance.method()
