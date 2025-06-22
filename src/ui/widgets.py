import tkinter as tk

class UIWidgets:
    def __init__(self, ui):
        self.ui = ui
        self.colors = ui.colors
        self.fonts = ui.fonts

    def add_hover_effects(self, button):
        def on_enter(e):
            if button['text'] == "":
                button.config(bg=self.colors['hover'], relief='raised')
        def on_leave(e):
            if button['text'] == "":
                button.config(bg='white', relief='raised')
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def create_board_buttons(self, parent, handle_click):
        buttons = [[None for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                btn = tk.Button(
                    parent, text="", font=self.fonts['button'], width=3, height=1,
                    bg='white', fg=self.colors['bg_primary'], relief='flat', bd=0,
                    highlightthickness=0, command=lambda row=r, col=c: handle_click(row, col),
                    cursor='hand2', activebackground=self.colors['hover']
                )
                self.add_hover_effects(btn)
                btn.grid(row=r, column=c, padx=4, pady=4, sticky='nsew')
                buttons[r][c] = btn
            parent.grid_rowconfigure(r, weight=1)
        for c in range(3):
            parent.grid_columnconfigure(c, weight=1)
        return buttons
