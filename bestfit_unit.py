# -*- coding: utf-8 -*-

"""
Best fit unit test

The purpose of this unit test is to verify that the best fit translation
algorithm works as expected. The test data is loaded from a JSON file
(best_fit_translation.json) and the results are displayed in a GUI window.

We are trying to find the best fit translation between two sets of ball
positions. The first set is the theoretical ball positions, the second set is
the measured ball positions. The measured ball positions are shifted by a
random amount in x and y direction. The best fit translation algorithm should
find the correct shift in x and y direction.

The ``best_fit_translation`` function is called with the following arguments:
- ``set1``: Theoretical ball positions
- ``set2``: Measured ball positions
- ``radius``: Ball radius

It returns the following values:
- ``dx``: Shift in x direction
- ``dy``: Shift in y direction
- ``error``: Error value (not used in this unit test, could be useful for
  debugging purposes, but clearly optional here)

The ultimate goal of this unit test is to verify that the ``dx`` and ``dy``
values returned by the ``best_fit_translation`` function are equal to the
random shift in x and y direction that was applied to the measured ball
positions. If it works as expected, the corrected ball positions should be
exactly on top of the measured ball positions.
"""

# pylint: disable=invalid-name  # Allows short reference names like x, y, ...

import json

from guidata.qthelpers import qt_app_context
from guiqwt.plot import ImageDialog

from processing import best_fit_translation
from vistools import add_circles


def load_best_fit_translation_data() -> list:
    """Load data"""
    with open("best_fit_translation.json") as f:
        data = json.load(f)
    return data


def test():
    """Test"""
    with qt_app_context():
        data = load_best_fit_translation_data()
        for index, kwargs in enumerate(data):
            set1 = kwargs["set1"]
            set2 = kwargs["set2"]
            radius = kwargs["radius"]
            # Note: the radius is not necessarily useful for the
            # best_fit_translation function, but it is at least
            # used for visualization purposes in this unit test.

            dx, dy, error = best_fit_translation(set1, set2, radius)
            print(f"{index}: dx = {dx}, dy = {dy}, error = {error}")

            b_theo = [(x, y, radius) for x, y in set1]
            b_meas = [(x, y, radius) for x, y in set2]

            # Radius is halved just for visualization purposes (it allows
            # us to see the balls better when they are on top of each other)
            b_corr = [(x + dx, y + dy, radius / 2) for x, y in set1]

            # Calculate plot limits
            xmin = min([x - radius for x, _, _ in b_theo])
            xmin = min(xmin, min([x - radius for x, _, _ in b_meas]))
            xmin = min(xmin, min([x - radius for x, _, _ in b_corr]))
            xmax = max([x + radius for x, _, _ in b_theo])
            xmax = max(xmax, max([x + radius for x, _, _ in b_meas]))
            xmax = max(xmax, max([x + radius for x, _, _ in b_corr]))
            ymin = min([y - radius for _, y, _ in b_theo])
            ymin = min(ymin, min([y - radius for _, y, _ in b_meas]))
            ymin = min(ymin, min([y - radius for _, y, _ in b_corr]))
            ymax = max([y + radius for _, y, _ in b_theo])
            ymax = max(ymax, max([y + radius for _, y, _ in b_meas]))
            ymax = max(ymax, max([y + radius for _, y, _ in b_corr]))
            xmin -= (xmax - xmin) / 4
            xmax += (xmax - xmin) / 4
            ymin -= (ymax - ymin) / 4
            ymax += (ymax - ymin) / 4

            dlg = ImageDialog(f"Best fit translation - Data set {index + 1}")
            plot = dlg.get_plot()
            plot.set_axis_limits(plot.X_BOTTOM, xmin, xmax)
            plot.set_axis_limits(plot.Y_LEFT, ymin, ymax)
            # Theoretical ball positions:
            add_circles(plot, b_theo, color="green")
            # Measured ball positions:
            add_circles(plot, b_meas, color="yellow")
            # Corrected ball positions (should be on top of measured positions):
            add_circles(plot, b_corr, color="blue")
            dlg.exec()


if __name__ == "__main__":
    test()
