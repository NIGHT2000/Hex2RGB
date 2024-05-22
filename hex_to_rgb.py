import tkinter as tk
import re

def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def is_valid_input(value):
    return bool(re.match("^([0-9a-fA-F]{6})$", value))

def convert():
    hex_color = entry_hex.get()

    if not is_valid_input(hex_color):
        result_label.config(text="输入错误，请输入有效的16进制颜色值")
        return

    try:
        r, g, b = hex_to_rgb(hex_color)
    except ValueError:
        result_label.config(text="转换错误，请输入有效的16进制颜色值")
        return

    result_label.config(text="对应的RGB值为：R={}, G={}, B={}".format(r, g, b))

def copy_rgb_code():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))

root = tk.Tk()
root.title("16进制转RGB")

label_hex = tk.Label(root, text="16进制颜色值（如：FF00FF，无#）：")
label_hex.grid(row=0, column=0)
entry_hex = tk.Entry(root)
entry_hex.grid(row=0, column=1)

convert_button = tk.Button(root, text="转换", command=convert)
convert_button.grid(row=1, column=0, columnspan=2)

copy_button = tk.Button(root, text="复制", command=copy_rgb_code)
copy_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
