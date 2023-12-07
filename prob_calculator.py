import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):  # https://www.geeksforgeeks.org/args-kwargs-python/
        self.contents = []
        self.initial_state = kwargs
        for color in kwargs:
            for _ in range(kwargs[color]):
                self.contents.append(color)

    def draw(self, num_balls):
        balls = []
        if num_balls > len(self.contents):
            return self.contents
        for _ in range(num_balls):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            balls.append(ball)
        return balls

    def __str__(self):
        return str(self.initial_state)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)

        # draw_dict = {}
        # for ball in set(balls_drawn):
        #     draw_dict[ball] = balls_drawn.count(ball)
        draw_dict = {ball: balls_drawn.count(ball) for ball in set(balls_drawn)}

        success = True
        for color, expected_count in expected_balls.items():
            if draw_dict.get(color, 0) < expected_count:
                success = False
                break

        if success:
            count += 1

    print(
        f"The probability to get {expected_balls} from {hat} with {num_balls_drawn} draws is: {round(count / num_experiments, 5) * 100}%."
    )
    return count / num_experiments
