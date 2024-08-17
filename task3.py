import re

def assess_password_strength(password):
    strength = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password) is not None,
        "lowercase": re.search(r'[a-z]', password) is not None,
        "numbers": re.search(r'\d', password) is not None,
        "special_characters": re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }

    # Assign points based on criteria
    if criteria["length"]:
        strength += 1
    if criteria["uppercase"]:
        strength += 1
    if criteria["lowercase"]:
        strength += 1
    if criteria["numbers"]:
        strength += 1
    if criteria["special_characters"]:
        strength += 1

    # Determine the strength level
    if strength == 5:
        strength_level = "Very Strong"
    elif strength == 4:
        strength_level = "Strong"
    elif strength == 3:
        strength_level = "Moderate"
    elif strength == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    return {
        "strength_level": strength_level,
        "criteria": criteria
    }

# Example usage
password = input("Enter your password: ")
result = assess_password_strength(password)
print(f"Password Strength: {result['strength_level']}")
print("Criteria Met:")
for criterion, met in result["criteria"].items():
    print(f"  {criterion.capitalize()}: {'Yes' if met else 'No'}")
