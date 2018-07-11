import random


def field_goal_pct(instance):
    return 0.5


def get_func():
    func_list = [field_goal_pct]
    index = random.randint(0,len(func_list)-1)
    return func_list[index]