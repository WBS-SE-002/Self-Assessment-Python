"""Pytest suite for the self‑assessment."""
import pytest
from src.student_functions import (
    add, fibonacci, is_prime, reverse_string, factorial, is_palindrome,
    find_max, celsius_to_fahrenheit, fahrenheit_to_celsius, is_even,
    sum_list, count_vowels, remove_duplicates, find_min, power,
    is_leap_year, calculate_average, string_length, concat_list_of_strings,
    get_unique_elements
)

# ----------------------------------------------------------------------
# add
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (2, 3, 5),
        (-4, 10, 6),
        (2.5, 0.5, 3.0),
        (100, -50, 50),
    ],
)
def test_add(a, b, expected):
    """Test cases for the add function."""
    assert add(a, b) == expected

# ----------------------------------------------------------------------
# fibonacci
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (8, [0, 1, 1, 2, 3, 5, 8, 13]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ],
)
def test_fibonacci(n, expected):
    """Test cases for the fibonacci function."""
    assert fibonacci(n) == expected

# ----------------------------------------------------------------------
# is_prime
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (23, True),
        (97, True),
        (100, False),
    ],
)
def test_is_prime_basic(n, expected):
    """Test cases for the is_prime function with valid inputs."""
    assert is_prime(n) == expected


def test_is_prime_negative():
    """Test that is_prime raises ValueError for negative inputs."""
    with pytest.raises(ValueError):
        is_prime(-1)
    with pytest.raises(ValueError):
        is_prime(-100)

# ----------------------------------------------------------------------
# reverse_string
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "s,expected",
    [
        ("", ""),
        ("a", "a"),
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("madam", "madam"),
        ("A B C", "C B A"),
    ],
)
def test_reverse_string(s, expected):
    """Test cases for the reverse_string function."""
    assert reverse_string(s) == expected

# ----------------------------------------------------------------------
# factorial
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (7, 5040),
    ],
)
def test_factorial_basic(n, expected):
    """Test cases for the factorial function with valid non-negative inputs."""
    assert factorial(n) == expected


# ----------------------------------------------------------------------
# is_palindrome
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "s,expected",
    [
        ("", True),
        ("a", True),
        ("madam", True),
        ("racecar", True),
        ("hello", False),
        ("Python", False),
    ],
)
def test_is_palindrome(s, expected):
    """Test cases for the is_palindrome function."""
    assert is_palindrome(s) == expected

# ----------------------------------------------------------------------
# find_max
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([1, 2, 3, 4, 5], 5),
        ([-1, -5, -2], -1),
        ([7], 7),
        ([3.14, 2.71, 1.618], 3.14),
        ([0, 0, 0], 0),
        ([10, 1, 100, 5], 100),
    ],
)
def test_find_max(numbers, expected):
    """Test cases for the find_max function."""
    assert find_max(numbers) == expected


def test_find_max_empty_list():
    """Test find_max with an empty list should raise ValueError."""
    with pytest.raises(ValueError):
        find_max([])

# ----------------------------------------------------------------------
# celsius_to_fahrenheit
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "celsius,expected",
    [
        (0, 32.0),
        (100, 212.0),
        (25, 77.0),
        (-10, 14.0),
        (37, 98.6),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    """Test cases for the celsius_to_fahrenheit function."""
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)

# ----------------------------------------------------------------------
# fahrenheit_to_celsius
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "fahrenheit,expected",
    [
        (32, 0.0),
        (212, 100.0),
        (77, 25.0),
        (14, -10.0),
        (98.6, 37.0),
    ],
)
def test_fahrenheit_to_celsius(fahrenheit, expected):
    """Test cases for the fahrenheit_to_celsius function."""
    assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(expected)

# ----------------------------------------------------------------------
# is_even
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, True),
        (2, True),
        (1, False),
        (-4, True),
        (-3, False),
    ],
)
def test_is_even(n, expected):
    """Test cases for the is_even function."""
    assert is_even(n) == expected

# ----------------------------------------------------------------------
# sum_list
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([], 0),
        ([1], 1),
        ([1, 2, 3], 6),
        ([-1, 0, 1], 0),
        ([1.5, 2.5, 3.0], 7.0),
    ],
)
def test_sum_list(numbers, expected):
    """Test cases for the sum_list function."""
    assert sum_list(numbers) == pytest.approx(expected)

