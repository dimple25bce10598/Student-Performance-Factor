# Simple Student Performance Factor Analyzer

def calculate_performance(attendance, study_hours, test_score):
    """
    Calculates a simple performance score based on:
    - Attendance percentage
    - Daily study hours
    - Test score percentage
    """

    # Weight distribution (you can change these)
    w_attendance = 0.3
    w_study = 0.3
    w_test = 0.4

    performance_score = (attendance * w_attendance) + \
                        (study_hours * 10 * w_study) + \
                        (test_score * w_test)

    return performance_score


def performance_grade(score):
    """Returns grade based on performance score."""
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Needs Improvement"


def main():
    print("---- Student Performance Factor Analyzer ----")

    attendance = float(input("Enter attendance percentage (0-100): "))
    study_hours = float(input("Enter average study hours per day (0-10): "))
    test_score = float(input("Enter test score percentage (0-100): "))

    score = calculate_performance(attendance, study_hours, test_score)
    grade = performance_grade(score)

    print("\n--- RESULT ---")
    print(f"Performance Score: {score:.2f}")
    print(f"Performance Rating: {grade}")


if __name__ == "__main__":
    main()
