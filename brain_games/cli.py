import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    return user_name


def get_answer(question):
    print(f"Question: {question}")
    user_answer = prompt.string('Your answer: ')
    return user_answer
