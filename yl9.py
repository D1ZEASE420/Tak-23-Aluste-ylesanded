a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("See ei ole kolnurk")
elif a == b and b==c:
    print("võrdkülgne kolmnurk")
elif a == b and b != c or a == c and a != b or b == c and b != a:
    print("võrdhaarne kolmnurk")
else:
    print("erikülgne kolmnurk")