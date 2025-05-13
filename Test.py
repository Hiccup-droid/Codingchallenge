# sorter.py

def sort(width, height, length, mass):
    """
    Determines how a package should be dispatched based on its size and weight.

    Parameters:
    - width (int or float): Width in cm
    - height (int or float): Height in cm
    - length (int or float): Length in cm
    - mass (int or float): Mass in kg

    Returns:
    - str: "STANDARD", "SPECIAL", or "REJECTED" based on the rules
    """
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
