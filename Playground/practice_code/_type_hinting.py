from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Set
from typing import Tuple

x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"

# For collections, the name of the type is capitalized, and the
# name of the type inside the collection is in brackets
x: List[int] = [1]
x: Set[int] = {6, 7}

# Same as above, but with type comment syntax
x = [1]  # type: List[int]

# For mappings, we need the types of both keys and values
x: Dict[str, float] = {'field': 2.0}

# For tuples of fixed size, we specify the types of all the elements
x: Tuple[int, str, float] = (3, "yes", 7.5)

# For tuples of variable size, we use one type and ellipsis
x: Tuple[int, ...] = (1, 2, 3)


# This is how you annotate a function definition
def stringify(num: int) -> str:
    return str(num)


# And here's how you specify multiple arguments
def plus(num1: int, num2: int) -> int:
    return num1 + num2


# Add default value for an argument after the type annotation
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float


# This is how you annotate a callable (function) value
x: Callable[[int, float], float] = f


# A generator function that yields ints is secretly just a function that
# returns an iterator of ints, so that's how we annotate it
def g(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


# An argument can be declared positional-only by giving it a name
# starting with two underscores:
def quux(__x: int) -> None:
    pass
