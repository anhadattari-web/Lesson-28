class myClass:
    __privateVar_=25;
    def _privMthd(self):
        print("I'm inside class myClass")
    def hello(self):
        print("Private variable value",myClass._privateVar)
foo=myClass()
foo.hello()
foo._privMthd
