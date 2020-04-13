#class style to get things from thing 
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff() #this is calling a function instantiate
thing.apple()
print(thing.tangerine) # does this rely on the self.tangerine?
