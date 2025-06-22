import pytest
from cfbuild import Dataset


def test_dataset_initialization_empty():
    """Test that cfbuild.Dataset can be initialized with no arguments."""
    try:
        ds = Dataset()
        # Further checks could be added here if default state is expected
        assert ds.attributes == {}
        assert ds.variables == {}
        assert ds.dimensions == {}
        assert ds.dataset is None  # Expecting no netCDF4.Dataset object internally yet
    except Exception as e:
        pytest.fail(f"Dataset initialization with no arguments failed: {e}")


def test_dataset_initialization_with_nonexistent_file():
    """Test that cfbuild.Dataset raises FileNotFoundError for a non-existent file."""
    with pytest.raises(FileNotFoundError):
        Dataset("non_existent_file.nc")


# A more complex test to ensure pytest is running and can import the package code.
# This is a placeholder for more meaningful tests later.
def test_example_addition():
    assert 1 + 1 == 2
