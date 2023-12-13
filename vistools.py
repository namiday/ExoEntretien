# -*- coding: utf-8 -*-

"""
Visualization tools (based on guiqwt)
"""

# pylint: disable=invalid-name  # Allows short reference names like x, y, ...

from guiqwt.baseplot import BasePlot
from guiqwt.builder import make
from guiqwt.shapes import PolygonShape


def set_shape_color(shape: PolygonShape, color: str) -> None:
    """Set circle color"""
    param = shape.shapeparam
    param.line.color = param.fill.color = color
    param.fill.alpha = 0.3
    param.fill.style = "SolidPattern"
    param.update_shape(shape)
    plot = shape.plot()
    if plot is not None:
        shape.plot().replot()


def add_shape_to_plot(plot: BasePlot, shape: PolygonShape, color: str = None):
    """Add shape to plot"""
    shape.set_readonly(True)
    shape.set_resizable(False)
    shape.set_movable(False)
    plot.add_item(shape)
    if color is not None:
        set_shape_color(shape, color)
    else:
        plot.replot()


def add_circles(plot, circles, color="yellow"):
    """Add circles to plot"""
    for circle in circles:
        x, y, r = circle
        add_shape_to_plot(plot, make.circle(x - r, y, x + r, y), color)
