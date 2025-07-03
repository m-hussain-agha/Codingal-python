def check_exam_eligibility(age, education_level):
    # Check if the user meets the age requirement
    if age < 18:
        return "You are not eligible to take the exam because you are under 18."
    
    # Check if the user has completed high school
    if education_level.lower() != "high school":
        return "You are not eligible to take the exam because you have not completed high school."
    
    return "You are eligible to take the exam."

# Get user input
try:
    user_age = int(input("Enter your age: "))
    user_education = input("Enter your highest level of education (e.g., High School, Bachelor's, etc.): ")

    # Check eligibility
    eligibility_message = check_exam_eligibility(user_age, user_education)
    print(eligibility_message)

except ValueError:
    print("Please enter a valid age.")
