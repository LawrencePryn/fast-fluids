from math import sqrt

import pytest

from fast_fluids.domain.grid import CartesianGrid, Dimension, Point


@pytest.mark.parametrize("x", [0, 3, 5], ids=lambda x: f"{x=}")
@pytest.mark.parametrize("y", [0, 2, 4], ids=lambda y: f"{y=}")
def test_instantiation_of_valid_point(x: int, y: int) -> None:
    valid_point = Point(x=x, y=y)
    assert valid_point.x == x
    assert valid_point.y == y


@pytest.mark.parametrize("dimension", Dimension, ids=lambda x: x.name)
@pytest.mark.parametrize("invalid_index", [-1, -3])
def test_throw_on_invalid_point_index(dimension: Dimension, invalid_index: int) -> None:
    invalid_data = {x.name: 0 for x in Dimension} | {dimension.name: invalid_index}
    with pytest.raises(ValueError, match="greater than or equal to 0"):
        Point(**invalid_data)


@pytest.mark.parametrize("area", [0.01, 1.2], ids=lambda area: f"{area=}")
@pytest.mark.parametrize("num_x_cells", [1, 5, 7], ids=lambda num_x_cells: f"{num_x_cells=}")
@pytest.mark.parametrize("num_y_cells", [1, 3, 8], ids=lambda num_y_cells: f"{num_y_cells=}")
def test_instantiation_of_valid_cartesian_grid(
    area: float, num_x_cells: int, num_y_cells: int
) -> None:
    valid_grid = CartesianGrid(area=area, num_x_cells=num_x_cells, num_y_cells=num_y_cells)
    assert valid_grid.area == area
    assert valid_grid.num_x_cells == num_x_cells
    assert valid_grid.num_y_cells == num_y_cells
    assert valid_grid.num_cells == num_x_cells * num_y_cells
    assert valid_grid.cell_area == area / (num_x_cells * num_y_cells)
    assert valid_grid.cell_length == sqrt(area / (num_x_cells * num_y_cells))


@pytest.mark.parametrize("x", [0, 3, 9], ids=lambda x: f"{x=}")
@pytest.mark.parametrize("y", [0, 2, 4], ids=lambda y: f"{y=}")
def test_point_is_contained_within_cartesian_grid(x: int, y: int) -> None:
    grid = CartesianGrid(area=1.0, num_x_cells=10, num_y_cells=5)
    point = Point(x=x, y=y)
    assert point in grid
