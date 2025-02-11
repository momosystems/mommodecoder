import tkinter as tk
from tkinter import ttk
import string


def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char in string.ascii_letters:
            is_upper = char.isupper()
            char = char.lower()
            new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                new_char = new_char.upper()
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text


def atbash_decrypt(text):
    decrypted_text = ""
    for char in text:
        if char in string.ascii_letters:
            is_upper = char.isupper()
            char = char.lower()
            new_char = chr(ord('z') - (ord(char) - ord('a')))
            if is_upper:
                new_char = new_char.upper()
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text


def detect_best_shift(text):
    common_words = ["the", "and", "that", "have", "for", "not", "with", "you", "this", "but", "hallo", "ich", "der", "die", "das", "und", "in", "zu", "den", "nicht", "von", "sie", "ist", "des", "sich", "mit", "dem", "er", "es", "ein", "auf", "so", "eine", "auch", "als", "an", "nach", "wie", "im", "für"]
    best_shift = None
    max_word_count = 0
    best_decryption = ""

    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        word_count = sum(decrypted.lower().count(word) for word in common_words)

        if word_count > max_word_count:
            max_word_count = word_count
            best_shift = shift
            best_decryption = decrypted

    return best_shift, best_decryption


def detect_encryption(text):
    shift, caesar_text = detect_best_shift(text)
    atbash_text = atbash_decrypt(text)

    return {"Caesar": caesar_text, "Atbash": atbash_text, "Shift": shift}


def on_decrypt():
    text = entry_text.get()
    results = detect_encryption(text)
    result_label.config(
        text=f"Caesar (Shift {results['Shift']}):\n{results['Caesar']}\n\nAtbash:\n{results['Atbash']}")
    show_all_button.pack(pady=5)


def show_all_shifts():
    text = entry_text.get()
    all_shifts = "\n".join([f"Shift {s}: {caesar_decrypt(text, s)}" for s in range(26)])
    result_label.config(text=f"Mögliche Caesar-Varianten:\n{all_shifts}")


# Hauptfenster erstellen
root = tk.Tk()
root.title("Multi-Decoder")
root.geometry("500x700")

# Label und Eingabefelder
ttk.Label(root, text="Verschlüsselte Nachricht:").pack(pady=5)
entry_text = ttk.Entry(root, width=40)
entry_text.pack(pady=5)

# Buttons
button = ttk.Button(root, text="Automatisch Entschlüsseln", command=on_decrypt)
button.pack(pady=10)
show_all_button = ttk.Button(root, text="Alle Caesar-Entschlüsselungen anzeigen", command=show_all_shifts)
show_all_button.pack_forget()  # Anfangs ausblenden

# Ergebnisanzeige
result_label = ttk.Label(root, text="", font=("Arial", 10), justify="left", wraplength=480)
result_label.pack(pady=20)

# Hauptloop starten
root.mainloop()
