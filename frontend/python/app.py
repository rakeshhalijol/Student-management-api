import tkinter as tk
import requests
import json
def send_data(data:dict):
    url = "http://127.0.0.1:8000/student"
    data = json.dumps(data)
    response = requests.post(url=url,data=data)
    print(response)
    
def on_submit():
    name = name_entry.get()
    rno = rno_entry.get()
    section = section_entry.get()
    m1 = marks1_entry.get()
    m2 = marks2_entry.get()
    m3 = marks3_entry.get()
    m4 = marks4_entry.get()
    m5 = marks5_entry.get()
    m6 = marks6_entry.get()

    data = {
        "name":name,
        "rno" : rno,
        "section": section,
        "marks" : [int(m1),int(m2),int(m3),int(m4),int(m5),int(m6)]
    }
    print(data)
    send_data(data)

root = tk.Tk()
root.title("Student Information")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

rno_label = tk.Label(root, text="Roll Number:")
rno_label.grid(row=1, column=0, padx=5, pady=5)

rno_entry = tk.Entry(root)
rno_entry.grid(row=1, column=1, padx=5, pady=5)

section_label = tk.Label(root, text="Section:")
section_label.grid(row=2, column=0, padx=5, pady=5)

section_entry = tk.Entry(root)
section_entry.grid(row=2, column=1, padx=5, pady=5)

marks1_label = tk.Label(root, text="Marks 1:")
marks1_label.grid(row=3, column=0, padx=5, pady=5)

marks1_entry = tk.Entry(root)
marks1_entry.grid(row=3, column=1, padx=5, pady=5)

marks2_label = tk.Label(root, text="Marks 2:")
marks2_label.grid(row=4, column=0, padx=5, pady=5)

marks2_entry = tk.Entry(root)
marks2_entry.grid(row=4, column=1, padx=5, pady=5)

marks3_label = tk.Label(root, text="Marks 3:")
marks3_label.grid(row=5, column=0, padx=5, pady=5)

marks3_entry = tk.Entry(root)
marks3_entry.grid(row=5, column=1, padx=5, pady=5)

marks4_label = tk.Label(root, text="Marks 4:")
marks4_label.grid(row=6, column=0, padx=5, pady=5)

marks4_entry = tk.Entry(root)
marks4_entry.grid(row=6, column=1, padx=5, pady=5)

marks5_label = tk.Label(root, text="Marks 5:")
marks5_label.grid(row=7, column=0, padx=5, pady=5)

marks5_entry = tk.Entry(root)
marks5_entry.grid(row=7, column=1, padx=5, pady=5)

marks6_label = tk.Label(root, text="Marks 6:")
marks6_label.grid(row=8, column=0, padx=5, pady=5)

marks6_entry = tk.Entry(root)
marks6_entry.grid(row=8, column=1, padx=5, pady=5)

button = tk.Button(root, text="send data",command=on_submit)

# Use the grid layout manager to place the button in the window
button.grid(row=9, column=1)

root.mainloop()