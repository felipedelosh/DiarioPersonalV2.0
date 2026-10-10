"""
FelipdelosH
2026

Implementation of Drugs bar Graphier
"""
from tkinter import Canvas
from tkinter import LAST
from Application.Services.IGraphDrugsRenderer import IGraphDrugsRenderer
from Domain.Entities.Response import Response

class GraphDrugsRenderer(IGraphDrugsRenderer):
    def __init__(self):
        pass

    def render(self, canvas: Canvas, data: Response, options):
        """
        Enter All Drugs information {'path': 'data'}

        1. Read all Paths to extract [Drug, SUM]
        2. Draws a horizontal histogram: each row is a drug, bar length = frequency.
        """
        # VARS
        w = float(canvas["width"])
        h = float(canvas["height"])
        _SUM_DRUGS = self._getDictSumOfDrugs(data)

        if len(_SUM_DRUGS) == 0:
            return None

        self._renderDrugsHistogram(canvas, _SUM_DRUGS)

    def _getDictSumOfDrugs(self, data):
        """
        Enter Response(?, {path, "..."}, ?)
        read all druigs in path set and order.
        """
        _sum = {}

        for i in data["data"]:
            _path = str(i).split(" - ")[0]
            _drug = str(_path).split("/")[1]
            if _drug not in _sum.keys():
                _sum[_drug] = 0
            _sum[_drug] = _sum[_drug] + 1

        _sum_ordered = dict(sorted(_sum.items(), key=lambda kv: kv[1], reverse=True))
        return _sum_ordered

    # ---------- Histogram rendering ----------
    def _renderDrugsHistogram(self, canvas, data):
        _w = float(canvas["width"])
        _h = float(canvas["height"])

        # --- Plot dimensions ---
        _x_axis_origin    = _w * 0.20
        _y_axis_origin    = _h * 0.10
        _plot_max_width   = _w - (_w * 0.35)
        _plot_max_height  = _h - (_h * 0.10)
        _row_space        = (_plot_max_height / len(data)) * 0.8

        # --- Scale ---
        _max_frequency = 0
        for drug in data:
            if _max_frequency < data[drug]:
                _max_frequency = data[drug]

        self._renderDrugsHistogramAixis(canvas, _x_axis_origin, _y_axis_origin,
                                        _plot_max_width, _plot_max_height)
        self._renderDrugsHistogramScale(canvas, _x_axis_origin, _y_axis_origin,
                                        _plot_max_width, _max_frequency)
        self._renderDrugsHistogramBars(canvas, data, _w,
                                       _x_axis_origin, _y_axis_origin,
                                       _plot_max_width, _row_space, _max_frequency)

    def _renderDrugsHistogramAixis(self, canvas, x_origin, y_origin, plot_w, plot_h):
        # X axis
        canvas.create_line(x_origin, y_origin,
                           x_origin + plot_w, y_origin, arrow=LAST)
        # Y axis
        canvas.create_line(x_origin, y_origin,
                           x_origin, plot_h, arrow=LAST)

    def _renderDrugsHistogramScale(self, canvas, x_origin, y_origin, plot_w, max_freq):
        _divisions = 10
        _scale_step = plot_w / _divisions
        for i in range(1, _divisions):
            x = x_origin + (_scale_step * i)
            canvas.create_line(x, y_origin - 5, x, y_origin + 5)

        # Mid & max labels
        canvas.create_text(x_origin + (_scale_step * 5), y_origin - 15,
                           text=str(round(max_freq / 2, 2)))
        canvas.create_text(x_origin + (_scale_step * 10), y_origin - 15,
                           text=str(max_freq))

    def _renderDrugsHistogramBars(self, canvas, data, w,
                                  x_origin, y_origin,
                                  plot_w, row_space, max_freq):
        _counter = 1
        for drug in data:
            _y_pos = (row_space * _counter) + y_origin

            # Drug label
            canvas.create_text(w * 0.07, _y_pos, text=drug)

            # Bar
            _frequency_ratio = data[drug] / max_freq
            _bar_x0 = x_origin
            _bar_y0 = _y_pos - 5
            _bar_x1 = x_origin + (plot_w * _frequency_ratio)
            _bar_y1 = _y_pos + 5

            canvas.create_rectangle(_bar_x0, _bar_y0, _bar_x1, _bar_y1, fill="blue")

            _counter = _counter + 1
