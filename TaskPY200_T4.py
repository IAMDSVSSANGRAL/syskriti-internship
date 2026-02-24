def check_password_strength(s: str) -> str:
    """
    Checks password strength based on rules:
    1. Length >= 8
    2. At least 1 digit
    3. At least 1 uppercase letter
    4. At least 1 lowercase letter
    Returns: "STRONG" or "WEAK"
    """

    # Rule 1: Length check
    if len(s) < 8:
        return "WEAK"

    has_digit = False
    has_upper = False
    has_lower = False

    # Check each character manually (First Principle)
    for ch in s:
        # Check digit
        if '0' <= ch <= '9':
            has_digit = True

        # Check uppercase
        elif 'A' <= ch <= 'Z':
            has_upper = True

        # Check lowercase
        elif 'a' <= ch <= 'z':
            has_lower = True

    # Final validation
    if has_digit and has_upper and has_lower:
        return "STRONG"
    else:
        return "WEAK"