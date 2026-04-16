import json
import os
import datetime
import random

# -----------------------------
# File management 
# -----------------------------

users_file = "users.json"
complaints_file = "complaints.json"
history_file = "history.json"

for file in [users_file, complaints_file, history_file]:
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump({}, f)

def save_history(username, message):
    with open(history_file, "r") as f:
        data = json.load(f)
    if username not in data:
        data[username] = []
    data[username].append({
        "time": str(datetime.datetime.now()),
        "message": message
    })
    with open(history_file, "w") as f:
        json.dump(data, f, indent=4)

# -----------------------------
# Authentication 
# -----------------------------

def register():
    print("\n--- Register ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open(users_file, "r") as f:
        users = json.load(f)
    users[username] = password
    with open(users_file, "w") as f:
        json.dump(users, f)
    print("Registration successful!\n")

def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")
    with open(users_file, "r") as f:
        users = json.load(f)
    if username in users and users[username] == password:
        print("Login successful!\n")
        return username
    else:
        print("Invalid credentials\n")
        return None

# -----------------------------
# Original features 
# -----------------------------

def student_assistant(username):
    while True:
        print("\nStudent Assistant")
        print("1. Attendance")
        print("2. Marks")
        print("3. Timetable")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            response = "Your attendance is 85%"
            print(response)
            save_history(username, response)
        elif choice == "2":
            response = "Math:90 Python:92 Physics:88"
            print(response)
            save_history(username, response)
        elif choice == "3":
            response = "Mon:Python Tue:DS Wed:Math"
            print(response)
            save_history(username, response)
        elif choice == "4":
            break

def college_helpdesk(username):
    while True:
        print("\nCollege Helpdesk")
        print("1. Admission Info")
        print("2. Fees")
        print("3. Courses")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            response = "Admissions open from June"
            print(response)
            save_history(username, response)
        elif choice == "2":
            response = "Fees ₹1,50,000 per year"
            print(response)
            save_history(username, response)
        elif choice == "3":
            response = "Courses: AIML, CSE, ECE"
            print(response)
            save_history(username, response)
        elif choice == "4":
            break

def customer_support(username):
    while True:
        print("\nCustomer Support")
        print("1. Register Complaint")
        print("2. View Complaints")
        print("3. Back")
        choice = input("Choose option: ")
        if choice == "1":
            complaint = input("Enter complaint: ")
            with open(complaints_file, "r") as f:
                data = json.load(f)
            cid = str(len(data) + 1)
            data[cid] = complaint
            with open(complaints_file, "w") as f:
                json.dump(data, f)
            print("Complaint Registered ID:", cid)
        elif choice == "2":
            with open(complaints_file, "r") as f:
                data = json.load(f)
            print("\nComplaints:")
            for k, v in data.items():
                print(k, ":", v)
        elif choice == "3":
            break

def view_history(username):
    with open(history_file, "r") as f:
        data = json.load(f)
    if username in data:
        print("\nChat History:\n")
        for chat in data[username]:
            print(chat["time"], "-", chat["message"])
    else:
        print("No history found")

# -----------------------------
# IMPROVED AI CHATBOT
# -----------------------------

def ai_chatbot(username):
    """
    An enhanced rule-based chatbot with keyword scoring and contextual suggestions.
    """
    # Define intents with keywords and possible responses
    intents = [
        {
            "name": "greeting",
            "keywords": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"],
            "responses": [
                "Hello! How can I help you today?",
                "Hi there! Ask me anything about the college.",
                "Hey! What can I do for you?",
                "Greetings! Need any information?"
            ]
        },
        {
            "name": "farewell",
            "keywords": ["bye", "goodbye", "exit", "quit", "see you", "take care"],
            "responses": [
                "Goodbye! Have a great day!",
                "See you later!",
                "Take care! Come back anytime."
            ]
        },
        {
            "name": "thanks",
            "keywords": ["thanks", "thank you", "appreciate", "helpful"],
            "responses": [
                "You're welcome!",
                "Happy to help!",
                "Anytime!",
                "My pleasure!"
            ]
        },
        {
            "name": "who_are_you",
            "keywords": ["who are you", "your name", "what are you", "yourself"],
            "responses": [
                "I'm Smart College Chatbot, your virtual assistant.",
                "I'm an AI chatbot designed to answer college-related queries.",
                "I'm your friendly college assistant!"
            ]
        },
        {
            "name": "courses",
            "keywords": ["course", "courses", "program", "programs", "branch", "branches", "btech", "b.tech"],
            "responses": [
                "We offer B.Tech in: AIML, CSE, ECE, Mechanical, Civil, and Electrical.",
                "Our main courses: AIML, CSE, ECE, Mechanical Engineering.",
                "You can choose from AIML, CSE, ECE, Mechanical, Civil, and Electrical."
            ]
        },
        {
            "name": "fees",
            "keywords": ["fee", "fees", "cost", "tuition", "payment", "expenses"],
            "responses": [
                "The annual tuition fee is ₹1,50,000. Hostel and mess are extra.",
                "Fees: ₹1,50,000 per year. Scholarships are available for meritorious students.",
                "Total fees around ₹1,50,000 per year. Contact accounts office for detailed breakdown."
            ]
        },
        {
            "name": "admission",
            "keywords": ["admission", "admissions", "apply", "application", "enroll", "eligibility"],
            "responses": [
                "Admissions open from June. Last date is usually August 31st.",
                "You can apply online through our college website. Admission based on entrance exam or merit.",
                "Eligibility: 60% in 12th (PCM). Admissions start in June."
            ]
        },
        {
            "name": "location",
            "keywords": ["location", "where", "address", "campus", "place"],
            "responses": [
                "Our college is located in Vijayawada, Andhra Pradesh.",
                "Address: Smart College Campus, NH-16, Guntur District, Andhra Pradesh.",
                "We are situated in the heart of Andhra Pradesh, easily accessible by road and rail."
            ]
        },
        {
            "name": "attendance",
            "keywords": ["attendance", "present", "absent", "percentage"],
            "responses": [
                "Use the Student Assistant (option 1 in main menu) to check your attendance.",
                "Attendance details are available in Student Assistant section.",
                "Please go to Student Assistant for personalised attendance information."
            ]
        },
        {
            "name": "marks",
            "keywords": ["marks", "grades", "result", "scores", "cgpa", "gpa"],
            "responses": [
                "You can view your marks using the Student Assistant (option 1).",
                "Marks and grades are shown in the Student Assistant section.",
                "Please select Student Assistant from the main menu to see your marks."
            ]
        },
        {
            "name": "timetable",
            "keywords": ["timetable", "schedule", "time table", "class timings", "routine"],
            "responses": [
                "Timetable: Monday: Python, Tuesday: Data Structures, Wednesday: Mathematics.",
                "You can find your weekly timetable in the Student Assistant.",
                "Class schedule is available under Student Assistant → Timetable."
            ]
        },
        {
            "name": "exam",
            "keywords": ["exam", "examination", "midterms", "finals", "semester", "internal"],
            "responses": [
                "Mid semester exams are usually in September and February. Finals in December and May.",
                "Exam schedule is announced on the notice board and student portal.",
                "Make sure to check with your department for exact exam dates."
            ]
        },
        {
            "name": "hostel",
            "keywords": ["hostel", "accommodation", "room", "mess", "dorm"],
            "responses": [
                "We have separate hostels for boys and girls. AC and non-AC rooms available.",
                "Hostel fee is ₹80,000 per year including mess. Limited seats, apply early.",
                "Hostel facilities: Wi-Fi, 24/7 water, security, and mess with vegetarian food."
            ]
        },
        {
            "name": "library",
            "keywords": ["library", "books", "book", "reading", "journals"],
            "responses": [
                "The central library has over 50,000 books and online journals. Open 8 AM to 8 PM.",
                "Library membership is free for all students. You can borrow up to 5 books.",
                "Digital library and e-resources are available 24/7 through the student portal."
            ]
        },
        {
            "name": "placement",
            "keywords": ["placement", "job", "company", "recruitment", "campus", "package"],
            "responses": [
                "Our placement cell has tie-ups with top companies. Average package: ₹5 LPA.",
                "Last year 90% of eligible students were placed. Top recruiters: TCS, Infosys, Amazon.",
                "Placement training starts from the 6th semester. Contact placement office for details."
            ]
        },
        {
            "name": "scholarship",
            "keywords": ["scholarship", "financial aid", "fee waiver", "merit"],
            "responses": [
                "Merit scholarships: 100% fee waiver for top 5% of students. Also government scholarships available.",
                "You can apply for JVD, BC, SC/ST scholarships. Visit the admin office for forms.",
                "Scholarships based on entrance exam rank and family income. Last date: July 31st."
            ]
        },
        {
            "name": "faculty",
            "keywords": ["faculty", "teacher", "professor", "staff", "lecturer"],
            "responses": [
                "We have experienced faculty with PhDs from top institutes. Student-faculty ratio is 15:1.",
                "All departments have qualified professors. Many are industry experts and researchers.",
                "Faculty members are approachable and provide extra help during office hours."
            ]
        },
        {
            "name": "sports",
            "keywords": ["sports", "game", "play", "tournament", "cricket", "football"],
            "responses": [
                "We have facilities for cricket, football, basketball, volleyball, and indoor games.",
                "Annual sports meet is held in December. Students can join college teams.",
                "Sports complex includes a gym, swimming pool, and athletics track."
            ]
        }
    ]

    # Fallback responses when no intent matches
    fallback_responses = [
        "I'm not sure about that. Can you rephrase?",
        "Hmm, I don't understand. Try asking about courses, fees, admission, or exams.",
        "Sorry, I couldn't catch that. You can ask about attendance, marks, timetable, placements, etc.",
        "I'm still learning. Please use the main menu options for specific tasks."
    ]

    # Suggestions shown when confidence is low
    suggestions = [
        "Ask about courses",
        "Ask about fees",
        "Ask about admission",
        "Ask about placement",
        "Ask about hostel",
        "Ask about exam dates",
        "Use Student Assistant for attendance/marks",
        "Use College Helpdesk for general info"
    ]

    print("\n🤖 AI Chatbot: Hello! I'm your enhanced assistant. Type 'exit' to return to main menu.\n")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Bot: Goodbye!\n")
            break

        save_history(username, "User: " + user_input)

        # Score each intent based on keyword matches
        best_intent = None
        best_score = 0

        for intent in intents:
            score = sum(1 for kw in intent["keywords"] if kw in user_input)
            if score > best_score:
                best_score = score
                best_intent = intent

        # If we have a match with at least one keyword
        if best_intent and best_score > 0:
            # Special case: farewell intent – break the loop
            if best_intent["name"] == "farewell":
                response = random.choice(best_intent["responses"])
                print("Bot:", response)
                save_history(username, response)
                print()  # extra line before exiting
                break

            response = random.choice(best_intent["responses"])
            print("Bot:", response)
            save_history(username, response)
        else:
            # No match: provide fallback + suggestions
            response = random.choice(fallback_responses)
            print("Bot:", response)
            save_history(username, response)
            print("Bot: I can help with:")
            for s in suggestions:
                print(f"  • {s}")
            # Also log the suggestions as part of bot's message
            save_history(username, "Bot suggested: " + ", ".join(suggestions))

# -----------------------------
# Main menu 
# -----------------------------

def chatbot(username):
    while True:
        print("\n" + "="*40)
        print("        SMART COLLEGE CHATBOT")
        print("="*40)
        print("1. Student Assistant")
        print("2. College Helpdesk")
        print("3. Customer Support")
        print("4. AI Chat (Enhanced)")
        print("5. Chat History")
        print("6. Exit")
        choice = input("Select option: ")
        if choice == "1":
            student_assistant(username)
        elif choice == "2":
            college_helpdesk(username)
        elif choice == "3":
            customer_support(username)
        elif choice == "4":
            ai_chatbot(username)
        elif choice == "5":
            view_history(username)
        elif choice == "6":
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid option. Please try again.")

# -----------------------------
# Entry point
# -----------------------------

def main():
    print("🎓 Welcome to Smart College Chatbot")
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        opt = input("Choose: ")
        if opt == "1":
            user = login()
            if user:
                chatbot(user)
        elif opt == "2":
            register()
        elif opt == "3":
            print("Thank you for using Smart College Chatbot. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
