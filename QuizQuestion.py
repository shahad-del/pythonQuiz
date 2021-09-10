class QuizQuestion:
    def __init__(self, question, options, ans):
        self.question = question
        self.options = options
        self.ans = ans

    def display(self):
        print(f"\nQ. {self.question}")
        for optIdx,o in enumerate(self.options):
            print(f"{(optIdx + 1)}. {o}")

    def checkAnswer(self):
        answerToCheckAgainst = ""
        while True:
            try:
                userAnsNo = int(input())
                answerToCheckAgainst = self.options[userAnsNo-1]
                break
            except:
                print("please enter a valid option no.")

        if answerToCheckAgainst == self.ans:
            print("Correct")
            print("__________________________________")
            return True
        else:
            print("Incorrect")
            print("__________________________________")
            return False



