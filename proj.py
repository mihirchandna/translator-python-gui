import tkinter as tk
from translate import Translator

def translate_text():
    text = text_entry.get()
    if text:
        translator = Translator(to_lang='hi')
        translation = translator.translate(text)
        translated_text.set(translation)

# main application window
root = tk.Tk()
root.title("Language Translator")

# widgets
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=5)
translated_text = tk.StringVar()
result_label = tk.Label(root, textvariable=translated_text, wraplength=400, justify="center", bg="lightgray")
result_label.pack(pady=10)

root.mainloop()