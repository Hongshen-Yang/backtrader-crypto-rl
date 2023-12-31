import math
import random
from tqdm import tqdm
from itertools import product

param_grid = {
    "param1": random.sample(range(-50, 50), 5),
    "param2": random.sample(range(-50, 50), 10),
    "param3": random.sample(range(-50, 50), 6),
}

datafeeds = random.sample(range(-50, 50), 5)

def est(datafeeds, param_dict):
    # {param1: 1, param2: 2, param3:3}
    val1 = math.sin(param_dict.get('param1'))
    val2 = math.cos(param_dict.get('param2'))
    val3 = math.sin(param_dict.get('param3'))
    return val1 + val2 + val3

def scoring(result):
    score = result**2
    return score

# Try to follow the practice of sklearn
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
def gridsearch(estimator, param_grid, scoring, datafeeds):
    best_score = None

    # Generate all possible combinations of parameters
    param_combinations = list(product(*param_grid.values()))

    for params in tqdm(param_combinations):
        param_dict = {key: val for key, val in zip(param_grid.keys(), params)}
        if param_dict['OPEN_THRE'] > param_dict['CLOS_THRE']:
            print(param_dict)
            result = estimator(datafeeds, param_dict)
            score = scoring(result)
            if best_score is None or score > best_score:
                best_score = score
                best_params = param_dict
                best_result = result

    return best_score, best_params, best_result

if __name__ == '__main__':
    # res = gridsearch(est, param_grid, scoring, datafeeds)
    # print(res)
    print(param_grid)