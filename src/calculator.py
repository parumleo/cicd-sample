"""Small example module used to demonstrate CI unit testing."""

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def calculate_total(unit_price: float, quantity: int, discount_percent: float = 0) -> float:
    """Calculate an order total after an optional percentage discount."""
    if unit_price < 0:
        raise ValueError("unit_price cannot be negative")
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    subtotal = unit_price * quantity
    return round(subtotal * (1 - discount_percent / 100), 2)
