import random
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox

class GuessTheNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Guess the Number')
        self.root.resizable(True, True)
        self.root.minsize(320, 180)

        self.base_width = 400
        self.base_height = 240

        self.title_font = tkfont.Font(family='Arial', size=14, weight='bold')
        self.text_font = tkfont.Font(family='Arial', size=12)
        self.feedback_font = tkfont.Font(family='Arial', size=11)
        self.button_font = tkfont.Font(family='Arial', size=12)
        self.entry_font = tkfont.Font(family='Arial', size=12)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.secret = random.randint(1, 100)

        self.main_frame = tk.Frame(root, padx=16, pady=16)
        self.main_frame.grid(sticky='nsew')
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)

        self.title_label = tk.Label(
            self.main_frame,
            text='Welcome to Guess the Number!',
            font=self.title_font,
            anchor='w',
            justify='left',
            wraplength=self.base_width - 64,
        )
        self.title_label.grid(row=0, column=0, columnspan=2, sticky='ew', pady=(0, 8))

        self.instruction_label = tk.Label(
            self.main_frame,
            text='Guess a number between 1 and 100.',
            font=self.text_font,
            anchor='w',
            justify='left',
            wraplength=self.base_width - 64,
        )
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky='ew')

        self.guess_entry = tk.Entry(self.main_frame, font=self.entry_font)
        self.guess_entry.grid(row=2, column=0, sticky='ew', pady=12)
        self.guess_entry.focus()

        self.guess_button = tk.Button(self.main_frame, text='Guess', command=self.check_guess, font=self.button_font)
        self.guess_button.grid(row=2, column=1, sticky='ew', padx=(8, 0), pady=12)

        self.feedback_label = tk.Label(
            self.main_frame,
            text='',
            font=self.feedback_font,
            fg='blue',
            anchor='w',
            justify='left',
            wraplength=self.base_width - 64,
        )
        self.feedback_label.grid(row=3, column=0, columnspan=2, sticky='ew', pady=(0, 12))

        self.reset_button = tk.Button(self.main_frame, text='New Game', command=self.reset_game, font=self.button_font)
        self.reset_button.grid(row=4, column=0, columnspan=2, sticky='ew')

        self.root.bind('<Return>', lambda event: self.check_guess())
        self.root.bind('<Configure>', self.on_resize)

    def on_resize(self, event):
        width = max(event.width, self.base_width)
        height = max(event.height, self.base_height)
        scale = min(max(width / self.base_width, height / self.base_height), 3.0)

        self.title_font.configure(size=max(14, int(14 * scale)))
        self.text_font.configure(size=max(12, int(12 * scale)))
        self.feedback_font.configure(size=max(11, int(11 * scale)))
        self.button_font.configure(size=max(12, int(12 * scale)))
        self.entry_font.configure(size=max(12, int(12 * scale)))

        wrap_length = max(160, width - 64)
        self.title_label.configure(wraplength=wrap_length)
        self.instruction_label.configure(wraplength=wrap_length)
        self.feedback_label.configure(wraplength=wrap_length)

    def check_guess(self):
        guess_text = self.guess_entry.get().strip()
        if not guess_text:
            self.feedback_label.config(text='Please enter a number.', fg='red')
            return

        try:
            guess = int(guess_text)
        except ValueError:
            self.feedback_label.config(text='Enter a valid integer between 1 and 100.', fg='red')
            return

        if guess < 1 or guess > 100:
            self.feedback_label.config(text='Please choose a number between 1 and 100.', fg='red')
            return

        if guess < self.secret:
            self.feedback_label.config(text='Too low! Try again.', fg='orange')
        elif guess > self.secret:
            self.feedback_label.config(text='Too high! Try again.', fg='orange')
        else:
            self.feedback_label.config(text='Congratulations! You guessed the number!', fg='green')
            messagebox.showinfo('Correct!', f'You guessed it! The number was {self.secret}.')
            self.disable_input()

    def disable_input(self):
        self.guess_entry.config(state='disabled')
        self.guess_button.config(state='disabled')

    def reset_game(self):
        self.secret = random.randint(1, 100)
        self.feedback_label.config(text='')
        self.guess_entry.config(state='normal')
        self.guess_button.config(state='normal')
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

if __name__ == '__main__':
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()