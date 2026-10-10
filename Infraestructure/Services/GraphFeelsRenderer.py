"""
FelipedelosH
2026

Implementation of Feels bar Graphier
"""
from tkinter import Canvas
from tkinter import LAST
from Application.Services.IGraphFeelsRenderer import IGraphFeelsRenderer
from Domain.Entities.Response import Response

class GraphFeelsRenderer(IGraphFeelsRenderer):
    def __init__(self):
        pass

    def render(self, canvas: Canvas, data: Response, options):
        """
        Enter all Feels information {'path': 'data'}

        1. Read all Paths to extract [Feeling, SUM]
        2. Draws a horizontal histogram: each row is a feeling, bar length = frequency.
        """
        # VARS
        w = float(canvas["width"])
        h = float(canvas["height"])

        _SUM_FEELS = self._getDictSumOfFeels(data)

        if len(_SUM_FEELS) == 0:
            return None

        self._renderFeelsHistogram(canvas, _SUM_FEELS)

    def _getDictSumOfFeels(self, data):
        """
        Enter Response(?, {path, "..."}, ?)
        Read all feels in path set and order.
        """
        _sum = {}

        for i in data["data"]:
            _feel = data["data"][i]
            if _feel not in _sum.keys():
                _sum[_feel] = 0
            _sum[_feel] = _sum[_feel] + 1

        _sum_ordered = dict(sorted(_sum.items(), key=lambda kv: kv[1], reverse=True))
        return _sum_ordered

    # ---------- Histogram rendering ----------
    def _renderFeelsHistogram(self, canvas, data):
        _w = float(canvas["width"])
        _h = float(canvas["height"])

        # --- Limit to TOP 10 ---
        _MAX_FEELS_TO_PAINT = 10
        if len(data) > _MAX_FEELS_TO_PAINT:
            data = dict(list(data.items())[:_MAX_FEELS_TO_PAINT])

        # --- Plot dimensions ---
        _x_axis_origin    = _w * 0.20
        _y_axis_origin    = _h * 0.10
        _plot_max_width   = _w - (_w * 0.35)
        _plot_max_height  = _h - (_h * 0.10)
        _row_space        = (_plot_max_height / len(data)) * 0.8

        # --- Scale ---
        _max_frequency = 0
        for feel in data:
            if _max_frequency < data[feel]:
                _max_frequency = data[feel]

        self._renderFeelsHistogramAixis(canvas, _x_axis_origin, _y_axis_origin,
                                        _plot_max_width, _plot_max_height)
        self._renderFeelsHistogramScale(canvas, _x_axis_origin, _y_axis_origin,
                                        _plot_max_width, _max_frequency)
        self._renderFeelsHistogramBars(canvas, data, _w,
                                       _x_axis_origin, _y_axis_origin,
                                       _plot_max_width, _row_space, _max_frequency)

    def _renderFeelsHistogramAixis(self, canvas, x_origin, y_origin, plot_w, plot_h):
        # X axis
        canvas.create_line(x_origin, y_origin,
                           x_origin + plot_w, y_origin, arrow=LAST)
        # Y axis
        canvas.create_line(x_origin, y_origin,
                           x_origin, plot_h, arrow=LAST)

    def _renderFeelsHistogramScale(self, canvas, x_origin, y_origin, plot_w, max_freq):
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

    def _renderFeelsHistogramBars(self, canvas, data, w,
                                x_origin, y_origin,
                                plot_w, row_space, max_freq):
        _counter = 1
        for feel in data:
            _y_pos = (row_space * _counter) + y_origin

            # Feeling label
            canvas.create_text(w * 0.02, _y_pos, text=feel, anchor="w")

            # Bar
            _frequency_ratio = data[feel] / max_freq
            _bar_x0 = x_origin
            _bar_y0 = _y_pos - 5
            _bar_x1 = x_origin + (plot_w * _frequency_ratio)
            _bar_y1 = _y_pos + 5

            canvas.create_rectangle(_bar_x0, _bar_y0, _bar_x1, _bar_y1, fill="blue")

            _counter = _counter + 1
