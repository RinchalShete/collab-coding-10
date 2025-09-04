"""
Main driver file for Collaborative Coding Assignment
Theme: Math Utilities
"""

from armstrong import armstrongChecker
from factorial import factorial
from fibonacci import fibonacci
from gcd import gcd
from is_even import is_even


def main():
    while True:
        print("\n===== Collaborative Coding Driver Program =====")
        print("1. Check Armstrong Number")
        print("2. Factorial")
        print("3. Fibonacci (nth number)")
        print("4. GCD")
        print("5. Check Even/Odd")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if choice == 1:
            try:
                num = int(input("Enter a number: "))
                if armstrongChecker(num):
                    print(f"{num} is an Armstrong number ✅")
                else:
                    print(f"{num} is NOT an Armstrong number ❌")
            except (TypeError, ValueError) as e:
                print("Error:", e)

        elif choice == 2:
            try:
                n = int(input("Enter a number: "))
                print(f"Factorial of {n} = {factorial(n)}")
            except (TypeError, ValueError) as e:
                print("Error:", e)

        elif choice == 3:
            try:
                n = int(input("Enter the position (n): "))
                print(f"The {n}th Fibonacci number = {fibonacci(n)}")
            except ValueError as e:
                print("Error:", e)

        elif choice == 4:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print(f"GCD of {a} and {b} = {gcd(a, b)}")
            except ValueError as e:
                print("Error:", e)

        elif choice == 5:
            try:
                num = int(input("Enter a number: "))
                if is_even(num):
                    print(f"{num} is Even ✅")
                else:
                    print(f"{num} is Odd ❌")
            except TypeError as e:
                print("Error:", e)

        elif choice == 0:
            print("Exiting... 👋")
            break

        else:
            print("⚠️ Invalid choice, try again.")


if __name__ == "__main__":
    main()

