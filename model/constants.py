## Initialising Constants
## STATES - GRID ENVRIONMENT
GRID = [
    ['G', 'W', 'G', ' ', ' ', 'G'],
    [' ', 'B', ' ', 'G', 'W', 'B'],
    [' ', ' ', 'B', ' ', 'G', ' '],
    [' ', ' ', ' ', 'B', ' ', 'G'],
    [' ', 'W', 'W', 'W', 'B', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
]

## REWARD FUNCTION
REWARD_MAP = {
    ' ': -0.04,  # white square
    'G': 1.0,  # green square
    'B': -1.0  # brown square
}

## DISCOUNT
DISCOUNT = 0.99

## VALUE ITERATION ALGORITHM
C = 0.1
R_MAX = 1
EPSILON = C * R_MAX
CONVERGENCE_THRESHOLD = (EPSILON * (1 - DISCOUNT))/ DISCOUNT

## POLICY ITERATION ALGORITHM
K = 100


