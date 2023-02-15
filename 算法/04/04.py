import random

def generate_lottery_numbers(num_balls, num_red_balls):
    red_balls = random.sample(range(1, num_red_balls+1), 5)
    blue_balls = random.sample(range(1, num_balls+1), 2)
    return sorted(red_balls) + sorted(blue_balls)

for i in range(5):
    numbers = generate_lottery_numbers(num_balls=12, num_red_balls=35)
    print("大乐透号码: ", numbers)

