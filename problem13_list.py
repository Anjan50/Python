# Retrieves the largest integer value from a provided list

from typing import Iterable


def get_largest(l: Iterable[int]) -> int:
    return max(l)


input_array = map(int, input().split())
print(f"Largest element: {get_largest(input_array)}")
