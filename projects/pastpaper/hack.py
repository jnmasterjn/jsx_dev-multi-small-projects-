import csv
import random


def read_questions():
    chinese_questions=dict()
    english_questions=dict()

    csv_file = open ("/Users/jn_master_jn/Desktop/jsx_dev/projects/pastpaper/prompt.csv",encoding="utf-8")
    question_buffer = csv.reader(csv_file)
    line_number=0
    for question in question_buffer: 
        line_number+=1

        if line_number > 1 and line_number < 40:
            y = question [1]
            m = question [2]
            q = question[3]
            chinese_questions[q] = y,m

        elif line_number > 39 and line_number < 66:
            y = question [1]
            m = question [2]
            q = question[3]
            english_questions[q] = y,m

    csv_file.close()

    return chinese_questions, english_questions
    
    
def check_input(choice:str, min:int, max: int)->int or None:
    if not choice.isdigit():
        return None 
    
    int_choice = int(choice)
     
    if int_choice < min or int_choice > max:
        return None
    
    return int_choice

def get_input() -> int or None:
    choice = None
    valid_input = None
    
    while choice is None:
        choice = input("which Subject: ")
        if choice == " ":
            print("logging out...")
            return 
        
        valid_input = check_input(choice, 1, 3)

        if valid_input is None: 
            choice = None
            continue
    return valid_input
    
def starting():
    chinese_questions,english_questions = read_questions() 
    while True:
        print("""

        Choose a subject:
              
              1: Chinese
              2: English
              3: exit 
        
              """)
       
        valid_input = get_input()

        if valid_input == 1:
            chinese(chinese_questions)
        elif valid_input == 2:
            english(english_questions)
        elif valid_input == 3:
            break

def chinese(chinese_questions:dict):

    questions = list (chinese_questions.keys())
    time = list (chinese_questions.values())


    random_question = random.choice(questions)
    print("    ")
    print(random_question)

    print("  ")
    print("  ")
    q = input("""
    type 'skip' to skip this question
    type 'time' for more info about this question
              \nyour choice: """)
    
    if q == "time":
        question_info = chinese_questions.get(random_question)
        print("   ")
        print(f"{question_info}") 
    elif q == "skip":
        print("\nok")

        
def english(eng_questions:dict):
    questions = list (eng_questions.keys())
    time = list (eng_questions.values())

    random_question = random.choice(questions)
    print("    ")
    print(random_question)

    print("  ")
    q = input("""
    type 'skip' to skip this question
    type 'time' for more info about this question
              \nyour choice: """)
    
    if q == "time":
        question_info = eng_questions.get(random_question)
        print(" ")
        print(f"{question_info}")
       
    if q == "skip":
        print("\nok")

def main():
    starting()

if __name__=="__main__":
    main()