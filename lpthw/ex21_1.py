from typing import AnyStr


def cal(a, b, c, d):
    print(f"ADDING {a} + {b} / {c} - {d}")
    return a + b / c - d

ans = cal(24, 34, 100, 1023)
print(ans)