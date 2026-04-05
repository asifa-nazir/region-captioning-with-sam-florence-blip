"""Minimal Triton stub for environments where Triton is unavailable.

This is only intended to let libraries that unconditionally import Triton
modules load on platforms like Windows. It does not implement Triton kernels.
"""


def jit(fn=None, **_kwargs):
    if fn is None:
        def decorator(inner):
            return inner
        return decorator
    return fn


def autotune(configs=None, key=None):
    def decorator(fn):
        return fn
    return decorator


def cdiv(x, y):
    return (x + y - 1) // y


class Config:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
