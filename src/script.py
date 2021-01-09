import ctypes
LinesScrolling = ctypes.c_long()
Success = ctypes.windll.user32.SystemParametersInfoA(104, 0, ctypes.byref(LinesScrolling), 0)
print( Success, " | ", LinesScrolling.value)
if Success == 1 and LinesScrolling.value == 3:
    print("trying to change to 30")
    Success = ctypes.windll.user32.SystemParametersInfoA(105, 30, 0, 0)
elif Success == 1 and LinesScrolling.value == 30:
    print("trying to change to 3")
    Success = ctypes.windll.user32.SystemParametersInfoA(105, 3, 0, 0)
Success = ctypes.windll.user32.SystemParametersInfoA(104, 0, ctypes.byref(LinesScrolling), 0)
print("Current number of Scrolling Lines ", LinesScrolling.value)
