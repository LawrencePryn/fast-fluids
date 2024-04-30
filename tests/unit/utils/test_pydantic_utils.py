from fast_fluids.utils.pydantic_utils import BaseModel, field_names


def test_field_names() -> None:
    class ModelWithFields(BaseModel):
        first: int
        second: int
        third: int

    expected_field_names = {"first", "second", "third"}

    assert field_names(ModelWithFields) == expected_field_names
    assert field_names(ModelWithFields(first=1, second=2, third=3)) == expected_field_names
