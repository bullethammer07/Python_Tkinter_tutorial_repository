class c1:
    def my_method(self):
        print(f"This is method inside c1")

class c2(c1):
    def my_method(self):
        print(f"This is method inside c2")

c1_i = c1()
c2_i = c2()

c1_i.my_method()
c2_i.my_method()