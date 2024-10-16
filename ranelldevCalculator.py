import tkinter as tk
import random
import hashlib
import base64
import webbrowser  


gay_hash = "e46304cf15868d21befe8421d06f34c89dfde360bafc5689e0aa8320df681b89"
importm = False
important = [
    
    "V2hhdCBhcmUgeW91IGRvaW5nPw==",
    "VGhlIGZ1Y2shISE=",
    "SG9seSBTaGl0ISE=",
    "VCpuZ2EgbW8h",
    "eW91J3JlIGJhbm5lZCB1c2luZyB0aGlzIGFwcA==",
    "Qm9ibyBBbXB1dGEh",
    "QmFrbGEga2EgdGFsYWdhIQ==",
    "Q2FsdmluIHRoZSAiR0FZIg=="
]

def decode_message(message):
    return base64.b64decode(message).decode('utf-8')

def toggle_important_mode():
    global importm
    importm = not importm 
    entry.delete(0, tk.END)
    entry.insert(tk.END, "YEAH" if importm else "")

def delayed_evaluation(expression):
    if not expression:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "No input to evaluate")
        return
    
    try:
        result = str(eval(expression)) 
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        if importm:
            error_message = decode_message(random.choice(important))
            entry.delete(0, tk.END)
            entry.insert(tk.END, error_message)
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "ERROR")

def evaluate_expression(expression):
    expression = expression.strip()
    print(f"User entered: '{expression}' (Length: {len(expression)})")

    entered_hash = hashlib.sha256(expression.encode()).hexdigest()
    if entered_hash == gay_hash:

        root.after(50, toggle_important_mode) 
        return 

    root.after(20, delayed_evaluation, expression)

def on_button_press(value):
    current_text = entry.get()

    if value == "=":
        evaluate_expression(current_text)
    elif value == "AC":
        entry.delete(0, tk.END)
    elif value == "C":
        entry.delete(len(current_text) - 1)
    else:
        entry.insert(tk.END, value)


dn = "RGV2ZWxvcCBieSBDaXBoZXJDYWxjTGVhayA=" 
fl = "Pj4gR0lUSFVCIEZSRUUgU09VUkNFIENPREUgPDw="
gtb = "aHR0cHM6Ly9naXRodWIuY29tL3JhbmVsbHJhbi9weXRob25fYmFzaWNfY2FsY3VsYXRvcg=="

def open_link(event):
    webbrowser.open(base64.b64decode(gtb).decode('utf-8'))

root = tk.Tk()
root.title("Python Basic Calculator")
root.geometry("470x620")
root.configure(bg='#ffccff')

entry = tk.Entry(root, width=15, borderwidth=5, font=('arial', 40), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


button_width = 5 
button_height = int(2)

def set_button_color(button):
    button.config(bg="#ff99cc", activebackground="#ff66b3")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('AC', 5, 1), ('C', 5, 2)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=button_width, borderwidth=5, height=button_height, font=('Arial', 18), command=lambda val=text: on_button_press(val))
    set_button_color(button)
    button.grid(row=row, column=col, padx=15, pady=5)

dn = base64.b64decode(dn).decode('utf-8')
fl = base64.b64decode(fl).decode('utf-8')

dl = tk.Label(root, text=dn, font=('Arial', 12), bg='#ffccff', fg='blue')
dl.grid(row=6, column=0, columnspan=4, pady=5)

fl = tk.Label(root, text=fl, font=('Arial', 10), bg='#ffccff', fg='blue', cursor="hand2")
fl.grid(row=7, column=0, columnspan=4, pady=5)
fl.bind("<Button-1>", open_link)


# Run the Tkinter event loop
root.mainloop()
