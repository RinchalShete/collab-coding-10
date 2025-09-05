# Collaborative Coding Project 
This repository is part of a collaborative coding assignment where team members contributed mathematical functions using GitHub workflows (branches, pull requests, reviews, and CI/CD for automated testing).

---

## Project Structure
collab-coding-10/
│
├── src/ # Source code for math functions
│ ├── armstrong.py
│ ├── factorial.py
│ ├── fibonacci.py
│ ├── gcd.py
│ ├── is_even.py
│ └── driver.py # Driver program for running all functions
│
├── tests/ # Unit tests for each function
│ ├── test_armstrong.py
│ ├── test_factorial.py
│ ├── test_fibonacci.py
│ ├── test_gcd.py
│ └── test_is_even.py
│
├── .github/workflows/ # CI/CD GitHub Actions
│ └── tests.yml
│
├── README.md # Project documentation
└── CONTRIBUTING.md # Report of contribution guidelines
└── Experience_Report.md # Report of contributions

---

## Functions Implemented
- **Factorial Calculator** – `factorial(n)`
- **Armstrong Number Checker** – `armstrongChecker(num)`
- **Greatest Common Divisor (GCD)** – `gcd(a, b)`
- **Even Number Checker** – `is_even(n)`
- **Fibonacci Generator** – `fibonacci(n)`

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/RinchalShete/collab-coding-10.git
   cd collab-coding-10
   ```
   
2. Run the driver program:
   ```bash
   python src/driver.py
   ```

---

## Running Tests

Unit tests are written using unittest. To run all tests:
```bash
python -m unittest discover tests
```
GitHub Actions (tests.yml) is set up to run these tests automatically on every push and pull request.

---

## Team Members

- [Shete Rinchal Sachin](https://github.com/RinchalShete) (22BCS114) – Factorial  
- [Samridh Ramesha](https://github.com/Rammstone) (22BCS107) – Armstrong  
- [Soumya Patil](https://github.com/SOUMYA122004) (22BCS123) – GCD  
- [Shashank Acharya](https://github.com/TheBlueGeneral) (22BCS113) – is_even  
- [Shivateja A Korvan](https://github.com/shivateja126) (22BCS117) – Fibonacci

---

## Key Features

- Collaborative workflow using branches + pull requests + reviews
- Automated testing via GitHub Actions
- Clean and modular code structure
- Driver program integrates all functions



