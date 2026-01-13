# @validate_call
def greet(name: str) -> str:
    print(f"hello {name}")
    return f"Hello, {name}"


def add_numbers(a: int, b: int) -> None:
    result = a + b
    print(f"The result is {result}")
    # Error: We forgot to return the value and didn't annotate '-> int'


greet("1223")
