import sys
import os
import webbrowser
from tkinter import ttk, Label
import tkinter as tk

try:
	import easygui as e
except ModuleNotFoundError:
	os.system('pip install easygui')
	try:
		import easygui as e
	except ModuleNotFoundError:
		tk.messagebox.showerror("错误",
		                        "您未安装easygui库，这可能是因为您的python未完全安装，请访问'https://www.python.org/downloads/windows'以重新下载python")
		url = 'https://www.python.org/downloads/windows'
		webbrowser.open(url)
		sys.exit()
from tkinter import filedialog


def number_planner():
	from_number = e.enterbox(title="请输入", msg="从几开始？")
	if from_number is None or from_number == '':
		e.msgbox("您未输入数字")
		return
	try:
		from_number = int(from_number)
	except ValueError:
		e.msgbox("您输入的不是数字")
		return

	to_number = e.enterbox(title="请输入", msg="到几结束？")
	if to_number is None or to_number == '':
		e.msgbox("您未输入数字")
		return
	try:
		to_number = int(to_number)
	except ValueError:
		e.msgbox("您输入的不是数字")
		return

	to_path = filedialog.asksaveasfilename(title="请选择保存位置", defaultextension=".txt")
	if not to_path:
		return
	try:
		os.remove(to_path)
	except FileNotFoundError:
		pass
	with open(to_path, "w", encoding="utf-8") as f:
		pass

	root = tk.Tk()
	root.geometry('600x400+200+200')
	root.title('进度')
	var = tk.IntVar()
	pb = ttk.Progressbar(root, orient='horizontal', length=280, variable=var)
	pb.pack(expand=True)
	pb = ttk.Progressbar(root, length=280, mode='determinate')
	bei = 0
	for i in range(from_number, to_number + 1):
		global nowbai
		nowbai = i / (to_number + 1)
		label1 = Label(text="0%")
		with open(to_path, "a", encoding="utf-8") as t:
			t.write(str(i))
			t.write("\n")
			if i == t:
				t.close()
		var.set(int(nowbai))
		label1.config(text=str(nowbai))
		root.update_idletasks()

		bei = i
	var.set(int(i) + 1)
	root.update_idletasks()
	label2 = Label(text="输入已完成")
	label2.pack(root, expand=True)
	root.mainloop()


buttons = ['数字规划器', 'host修复(初始化)', "滑动关机"]
choose = e.buttonbox(title="请选择", msg="请选择你需要的功能", choices=buttons)
print(choose)

if choose == '数字规划器':
	number_planner()
elif choose == 'host修复(初始化)':
	os.startfile("bat/hosts.bat")

elif choose == "滑动关机":
	os.startfile("C:\Windows\System32\SlideToShutDown.exe")
elif choose == "注销":
	os.startfile("bat/zhu.bat")




