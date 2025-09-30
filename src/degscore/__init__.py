"""DegScore: A ridge regression model to predict RNA degradation."""

from .DegScore import DegScore, encode_input, create_U_mask

__version__ = "2.1.0"
__all__ = ["DegScore", "encode_input", "create_U_mask"]
