""" Colorbar Tests """

import numpy as np
import pytest

# mpl.use("TkAgg")
import matplotlib.pyplot as plt
import earthpy.plot as ep

plt.show = lambda: None


def test_colorbar_height(basic_image):
    """Test that the colorbar ax height matches the image axis height."""
    f, ax = plt.subplots(figsize=(5, 5))
    im = ax.imshow(basic_image, cmap="RdYlGn")
    cb = ep.colorbar(im)
    assert cb.ax.get_position().height == im.axes.get_position().height
    plt.close(f)


def test_colorbar_raises_value_error():
    """Test that a non matbplotlib axis object raises an value error."""
    with pytest.raises(AttributeError, match="requires a matplotlib"):
        ep.colorbar(list())
    plt.close()
