"""Minimal decord stub for environments where decord is unavailable."""


def cpu(index=0):
    return index


class VideoReader:
    def __init__(self, *args, **kwargs):
        raise RuntimeError(
            "decord is not installed in this environment. VideoReader is unavailable."
        )
