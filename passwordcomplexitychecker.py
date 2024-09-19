import re

def password_strength_checker(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*#?&]', password) is not None

    # Calculate the score based on criteria met
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback based on score
    if score == 5:
        feedback = "Strong Password"
    elif score == 4:
        feedback = "Moderately Strong Password"
    elif score == 3:
        feedback = "Weak Password"
    else:
        feedback = "Very Weak Password"

    # Provide tips for improvement
    tips = []
    if not length_criteria:
        tips.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        tips.append("Add at least one uppercase letter.")
    if not lowercase_criteria:
        tips.append("Add at least one lowercase letter.")
    if not number_criteria:
        tips.append("Add at least one number.")
    if not special_char_criteria:
        tips.append("Add at least one special character (e.g., @$!%*#?&).")

    return feedback, tips

# Example usage
password = input("Enter your password: ")
feedback, tips = password_strength_checker(password)

print("\nPassword Strength: " + feedback)
if tips:
    print("Suggestions for a stronger password:")
    for tip in tips:
        print("- " + tip)
