"""Fluid domain grid.

Defines a simple grid for parameterising a fluidic domain discetised into connected cells.
"""

from enum import IntEnum, unique
from functools import cached_property
from math import sqrt

from pydantic import Field

from fast_fluids.utils.pydantic_utils import BaseModel


@unique
class Dimension(IntEnum):
    """Dimension index within a multi-dimensional domain."""

    x: int = 0
    y: int = 1


class Point(BaseModel):
    """Point within a multi-dimensional cartesian grid.

    Args:
        x: X-axis index.
        y: Y-axis index.
    """

    x: int = Field(ge=0)
    y: int = Field(ge=0)


class CartesianGrid(BaseModel):
    """A multi-dimensional grid of equally sized cells.

    An array of equally sized square cells. The total area of the grid can be configured, which
    scales the size of every cell withing the domain.

    Args:
        area: Total area of the grid.
        num_x_cells: Number of cells in the x-axis.
        num_y_cells: Number of cells in the y-axis.
    """

    area: float = Field(gt=0)
    num_x_cells: int = Field(ge=1)
    num_y_cells: int = Field(ge=1)

    @cached_property
    def num_cells(self) -> int:
        """Total number of cells within the grid."""
        return self.num_x_cells * self.num_y_cells

    @cached_property
    def cell_area(self) -> float:
        """Area of each cell."""
        return self.area / self.num_cells

    @cached_property
    def cell_length(self) -> float:
        """Length of each cell."""
        return sqrt(self.cell_area)

    def __contains__(self, point: Point) -> bool:
        """Determine if a point is within the grid."""
        return (0 <= point.x < self.num_x_cells) and (0 <= point.y < self.num_y_cells)
