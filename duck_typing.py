class Pycharm:
    def execute(self):
        print("Compiling")
        print("Suggestion")
        print("Spelling Check")
class Netbean:
    def execute(self):
        print("Intrepeter")
        print("Compiling")
class Laptop:
    def code(self,ide):
        ide.execute()


pythonide=Pycharm()
javaide=Netbean()
lap1=Laptop()
lap1.code(pythonide)
lap1.code(javaide)