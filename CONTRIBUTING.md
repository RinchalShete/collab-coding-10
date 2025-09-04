# Contributing Guidelines

## Project Theme
All contributors will add one **Math Utility Function**.  
Examples (choose a unique one different from others):  
- Prime checker  
- Factorial calculator  
- Greatest Common Divisor (GCD)  
- Fibonacci sequence generator  
- Armstrong number checker  
- Any other simple math function  

Each function must be:  
- Written clearly with proper docstring  
- Tagged with **Author: <Your Name/GitHub Handle>**  
- Accompanied by a unit test in `/tests/`  

---

## Branching
- Create new branches as: `feature/<short-name>`  
  - Example: `feature/prime-checker`  
- Never push directly to `main`.

## Commit Messages
Follow a simple convention:  
- `feat: add prime checker`  
- `test: add tests for prime checker`  
- `docs: update README with usage instructions`

## Code Style & Docstrings
- Keep code simple and readable.  
- Each function must include a docstring with:  
  - **Description**  
  - **Parameters**  
  - **Returns**  
  - **Author: <Your Name/GitHub Handle>**

## Tests
- Each function must have a matching test file in `/tests/`.  
  - Example: `src/prime.py` → `tests/test_prime.py`  
- Use Python’s built-in `unittest` framework (easy to run for everyone).

## Pull Requests
- Open PRs to `main`.  
- Each PR must:  
  - Have at least **1 approving review** from a teammate.  
  - Pass all tests.  
- Keep PRs focused (one function + its test per PR).  

## Merging
- Only the **Admin/Integrator** merges PRs into `main`.  
- A PR requires at least **1 peer approval** before merge.  
- Contributors must resolve merge conflicts with help from the admin.  

## Definition of Done
- Code runs without errors.  
- Unit tests pass.  
- Function includes **Author tag**.  
- README updated if usage changes.  
