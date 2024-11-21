# Quiz Application
# Questions Database
quiz_db = {
    "DSA": {
        1: ["What is the time complexity of binary search?", "O(n)", "O(log n)", "O(n^2)", "O(1)", 2],
        2: ["What does 'FIFO' stand for?", "First In First Out", "Fast In Fast Out", "First In Final Out", "None", 1],
        3: ["Which data structure uses LIFO?", "Queue", "Stack", "Graph", "Tree", 2],
        4: ["What is a full binary tree?", "All nodes have 0 or 2 children", "All nodes have 2 children", 
            "All levels are completely filled", "None", 1],
        5: ["What is the height of an empty tree?", "-1", "0", "1", "None", 2]
    },
    "DBMS": {
        1: ["What does SQL stand for?", "Structured Query Language", "Simple Query Language", 
            "Standard Query Language", "None", 1],
        2: ["Which of the following is a NoSQL database?", "MySQL", "MongoDB", "Oracle", "PostgreSQL", 2],
        3: ["What does ACID stand for in DBMS?", "Atomicity Consistency Isolation Durability", 
            "Auto Consistent Isolation Dependency", "Atomicity Connection Integrity Dependency", "None", 1],
        4: ["What is a primary key?", "A unique identifier", "A foreign key", "A candidate key", "None", 1],
        5: ["What does DDL stand for?", "Data Definition Language", "Data Description Language", 
            "Database Description Language", "None", 1]
    },
    "Python": {
        1: ["What is the output of print(2**3)?", "6", "8", "9", "12", 2],
        2: ["What is a correct syntax for defining a function?", "func def():", "def func:", "def func():", 
            "function func()", 3],
        3: ["Which library is used for Data Analysis?", "NumPy", "Pandas", "SciPy", "All of these", 4],
        4: ["What is the default data type of 5 in Python?", "int", "float", "double", "string", 1],
        5: ["Which keyword is used to define a class?", "def", "class", "struct", "object", 2]
    }
}

users = {}
current_user = None
user_scores = {}

# Function to register a user
def register():
    global users
    print("=== Registration ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        print("Username already exists!")
    else:
        users[username] = password
        user_scores[username] = {}
        print("Registration successful!")

# Function to login
def login():
    global current_user
    print("=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        current_user = username
        print(f"Welcome {username}!")
    else:
        print("Invalid credentials!")

# Function to attempt a quiz
def attempt_quiz():
    if not current_user:
        print("Please login to attempt a quiz!")
        return
    print("=== Select Quiz Topic ===")
    print("1. DSA\n2. DBMS\n3. Python")
    choice = int(input("Enter your choice: "))
    topics = {1: "DSA", 2: "DBMS", 3: "Python"}
    if choice not in topics:
        print("Invalid choice!")
        return
    topic = topics[choice]
    print(f"Starting quiz on {topic}...")
    score = 0
    for qid, question in quiz_db[topic].items():
        print(f"Q{qid}. {question[0]}")
        print(f"1. {question[1]}\n2. {question[2]}\n3. {question[3]}\n4. {question[4]}")
        answer = int(input("Enter your answer (1-4): "))
        if answer == question[5]:
            score += 1
    user_scores[current_user][topic] = score
    print(f"Quiz completed! Your score: {score}/5")

# Function to show results
def show_results():
    if not current_user:
        print("Please login to view results!")
        return
    print(f"=== Results for {current_user} ===")
    if current_user not in user_scores or not user_scores[current_user]:
        print("No quizzes attempted yet!")
    else:
        for topic, score in user_scores[current_user].items():
            print(f"{topic}: {score}/5")

# Main menu
def main():
    while True:
        print("\n=== Quiz Application ===")
        print("1. Registration")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. Show Result")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            attempt_quiz()
        elif choice == 4:
            show_results()
        elif choice == 5:
            print("Exiting Quiz Application. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
