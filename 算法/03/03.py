import random

def generate_lottery_numbers(num_balls, num_red_balls):
    red_balls = random.sample(range(1, num_red_balls+1), 6)
    blue_ball = random.randint(1, num_balls)
    return sorted(red_balls) + [blue_ball]

for i in range(5):
    numbers = generate_lottery_numbers(num_balls=16, num_red_balls=33)
    print("双色球号码: ", numbers)
