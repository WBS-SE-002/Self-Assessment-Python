"""Starter file for the self‑assessment.

Implement the functions below.  Do not change their names or arguments.
Feel free to add helper functions, but keep them inside this file.
"""
from typing import List, Any


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of *a* and *b*.

    >>> add(2, 3)
    5
    >>> add(2.5, 0.5)
    3.0
    """


def fibonacci(n: int) -> List[int]:
    """Return a list containing the first *n* Fibonacci numbers.

    For n <= 0, return an empty list.

    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    """



def is_prime(n: int) -> bool:
    """Return ``True`` if *n* is a prime number, else ``False``.

    ▸ Accepts only non‑negative integers (raise ``ValueError`` otherwise).
    ▸ 0 and 1 are not prime.

    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    """


def reverse_string(s: str) -> str:
    """Return the reverse of the input string *s*.

    >>> reverse_string("hello")
    "olleh"
    >>> reverse_string("Python")
    "nohtyP"
    """


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer *n*.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """


def is_palindrome(s: str) -> bool:
    """Return ``True`` if the string *s* is a palindrome, else ``False``.

    A palindrome is a word which reads the same backward as forward, ignoring capitalization.

    >>> is_palindrome("madam")
    True
    >>> is_palindrome("Racecar")
    True
    >>> is_palindrome("hello")
    False
    """


def find_max(numbers: List[int | float]) -> int | float:
    """Return the maximum number in a list of numbers.

    Raises ValueError if the list is empty.

    >>> find_max([1, 5, 2, 8])
    8
    >>> find_max([-10, -1, -5])
    -1
    """


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit.

    Formula: $F = C \times 9/5 + 32$

    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(25)
    77.0
    """


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius.

    Formula: $C = (F - 32) \times 5/9$

    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(77)
    25.0
    """


def is_even(n: int) -> bool:
    """Return ``True`` if *n* is an even number, else ``False``.

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    """


def sum_list(numbers: List[int | float]) -> int | float:
    """Calculate the sum of all numbers in a list.

    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([])
    0
    """


def count_vowels(s: str) -> int:
    """Count the number of vowels (a, e, i, o, u, case-insensitive) in a string.

    >>> count_vowels("hello")
    2
    >>> count_vowels("Python")
    1
    """


def remove_duplicates(items: List[Any]) -> List[Any]:
    """Remove duplicate elements from a list while preserving their original order.

    >>> remove_duplicates([1, 2, 2, 3, 1])
    [1, 2, 3]
    >>> remove_duplicates(["a", "b", "a", "c"])
    ["a", "b", "c"]
    """


def find_min(numbers: List[int | float]) -> int | float:
    """Return the minimum number in a list of numbers.

    >>> find_min([1, 5, 2, 8])
    1
    >>> find_min([-10, -1, -5])
    -10
    """


def power(base: int | float, exponent: int) -> int | float:
    """Calculate base raised to the power of exponent.
    Only accepts non-negative integer exponents.

    Raises ValueError for negative exponents.

    >>> power(2, 3)
    8
    >>> power(5, 0)
    1
    """


def is_leap_year(year: int) -> bool:
    """Check if a given year is a leap year.

    A year is a leap year if it is divisible by 4,
    unless it is divisible by 100 but not by 400.

    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2024)
    True
    """


def calculate_average(numbers: List[int | float]) -> float:
    """Calculate the average of numbers in a list.

    Raises ValueError if the list is empty.

    >>> calculate_average([1, 2, 3])
    2.0
    >>> calculate_average([10, 20, 30, 40])
    25.0
    """


def string_length(s: str) -> int:
    """Return the length of a string without using the built-in len() function.

    >>> string_length("hello")
    5
    >>> string_length("")
    0
    """


def concat_list_of_strings(strings: List[str]) -> str:
    """Concatenate a list of strings into a single string.

    >>> concat_list_of_strings(["hello", " ", "world"])
    "hello world"
    >>> concat_list_of_strings(["Python", "is", "fun"])
    "Pythonisfun"
    """


def get_unique_elements(items: List[Any]) -> List[Any]:
    """Get unique elements from a list. The order of elements in the returned list is not guaranteed.

    >>> sorted(get_unique_elements([1, 2, 2, 3, 1]))
    [1, 2, 3]
    >>> sorted(get_unique_elements(["a", "b", "a", "c"]))
    ["a", "b", "c"]

    """
