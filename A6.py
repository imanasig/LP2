# I. Information Management Expert System
def information_system():

    knowledge_base = {
        "store": ["Data stored successfully"],
        "search": ["Fetching required data"],
        "update": ["Data updated"],
        "delete": ["Data removed"]
    }

    def process_query(queries):
        result = []
        for q in queries:
            q = q.strip().lower()
            if q in knowledge_base:
                result.extend(knowledge_base[q])
        return list(set(result))

    print("\nInformation Management Expert System")
    user_input = input("Enter operations (comma separated): ")
    queries = user_input.split(",")

    output = process_query(queries)
    print("Result:", output if output else "No match found")

# II. Hospital Expert System
def hospital_system():

    knowledge_base = {
        "fever": ["Flu", "Infection"],
        "cough": ["Cold", "Bronchitis"],
        "chest pain": ["Heart Attack"]
    }

    facility = {
        "Heart Attack": "Emergency Room",
        "Flu": "General Physician"
    }

    def diagnose(symptoms):
        conditions = []
        for s in symptoms:
            s = s.strip().lower()
            if s in knowledge_base:
                conditions.extend(knowledge_base[s])
        return list(set(conditions))

    def recommend(conditions):
        result = []
        for c in conditions:
            if c in facility:
                result.append(facility[c])
            else:
                result.append("General Clinic")
        return list(set(result))

    print("\nHospital Expert System")
    user_input = input("Enter symptoms: ")
    symptoms = user_input.split(",")

    conditions = diagnose(symptoms)
    facilities = recommend(conditions)

    print("Possible Conditions:", conditions)
    print("Recommended Facilities:", facilities)

# III. Help Desk Expert System
def help_desk_system():

    knowledge_base = {
        "login": ["Reset password"],
        "network": ["Check internet connection"],
        "software": ["Reinstall application"]
    }

    def solve(issues):
        solutions = []
        for i in issues:
            i = i.strip().lower()
            if i in knowledge_base:
                solutions.extend(knowledge_base[i])
        return list(set(solutions))

    print("\nHelp Desk Expert System")
    user_input = input("Enter issues: ")
    issues = user_input.split(",")

    solutions = solve(issues)
    print("Solutions:", solutions if solutions else "No solution found")

# IV. Employee Performance Expert System
def employee_system():

    def evaluate(rating):
        if rating >= 4:
            return "Excellent"
        elif rating == 3:
            return "Good"
        elif rating == 2:
            return "Average"
        else:
            return "Needs Improvement"

    print("\nEmployee Evaluation System")
    rating = int(input("Enter rating (1-5): "))

    result = evaluate(rating)
    print("Performance:", result)

# V. Stock Market Expert System
def stock_system():

    rules = {
        "up": "Buy stocks",
        "down": "Sell stocks",
        "stable": "Hold stocks"
    }

    def suggest(trend):
        trend = trend.lower()
        if trend in rules:
            return rules[trend]
        else:
            return "Observe market"

    print("\nStock Market Expert System")
    trend = input("Enter market trend: ")

    print("Advice:", suggest(trend))

# VI. Airline Scheduling Expert System
def airline_system():

    rules = {
        "high": "Immediate flight allocation",
        "medium": "Next available flight",
        "low": "Waiting list"
    }

    def schedule(priority):
        priority = priority.lower()
        if priority in rules:
            return rules[priority]
        else:
            return "Invalid input"

    print("\nAirline Scheduling Expert System")
    priority = input("Enter cargo priority: ")

    print("Schedule:", schedule(priority))

def main():
    print("\n===== Expert System Menu =====")
    print("1. Information Management")
    print("2. Hospital System")
    print("3. Help Desk")
    print("4. Employee Evaluation")
    print("5. Stock Market")
    print("6. Airline Scheduling")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        information_system()
    elif choice == 2:
        hospital_system()
    elif choice == 3:
        help_desk_system()
    elif choice == 4:
        employee_system()
    elif choice == 5:
        stock_system()
    elif choice == 6:
        airline_system()
    else:
        print("Invalid choice")

# Run program
main()