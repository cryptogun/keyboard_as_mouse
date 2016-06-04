# /usr/bin/env python
# coding: utf-8
############################################
# General setting. change it if you want.
enable_character_positioning=True

left_click_key="ctrl+space"
double_left_click_key="ctrl+space+space"
right_click_key="alt+space"

select_text_begin_key="ctrl+shift+u"
select_text_end_key="ctrl+shift+o"

move_left_slow_key="ctrl+shift+j"
move_right_slow_key="ctrl+shift+l"
move_up_slow_key="ctrl+shift+i"
move_down_slow_key="ctrl+shift+k"

move_left_fast_key="alt+j"
move_right_fast_key="alt+l"
move_up_fast_key="alt+i"
move_down_fast_key="alt+k"

zone11_key="ctrl+7"
zone21_key="ctrl+8"
zone31_key="ctrl+9"
zone41_key="ctrl+0"

zone12_key="ctrl+u"
zone22_key="ctrl+i"
zone32_key="ctrl+o"
zone42_key="ctrl+p"

zone13_key="ctrl+j"
zone23_key="ctrl+k"
zone33_key="ctrl+l"
zone43_key="ctrl+;"

zone14_key="ctrl+m"
zone24_key="ctrl+,"
zone34_key="ctrl+."
zone44_key="ctrl+/"

############################################


import keyboard
import ctypes
import time

import cursor_position
'''
MOUSEEVENTF_MOVE = 0x0001 # mouse move 
MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down 
MOUSEEVENTF_LEFTUP = 0x0004 # left button up 
MOUSEEVENTF_RIGHTDOWN = 0x0008 # right button down 
MOUSEEVENTF_RIGHTUP = 0x0010 # right button up 
MOUSEEVENTF_MIDDLEDOWN = 0x0020 # middle button down 
MOUSEEVENTF_MIDDLEUP = 0x0040 # middle button up 
MOUSEEVENTF_WHEEL = 0x0800 # wheel button rolled 
MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move 
'''
def move_left(pixel):
	ctypes.windll.user32.mouse_event(0x0001, -pixel, 0, 0, 0)
def move_right(pixel):
	ctypes.windll.user32.mouse_event(0x0001, pixel, 0, 0, 0)
def move_up(pixel):
	ctypes.windll.user32.mouse_event(0x0001, 0, -pixel, 0, 0)
def move_down(pixel):
	ctypes.windll.user32.mouse_event(0x0001, 0, pixel, 0, 0)

def left_click():
	ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
	ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
def right_click():
	ctypes.windll.user32.mouse_event(0x0008, 0, 0, 0, 0)
	ctypes.windll.user32.mouse_event(0x0010, 0, 0, 0, 0)

def double_left_click():
	left_click()
	left_click()
def double_right_click():
	right_click()
	right_click()

pos_select_left=None
pos_select_right=None
def select_text_begin():
	"""Text selection begin. Record left position(relative to 2^16)."""
	global pos_select_left
	pos_select_left = cursor_position.get_cursor_position()
def select_text_end():
	"""Text selection done. Simulating the selection procedure."""
	#left click to clear selected text. In case that you need to adjust text length.
	left_click()
	
	global pos_select_left, pos_select_right
	pos_select_right = cursor_position.get_cursor_position()

	ctypes.windll.user32.mouse_event(0x0001+0x8000, pos_select_left[0], pos_select_left[1], 0, 0)
	#Wait or fail.
	time.sleep(0.1)
	ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
	ctypes.windll.user32.mouse_event(0x0001+0x8000, pos_select_right[0], pos_select_right[1], 0, 0)
	ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)


#click control:
##single click:
keyboard.add_hotkey(left_click_key, lambda: left_click())
keyboard.add_hotkey(right_click_key, lambda: right_click())

#double click:
keyboard.add_hotkey(double_left_click_key, lambda: double_left_click())

#Text select control:
keyboard.add_hotkey(select_text_begin_key, lambda: select_text_begin())
keyboard.add_hotkey(select_text_end_key, lambda: select_text_end())

#Cursor movement control:
##fast speed:
keyboard.add_hotkey(move_left_fast_key, lambda: move_left(16))
keyboard.add_hotkey(move_right_fast_key, lambda: move_right(16))
keyboard.add_hotkey(move_up_fast_key, lambda: move_up(16))
keyboard.add_hotkey(move_down_fast_key, lambda: move_down(16))

##slow speed:
keyboard.add_hotkey(move_left_slow_key, lambda: move_left(4))
keyboard.add_hotkey(move_right_slow_key, lambda: move_right(4))
keyboard.add_hotkey(move_up_slow_key, lambda: move_up(4))
keyboard.add_hotkey(move_down_slow_key, lambda: move_down(4))

if enable_character_positioning:
	##Full screen divition using:
	"""
	7890
	uiop
	jkl;
	m,./
	"""
	full_width_1 = 65536 / 4
	full_height_1 = 65536 / 4
	x1 = int(0.5*full_width_1)
	x2 = int(1.5*full_width_1)
	x3 = int(2.5*full_width_1)
	x4 = int(3.5*full_width_1)
	y1 = int(0.5*full_height_1)
	y2 = int(1.5*full_height_1)
	y3 = int(2.5*full_height_1)
	y4 = int(3.5*full_height_1)
	keyboard.add_hotkey(zone11_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x1, y1, 0, 0))
	keyboard.add_hotkey(zone21_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x2, y1, 0, 0))
	keyboard.add_hotkey(zone31_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x3, y1, 0, 0))
	keyboard.add_hotkey(zone41_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x4, y1, 0, 0))

	keyboard.add_hotkey(zone12_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x1, y2, 0, 0))
	keyboard.add_hotkey(zone22_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x2, y2, 0, 0))
	keyboard.add_hotkey(zone32_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x3, y2, 0, 0))
	keyboard.add_hotkey(zone42_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x4, y2, 0, 0))

	keyboard.add_hotkey(zone13_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x1, y3, 0, 0))
	keyboard.add_hotkey(zone23_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x2, y3, 0, 0))
	keyboard.add_hotkey(zone33_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x3, y3, 0, 0))
	keyboard.add_hotkey(zone43_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x4, y3, 0, 0))

	keyboard.add_hotkey(zone14_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x1, y4, 0, 0))
	keyboard.add_hotkey(zone24_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x2, y4, 0, 0))
	keyboard.add_hotkey(zone34_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x3, y4, 0, 0))
	keyboard.add_hotkey(zone44_key, lambda: ctypes.windll.user32.mouse_event(0x0001+0x8000, x4, y4, 0, 0))




if __name__ == "__main__":
	print("keyboard mouse started.")
	# Usage:
	print("*************************************************")
	print("Usage:")
	print("Left  click            :\t"+left_click_key)
	print("Right click            :\t"+right_click_key)
	print("Double left click      :\t"+double_left_click_key)
	print("Text selection begin   :\t"+select_text_begin_key)
	print("Text selection ended   :\t"+select_text_end_key)
	print("Fast move jlik         :\t"+move_left_fast_key)
	print("Slow move jlik         :\t"+move_left_slow_key)
	print("Full screen positioning:")
	print("                           "+zone11_key+"890")
	print("""                      \t\tjkl;
                      \t\tm,./""")
	print("Exit program           :\tesc,esc,esc")
	print("************************************************")

	# Blocks until you press esc for 3 times.
	keyboard.wait('esc, esc, esc')

	print("keyboard mouse closed.\n3 seconds to exit...")
	time.sleep(3)

	'''
	remove_hotkey lack of documentation.
	keyboard.remove_hotkey(key_handlers)
	'''