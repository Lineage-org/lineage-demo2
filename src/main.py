#!/usr/bin/env python3
"""
AcmeCorp Demo Application

This demonstrates NixLine configuration-driven consumption with:
- Custom EditorConfig (4 spaces for Python, 88 char line length)
- Custom CODEOWNERS (jasonodoom owns *.py files)
- Custom pre-commit hooks (black, flake8)
- Custom license (Apache-2.0 with NixLine Contributors)
"""

def calculate_factorial(n: int) -> int:
    """Calculate factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)


def greet_user(name: str = "World") -> str:
    """Generate a greeting message."""
    return f"Hello {name} from NixLine-org!"


def main() -> None:
    """Main application entry point."""
    print(greet_user("AcmeCorp Team"))
    print("Demonstrating NixLine configuration-driven consumption...")

    # Test the factorial function
    test_numbers = [0, 1, 5, 10]
    for num in test_numbers:
        result = calculate_factorial(num)
        print(f"Factorial of {num} is {result}")


if __name__ == "__main__":
    main()