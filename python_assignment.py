import json

def quiz(user_input):
    with open("quiz.json",'r') as f:
        content = json.load(f)
        score = 0
        if user_input == "1" or user_input=="Sport" or user_input=="sport":
            print("\nQuestion:   ",content["quiz"]["sport"]["q1"]["question"],"\n")
            options = list(content["quiz"]["sport"]["q1"]["options"])
            for i,op in enumerate(options):
                print(i+1,".",op,sep=" ")
            answer = input("\nEnter your answer:\n")
            if answer== "4" or answer=="Huston Rocket":
                score += 1
                
            print("\nYour Score is {}/1".format(score))
            return 0
                
        elif user_input == "2" or user_input=="Math" or user_input=="math":
            print("\nQuestion:   ",content["quiz"]["maths"]["q1"]["question"],"\n")
            options = list(content["quiz"]["maths"]["q1"]["options"])
            for i,op in enumerate(options):
                print(i+1,".",op,sep=" ")
            answer = input("\nEnter your answer:\n")
            if answer== "3" or answer=="12":
                score += 1
                
            print("\nQuestion:   ",content["quiz"]["maths"]["q2"]["question"],"\n")
            options = list(content["quiz"]["maths"]["q2"]["options"])
            for i,op in enumerate(options):
                print(i+1,".",op,sep=" ")
            answer = input("\nEnter your answer:\n")
            if answer== "4" or answer=="4":
                score += 1
                
            print("\nYour Score is {}/2".format(score))
            return 0
        
        else:
            print("\nInvalid Entry \n")
            return 1

if __name__ == '__main__':
    
    user_input = input("Enter your choice for quiz area: \n1. Sport\n2. Math\n")
    result = quiz(user_input)
    while result == 1:
        user_input = input("Enter your choice for quiz area: \n1. Sport\n2. Math\n")
        new_result = quiz(user_input)
        if new_result == 0:
            result = 0
        else:
            result = 1