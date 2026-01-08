
import asyncio
from typeguard import typechecked
from pydantic import validate_call
from common import DateTimeProvider, AppSettings


# EXAMPLE 1: Missing Argument and Return Types
# Ruff will trigger: ANN001 (missing arg type) and ANN201 (missing return type)
# Mypy will trigger: "Function is missing a type annotation"
@validate_call
def greet(name: str):

    print(f"hello {name}")
    return f"Hello, {name}"
# EXAMPLE 2: Incomplete/Incorrect Types
# Ruff will trigger: ANN201 (missing return type)
# Mypy will trigger: "Function is missing a return type annotation"
# AND "Incompatible return value" (it expects a return but finds None)
# @typechecked


def add_numbers(a: int, b: int):
    result = a + b
    print(f"The result is {result}")
    # Error: We forgot to return the value and didn't annotate '-> int'


async def main():

    print("dasdas")

# await main()
asyncio.run(main())
greet('1223')
print("hello wordl")
print(DateTimeProvider().today())
print(AppSettings().external_api_base_url)
