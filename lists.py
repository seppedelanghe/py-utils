import os, random, math


'''
    accepts a list 'l' and returns a new list that only contains a certain percentage of that list
    l = list
    s = percentage
    r = randomize selection
'''
def select_in_list(l, s=0.1, r=False):
    if r:
        random.shuffle(l)

    res = [l[int(i / s)] for i in range(int(len(l) * s))]
    assert len(res) == math.floor(len(l) * s), 'result is not the correct length'

    return res



    
if __name__ == '__main__':
    l = [i for i in range(5005)]
    ll = select_in_list(l)