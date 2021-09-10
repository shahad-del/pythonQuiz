# question = {'full form of css':['cascading style sheet','common style sheet','clean style sheet','clear style sheet'],
# 'full form of http':['http style sheet','hypertext protocol','hypertext transfer protocol','height of text']}
questions = ['full form of css','full form of http'];
answers = ['cascading style sheet','hypertext transfer protocol'];
options =[['cascading style sheet','common style sheet','clean style sheet','clear style sheet'],['http style sheet','hypertext protocol','hypertext transfer protocol','height of text']]


score = 0

for curQuesIdx,q in enumerate(questions):
    curQues = questions[curQuesIdx]
    print(f"\nQ{(curQuesIdx + 1)}. {curQues}")
    curOptions = options[curQuesIdx]
    for optIdx,o in enumerate(curOptions):
        print(f"{(optIdx + 1)}. {o}")
    
    print('Enter correct options no.:')
    userAns = ""
    while True:
        try:
            userAnsNo = int(input())            
            userAns = curOptions[userAnsNo-1]
            break
        except:
            print("please enter a valid option no.")

    curAns = answers[curQuesIdx]
    if curAns == userAns:
        print('Correct')
        score = score + 1
    else:
        print('incorrect')


print(f"Quiz complete. You answered {score} out of {(len(questions))} questions correctly.")














    