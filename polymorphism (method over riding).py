class A:
    def show(self):
        print("Show From Class A: ")
class B(A):
    def show(self):
        super() .show()
        print("Show From Class B: ")
class C(B):
    def show(self):
        super() .show()
        print("Show From Class C: ")

c1=C()
c1.show()

# new programme:

class A:
    def show(self):
        print("Show From Class A: ")
class B(A):
    def show(self):
        super() .show()
        print("Show From Class B: ")
class C(A):
    def show(self):
        super() .show()
        print("Show From Class C: ")
class D(B,C):
    def show(self):
        super() .show()
        print("Show From Class D: ")

d1=D()
d1.show()
