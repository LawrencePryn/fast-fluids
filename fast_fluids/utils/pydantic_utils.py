"""Utility functions for Pydantic.

Defines a number of utility functions to be used in conjunction with the Pydantic module.
"""

from typing import TypeVar

from pydantic import BaseModel as _BaseModel
from pydantic import ConfigDict


class BaseModel(_BaseModel):
    """Pydantic BaseModel with a custom default configuration."""

    model_config = ConfigDict(extra="forbid", frozen=True)


Model = TypeVar("Model", bound=BaseModel)


def field_names(model: Model | type[Model]) -> set[str]:
    """List the field names of a Pydantic model class or object.

    Args:
        model: Pydantic model.

    Returns:
        Set of unique field names.
    """
    return set(model.model_fields.keys())
