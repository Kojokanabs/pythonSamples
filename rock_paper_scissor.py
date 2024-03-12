import random
while True:
    def play():
        user = input("make a choice between rock for 'r', scissor for 's', paper for 'p':").lower()
        computer_choice = random.choice(['r', 'p', 's'])
        if user == computer_choice:
            return 'It\'s a tie'
        if is_win(user, computer_choice):
            return 'You have won'
        return 'You have lost'

# r>s, s>p, p>r
    def is_win(user, computer):
        if (user == 'r' and computer == 's') or (user == 's' and computer == 'r') or (user == 'p' and computer == 'r'):
            return True
    print(play())