Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================

Traceback (most recent call last):
  File "/home/user/RTR105/1B1.py", line 5, in <module>
    matplotlib.pyplot
NameError: name 'matplotlib' is not defined
>>> import sys
>>> sys.path.append('usr/local/anaconda3/lib/python3.6/site-packages')
>>> sys.path.append('usr/local/anaconda3/lib/python2.7.10/site-packages')
>>> sys.path.append('usr/local/anaconda3/lib/python2.7.12/site-packages')
>>> sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================

Warning (from warnings module):
  File "/usr/lib/python2.7/dist-packages/matplotlib/font_manager.py", line 273
    warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.

Traceback (most recent call last):
  File "/home/user/RTR105/1B1.py", line 8, in <module>
    plt.ylaber('f(x)')
AttributeError: 'module' object has no attribute 'ylaber'
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================

Traceback (most recent call last):
  File "/home/user/RTR105/1B1.py", line 8, in <module>
    plt.ylaber('f(x)')
AttributeError: 'module' object has no attribute 'ylaber'
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================

===================== RESTART: /home/user/RTR105/1B1.py =====================

===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================

Traceback (most recent call last):
  File "/home/user/RTR105/1B1.py", line 24, in <module>
    plt.plot(x, y2, color='#60GG30')
NameError: name 'y2' is not defined
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "#60GG30"
to_rgb: Invalid rgb arg "#60GG30"
invalid hex color string "#60gg30"
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "#60GG30"
to_rgb: Invalid rgb arg "#60GG30"
invalid hex color string "#60gg30"
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "FF0000"
to_rgb: Invalid rgb arg "FF0000"
could not convert string to float: ff0000
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "04B45F"
to_rgb: Invalid rgb arg "04B45F"
invalid literal for float(): 04b45f
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "0610B4B"
to_rgb: Invalid rgb arg "0610B4B"
invalid literal for float(): 0610b4b
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "66FF33"
to_rgb: Invalid rgb arg "66FF33"
invalid literal for float(): 66ff33
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "#6FF33"
to_rgb: Invalid rgb arg "#6FF33"
invalid hex color string "#6ff33"
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
