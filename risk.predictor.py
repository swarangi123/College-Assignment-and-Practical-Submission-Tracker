# ============================================================
# SMARTCLASS.AI - RISK PREDICTOR
# ============================================================

from database.db import (
    get_all_students,
    get_all_assignments,
    get_all_submissions
)


# ============================================================
# CALCULATE STUDENT RISK
# ============================================================

def calculate_student_risk(student_id):
    """
    Calculate an academic risk score for one student.

    The score is based on:
    - Assignment completion
    - Submission activity
    - Graded performance

    Returns a dictionary containing:
        risk_score
        risk_level
        completion_rate
        average_score
        recommendation
    """

    assignments = get_all_assignments()
    submissions = get_all_submissions()

    # --------------------------------------------------------
    # NO ASSIGNMENTS
    # --------------------------------------------------------

    if not assignments:

        return {
            "risk_score": 0,
            "risk_level": "No Data",
            "completion_rate": 0,
            "average_score": 0,
            "recommendation": "Create assignments to begin analysis."
        }

    # --------------------------------------------------------
    # STUDENT SUBMISSIONS
    # --------------------------------------------------------

    student_submissions = [
        submission
        for submission in submissions
        if submission["student_id"] == student_id
    ]

    total_assignments = len(assignments)
    submitted_assignments = len(student_submissions)

    # --------------------------------------------------------
    # COMPLETION RATE
    # --------------------------------------------------------

    completion_rate = (
        submitted_assignments /
        total_assignments
    ) * 100

    # --------------------------------------------------------
    # AVERAGE SCORE
    # --------------------------------------------------------

    scores = []

    for submission in student_submissions:

        if (
            submission["status"] == "Graded"
            and submission["marks"] is not None
            and submission["max_marks"]
            and submission["max_marks"] > 0
        ):

            percentage = (
                float(submission["marks"]) /
                float(submission["max_marks"])
            ) * 100

            scores.append(percentage)

    if scores:

        average_score = (
            sum(scores) /
            len(scores)
        )

    else:

        # If nothing has been graded yet,
        # don't automatically treat the student
        # as academically weak.
        average_score = 100

    # --------------------------------------------------------
    # RISK SCORE
    # --------------------------------------------------------

    risk_score = 0

    # Missing assignments
    if completion_rate < 40:

        risk_score += 65

    elif completion_rate < 60:

        risk_score += 50

    elif completion_rate < 80:

        risk_score += 30

    elif completion_rate < 90:

        risk_score += 10

    # Academic performance
    if average_score < 40:

        risk_score += 35

    elif average_score < 50:

        risk_score += 30

    elif average_score < 60:

        risk_score += 20

    elif average_score < 70:

        risk_score += 10

    # Never allow the score above 100
    risk_score = min(
        risk_score,
        100
    )

    # --------------------------------------------------------
    # RISK LEVEL
    # --------------------------------------------------------

    if risk_score >= 70:

        risk_level = "High Risk"

        recommendation = (
            "Student may need immediate academic attention. "
            "Review missing work and provide additional support."
        )

    elif risk_score >= 40:

        risk_level = "Medium Risk"

        recommendation = (
            "Student shows some warning signs. "
            "Monitor upcoming submissions and performance."
        )

    elif risk_score >= 20:

        risk_level = "Low Risk"

        recommendation = (
            "Student is progressing normally, but continued "
            "monitoring is recommended."
        )

    else:

        risk_level = "Healthy"

        recommendation = (
            "Student is showing healthy submission and "
            "academic activity."
        )

    return {
        "risk_score": round(risk_score, 1),
        "risk_level": risk_level,
        "completion_rate": round(completion_rate, 1),
        "average_score": round(average_score, 1),
        "recommendation": recommendation
    }


# ============================================================
# CALCULATE RISK FOR ALL STUDENTS
# ============================================================

def calculate_all_student_risks():
    """
    Calculate risk information for every student.

    Returns a list sorted from highest risk
    to lowest risk.
    """

    students = get_all_students()

    results = []

    for student in students:

        analysis = calculate_student_risk(
            student["user_id"]
        )

        results.append({
            "student_id": student["user_id"],
            "name": student["name"],
            "email": student["email"],
            **analysis
        })

    # --------------------------------------------------------
    # SORT BY RISK SCORE
    # --------------------------------------------------------

    results.sort(
        key=lambda student: student["risk_score"],
        reverse=True
    )

    return results


# ============================================================
# GET HIGH-RISK STUDENTS
# ============================================================

def get_high_risk_students():

    students = calculate_all_student_risks()

    return [
        student
        for student in students
        if student["risk_level"] == "High Risk"
    ]


# ============================================================
# GET MEDIUM-RISK STUDENTS
# ============================================================

def get_medium_risk_students():

    students = calculate_all_student_risks()

    return [
        student
        for student in students
        if student["risk_level"] == "Medium Risk"
    ]


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("\nSmartClass.ai - Risk Analysis")
    print("=" * 40)

    students = calculate_all_student_risks()

    if not students:

        print("No students available.")

    else:

        for student in students:

            print(
                f"\nStudent: {student['name']}"
            )

            print(
                f"Risk: {student['risk_level']}"
            )

            print(
                f"Risk Score: {student['risk_score']}"
            )

            print(
                f"Completion: {student['completion_rate']}%"
            )

            print(
                f"Average Score: {student['average_score']}%"
            )

            print(
                f"Recommendation: "
                f"{student['recommendation']}"
            )
