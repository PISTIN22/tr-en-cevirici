#pip install googletrans==4.0.0-rc1
#pip install pyaudio

import tkinter as tk
import speech_recognition as sr
from googletrans import Translator

def translate_speech():
    r = sr.Recognizer()
    translator = Translator()

    def recognize_speech():
        try:
            with sr.Microphone() as source:
                print("Konuşun...")
                audio_data = r.listen(source)
                text = r.recognize_google(audio_data, language='tr-TR')
                print("Söylediğiniz: " + text)
                translated_text = translator.translate(text, src='tr', dest='en')
                translation_label.config(text="Çeviri: " + translated_text.text)
                original_label.config(text="Türkçe: " + text)
        except sr.UnknownValueError:
            translation_label.config(text="Ne dediğinizi anlayamadım.")
        except sr.RequestError:
            translation_label.config(text="Sistem çalışmıyor, lütfen daha sonra tekrar deneyin.")

    def show_full_text(event, text):
        full_text_window = tk.Toplevel(root)
        full_text_window.title("Tam Metin")
        full_text_window.geometry("300x100")
        full_text_label = tk.Label(full_text_window, text=text)
        full_text_label.pack(padx=20, pady=10)

    root = tk.Tk()
    root.title("Konuşma Çevirici")

    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

    start_button = tk.Button(root, text="Konuşmayı Başlat", command=recognize_speech)
    start_button.place(relx=0.5, rely=0.4, anchor='center')

    translation_label = tk.Label(root, text="")
    translation_label.place(relx=0.5, rely=0.5, anchor='center')
    translation_label.bind("<Button-1>", lambda event: show_full_text(event, translation_label.cget("text")))

    original_label = tk.Label(root, text="")
    original_label.place(relx=0.5, rely=0.6, anchor='center')
    original_label.bind("<Button-1>", lambda event: show_full_text(event, original_label.cget("text")))

    root.mainloop()

translate_speech()
