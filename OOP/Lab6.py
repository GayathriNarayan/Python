# Complete this code so it works using decorators.


def even_number(function):
    def wrap(numbers):
        print([i for i in a if i % 2 == 0])
        function()
        print('After the function execution')
    return wrap

@even_number
def function_needs_decorator():
    print("Even numbers")

a = [1,2,3,4]
function_needs_decorator(a)

