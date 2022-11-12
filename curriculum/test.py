# print("Hello World!")
#print("Ko Paing is here!")

## Simple closure function
def outer(outer_arg):
    """
    A function factory
    """
    def inner(inner_arg):
        """
        Produced function 
        """
        return inner_arg + outer_arg
    return inner

if __name__ == "__main__":
    f10 = outer(10)
    f10(5)
    print(f10.__closure__)
    print(f10.__closure__[0].cell_contents)
    
    f20 = outer(20)
    f20(5)