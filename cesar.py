import tkinter as tk
from tkinter import messagebox


def caesar_decrypt(ciphertext: str, shift: int):
    result = []

    shift = shift % 26

    for ch in ciphertext:
        if 'A' <= ch <= 'Z':
            base = ord('A')
            new_pos = (ord(ch) - base - shift) % 26
            result.append(chr(base + new_pos))
        elif 'a' <= ch <= 'z':
            base = ord('a')
            new_pos = (ord(ch) - base - shift) % 26
            result.append(chr(base + new_pos))
        else:
            result.append(ch)

    return "".join(result)


def caesar_encrypt(ciphertext: str, shift: int):
    result = []

    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            offset = (ord(ch) - base + shift) % 26
            # result += ch(base + offset)
            result.append(chr(base + offset))
        else:
            result.append(ch)
    return "".join(result)


def on_decrypt():
    text = entry_text.get("1.0", tk.END).rstrip("\n")
    shift_str = entry_shift.get()

    try:
        shift = int(shift_str)
    except ValueError:
        messagebox.showerror("Error", "Posun musi byt cele cislo (napr. 3).")
        return

    decrypted = caesar_decrypt(text, shift)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted)
    output_text.config(state="disabled")


def on_encrypt():
    text = entry_text.get("1.0", tk.END).rstrip("\n")
    shift_str = entry_shift.get()

    try:
        shift = int(shift_str)
    except ValueError:
        messagebox.showerror("Error", "Posun musi byt cele cislo (napr. 3).")
        return

    encrypted = caesar_encrypt(text, shift)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted)
    output_text.config(state="disabled")


root = tk.Tk()
root.title("Desifrovac Caesarovej sifry")

label_text = tk.Label(root, text="Vstupny text:")
label_text.pack(padx=10, pady=(10, 0), anchor="w")

entry_text = tk.Text(root, height=5, width=50)
entry_text.pack(padx=10, pady=5)

frame_shift = tk.Frame(root)
frame_shift.pack(padx=10, pady=5, anchor="w")

label_shift = tk.Label(frame_shift, text="Posun:")
label_shift.pack(side=tk.LEFT)

entry_shift = tk.Entry(frame_shift, width=5)
entry_shift.pack(side=tk.LEFT, padx=(5, 0))

frame_buttons = tk.Frame(root)
frame_buttons.pack(padx=10, pady=10)

btn_decrypt = tk.Button(frame_buttons, text="Desifrovat",
                        width=15, command=on_decrypt)
btn_decrypt.pack(side=tk.LEFT, padx=5)
btn_encrypt = tk.Button(frame_buttons, text="Sifrovat",
                        width=15, command=on_encrypt)
btn_encrypt.pack(side=tk.LEFT, padx=5)

label_output = tk.Label(root, text="Vysledok:")
label_output.pack(padx=10, pady=(10, 0), anchor="w")

output_text = tk.Text(root, height=5, width=50, state="disabled")
output_text.pack(padx=10, pady=(5, 10))

root.mainloop()
