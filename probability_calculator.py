import random
class Hat:
    def __init__(self,**kwargs):
        contents = kwargs
        self.contents = list(contents)
        self.hat = contents
        ball_num = contents.values()
        self.orig = contents
        self.ball = []
        for ball in list(contents):
            while contents[ball] != 0:
                self.ball.append(ball)
                contents[ball] = contents[ball] - 1
    def draw(self,number):
        self.draw_bucket = []
        rand_draw = random.sample(self.ball,number)
        return rand_draw
        print (rand_draw)
        if len(self.ball) > number:
            for rand in rand_draw:
                self.ball.remove(rand)
                self.draw_bucket.append(rand)
        if len(self.ball) < number:
            for draws in self.draw_bucket:
                self.ball.append(draws)
                self.draw_bucket.remove(draws)

def experiment(hat,expected_balls= {},num_balls_drawn=0,num_experiments =0):
    expect = list(expected_balls)
    exp_bucket = []
    proba_count = 0
    small_count = 0
    proba_c = 0
    cycle_count = num_experiments
    for ball_exp in expect:
        while expected_balls[ball_exp] != 0:
            exp_bucket.append(ball_exp)
            expected_balls[ball_exp] = expected_balls[ball_exp] - 1
    while cycle_count !=0:
        draws = hat.draw(num_balls_drawn)
        x = len(exp_bucket)
        for exp in exp_bucket:
            small_count = small_count + 1
            num1 = exp_bucket.count(exp)
            num2 = draws.count(exp)
            if num2 >= num1:
                proba_c = proba_c + 1
        if small_count == x:
                small_count = small_count*0
        if proba_c == x:
            proba_count = proba_count + 1
        proba_c = proba_c*0
        cycle_count = cycle_count - 1
    perc = proba_count/num_experiments*100
    return ('{0:.2f}%'.format(perc))
