def safe_divide(numerator, denominator):
    """
    Safely divide numerator by denominator.

    Accepts numeric values or strings that can be converted to float.
    Returns a string message with result or an error message:
      - "Error: Please enter numeric values only."
      - "Error: Cannot divide by zero."
      - "The result of the division is <result>"
    """
    # Convert inputs to floats (handle non-numeric input)
    try:
        num = float(numerator)
        den = float(denominator)
    except (ValueError, TypeError):
        return "Error: Please enter numeric values only."

    # Check for zero denominator
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
