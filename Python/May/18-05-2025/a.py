def add(a, b):
    print(a + b)

def add_v2(a, b, c):
    print(a + b + c)
print(__name__)


if __name__ == "__main__":
    # __name__ == "b": --> when i import a from file b
    # __name__ == "__main__": --> when i import a from file b 
    add(1, 2)
    add_v2(1, 3, 2)