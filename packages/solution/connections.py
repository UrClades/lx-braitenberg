# modified bij WPH
from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    res[175:329, 320:589] = 0.4
    res[175:329, 270:319] = 0.35
    res[175:329, 220:269] = 0.3
    res[175:329, 170:219] = 0.2
    res[175:329, 120:169] = 0.1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    res[175:329,  50:319] = 0.4
    res[175:329, 320:369] = 0.35
    res[175:329, 370:419] = 0.3
    res[175:329, 420:469] = 0.2
    res[175:329, 470:519] = 0.1
    return res
