import random
import time

operators = [ "+","-","*"]
min_value = 3
max_value = 13
no_question = 10
wrong_count = 0

def generate_exp():
    first_term = random.randint(min_value,max_value)
    second_term = random.randint(min_value,max_value)
    operator = random.choice(operators)
    expression = str(first_term)+" " + operator +" "+ str(second_term)
    answer = eval(expression)
    return expression , answer


input("Press Enter to start")
print("-----------------")

start_time = time.time()
for  i in range(no_question):
    expression  , answer = generate_exp()
    while True:
        guess = input(f"{expression} : ")
        if guess == str(answer):
            break
        wrong_count +=1

end_time = time.time()
total_time = end_time - start_time
total_time = round(total_time,2)
print("-----------------------")
print(f"well done your time is {total_time}")
print(f"you got {wrong_count} wrong answer")
