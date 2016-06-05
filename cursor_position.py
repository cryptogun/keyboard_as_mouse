#!/usr/bin/env python
# coding: utf-8

"""Return current cursor position relative to cursor resolution 2^16 x 2^16."""
import ctypes

class _point_t(ctypes.Structure):
    """Cursor point coordinate relative to screen resolution."""
    _fields_ = [
                ('x',  ctypes.c_long),
                ('y',  ctypes.c_long),
               ]

def get_cursor_position():
    point = _point_t()

    result = ctypes.windll.user32.GetCursorPos(ctypes.pointer(point))
    window_w, window_h = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)

    #point.x : window width == x : 65536
    x = int(point.x * 65536 / window_w)
    y = int(point.y * 65536 / window_h)
    if result:  return (x, y)
    else:       return None


if __name__ == '__main__':

    pos=get_cursor_position()
    # get current mouse position then x coordinate *2.
    ctypes.windll.user32.mouse_event(0x0001+0x8000, pos[0] * 2, pos[1], 0, 0)


'''
# Another way using System module.
import System

# Get the mouse position
mp = System.Windows.Forms.Control.MousePosition

# Extract the coordinates
xPos = mp.X
yPos = mp.Y

print xPos,yPos
'''