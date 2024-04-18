score=0
print("Question 1: What is the capital of France?")
answer1 = input("a) Paris\nb) Rome\nc) Madrid\nYour answer: ")
if answer1 == 'a':
    score += 1

print("Question 1: which fruit has the highest oil content?")
answer2 = input("a) avacado\nb) tomato\nc) pumpkin\nYour answer: ")
if answer2 == 'a':
    score += 1

print("where was the kiwi fruit first grown?")
answer3 = input("a) china\nb) rome\nc) america\nYour answer: ")
if answer3 == 'a':
    score += 1



print("Quiz completed!")
print("You got score out of 3 questions correct is:",score)

