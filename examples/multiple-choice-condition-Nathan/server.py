import random



def generate(data):

    # Logic to compute a1 answer goes here
    if random.randint(0, 5) < 2:
        a1_0 = True
        a2_true = False
    else:
        a1_0 = False
        a2_true = True
        
    # which answers are true and false go here
    data['params']['correct_a1_0'] = a1_0
    data['params']['correct_a1_1'] = not a1_0

    data['params']['correct_a2_true'] = a2_true
    data['params']['correct_a2_false'] = not a2_true

    # you could also change the answer options by passing additional params
    # instead of hardcoding them in to question.html
