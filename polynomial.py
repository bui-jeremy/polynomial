class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, value):
        return value

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - ( " + repr(self.p2) + " )"

    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            repr_p1 = "( " + repr(self.p1) + " )"
        else:
            repr_p1 = repr(self.p1)

        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            repr_p2 = "( " + repr(self.p2) + " )"
        else:
            repr_p2 = repr(self.p2)

        return repr_p1 + " * " + repr_p2

    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"

    def evaluate(self, value):
        if self.p2.evaluate(value) == 0:
            raise ValueError("Division by zero is not allowed")
        return self.p1.evaluate(value) / self.p2.evaluate(value)

poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print("Polynomial Representation:", poly)
print("Polynomial Evaluation for X = -1:", poly.evaluate(-1))

div_by_zero = Div(Int(1), Int(0))
print("1 / 0:", div_by_zero.evaluate(0))