# ----------------------------------------------------------------------
# count_vowels
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "s,expected",
    [
        ("", 0),
        ("a", 1),
        ("hello", 2),
        ("Python", 1),
        ("AEIOUaeiou", 10),
        ("Rhythm", 0),
    ],
)
def test_count_vowels(s, expected):
    """Test cases for the count_vowels function."""
    assert count_vowels(s) == expected

# ----------------------------------------------------------------------
# remove_duplicates
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "items,expected",
    [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 2, 3, 1], [1, 2, 3]),
        (["a", "b", "a", "c"], ["a", "b", "c"]),
        ([1, 1, 1, 1], [1]),
    ],
)
def test_remove_duplicates(items, expected):
    """Test cases for the remove_duplicates function."""
    assert remove_duplicates(items) == expected

# ----------------------------------------------------------------------
# find_min
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([1, 2, 3, 4, 5], 1),
        ([-1, -5, -2], -5),
        ([7], 7),
        ([3.14, 2.71, 1.618], 1.618),
        ([0, 0, 0], 0),
        ([10, 1, 100, 5], 1),
    ],
)
def test_find_min(numbers, expected):
    """Test cases for the find_min function."""
    assert find_min(numbers) == expected


def test_find_min_empty_list():
    """Test find_min with an empty list should raise ValueError."""
    with pytest.raises(ValueError):
        find_min([])

# ----------------------------------------------------------------------
# power
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "base,exponent,expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (10, 1, 10),
        (2, 0, 1),
        (3, 2, 9),
        (2.5, 2, 6.25),
    ],
)
def test_power(base, exponent, expected):
    """Test cases for the power function."""
    assert power(base, exponent) == pytest.approx(expected)


def test_power_negative_exponent():
    """Test that power raises ValueError for negative exponents."""
    with pytest.raises(ValueError):
        power(2, -1)
    with pytest.raises(ValueError):
        power(5, -3)

# ----------------------------------------------------------------------
# is_leap_year
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "year,expected",
    [
        (2000, True),
        (2004, True),
        (1900, False),
        (2001, False),
        (1600, True),
    ],
)
def test_is_leap_year(year, expected):
    """Test cases for the is_leap_year function."""
    assert is_leap_year(year) == expected

# ----------------------------------------------------------------------
# calculate_average
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([1, 2, 3], 2.0),
        ([10, 20, 30], 20.0),
        ([5], 5.0),
        ([-1, 0, 1], 0.0),
        ([1.0, 2.0, 3.0, 4.0], 2.5),
    ],
)
def test_calculate_average(numbers, expected):
    """Test cases for the calculate_average function."""
    assert calculate_average(numbers) == pytest.approx(expected)


def test_calculate_average_empty_list():
    """Test calculate_average with an empty list should raise ValueError."""
    with pytest.raises(ValueError):
        calculate_average([])

# ----------------------------------------------------------------------
# string_length
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "s,expected",
    [
        ("", 0),
        ("a", 1),
        ("hello", 5),
        ("Python", 6),
        ("  spaces  ", 10),
        ("12345", 5),
    ],
)
def test_string_length(s, expected):
    """Test cases for the string_length function."""
    assert string_length(s) == expected

# ----------------------------------------------------------------------
# concat_list_of_strings
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "strings,expected",
    [
        ([], ""),
        (["a"], "a"),
        (["hello", " ", "world"], "hello world"),
        (["Python", "is", "fun"], "Pythonisfun"),
        (["", "test", ""], "test"),
    ],
)
def test_concat_list_of_strings(strings, expected):
    """Test cases for the concat_list_of_strings function."""
    assert concat_list_of_strings(strings) == expected

# ----------------------------------------------------------------------
# get_unique_elements
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    # Use sorted expected for comparison as order might not be preserved
    "items,expected_sorted",
    [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 2, 3, 1], [1, 2, 3]),
        (["a", "b", "a", "c"], ["a", "b", "c"]),
        ([1, 1, 1, 1], [1]),
    ],
)
def test_get_unique_elements(items, expected_sorted):
    """Test cases for the get_unique_elements function."""
    # Convert to set for comparison as order is not guaranteed for unique elements
    assert sorted(get_unique_elements(items)) == sorted(expected_sorted)
