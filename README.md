# Codingchallenge

# 📦 Package Sorter

A simple Python utility to classify packages as `STANDARD`, `SPECIAL`, or `REJECTED` based on their volume and mass.

## 🔧 Sorting Rules

The classification of a package depends on two main criteria:

### Bulky
- A package is **bulky** if:
  - Its **volume** (`width * height * length`) is **≥ 1,000,000 cm³**, or
  - Any **dimension** (width, height, length) is **≥ 150 cm**

### Heavy
- A package is **heavy** if:
  - Its **mass** is **≥ 20 kg**

### Dispatch Stacks
- `STANDARD`: Not bulky **and** not heavy
- `SPECIAL`: Bulky **or** heavy
- `REJECTED`: Bulky **and** heavy

## 🚀 Usage

1. Clone the repository or copy `sorter.py` into your project.
2. Import and use the `sort` function:

```python
from sorter import sort

print(sort(100, 100, 100, 10))   # STANDARD
print(sort(160, 50, 50, 10))     # SPECIAL (bulky)
print(sort(100, 100, 100, 25))   # SPECIAL (heavy)
print(sort(160, 160, 160, 25))   # REJECTED (both)