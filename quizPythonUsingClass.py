from QuizQuestion import QuizQuestion

quizQuestions = [
    QuizQuestion("Your fav fruit?", ["apple", "mango", "guava"],"apple"),
    QuizQuestion("Your fav city?", ["ktm", "jnk", "brt", "drn"],"drn"),
    QuizQuestion("Your fav bake?", ["bake1", "bake2", "bake3"],"bake3"),
    QuizQuestion("Your fav fruit?", ["lake3", "lake4", "lake5"],"lake5"),
]


score = 0

for q in quizQuestions:
    q.display()
    if q.checkAnswer():
        score = score + 1


print(f"Quiz complete. You answered {score} out of {(len(quizQuestions))} questions correctly.")




