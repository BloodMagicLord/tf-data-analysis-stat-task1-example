import numpy as np

chat_id = 632165934  # Ваш chat ID, не меняйте название переменной
TIME_INTERVAL = 4


def solution(x: np.array) -> float:
    return np.mean(x) * (2 / TIME_INTERVAL ** 2)
