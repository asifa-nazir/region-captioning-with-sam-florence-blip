"""Minimal pycocotools.mask stub for environments where pycocotools is unavailable."""


def __getattr__(name):
    raise RuntimeError(
        f"pycocotools.mask.{name} is unavailable in this environment."
    )
