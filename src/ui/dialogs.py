import tkinter as tk
from tkinter import Toplevel

class Dialogs:
    def __init__(self, ui):
        self.ui = ui
        self.colors = ui.colors
        self.fonts = ui.fonts
        self.window = ui.window

    def show_winner_dialog(self, winner, new_game_callback):
        dialog = Toplevel(self.window)
        dialog.title("🎉 Winner!")
        dialog.configure(bg=self.colors['bg_primary'])
        dialog.resizable(False, False)
        dialog.grab_set()
        width, height = 350, 250
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
        main_frame = tk.Frame(dialog, bg=self.colors['bg_primary'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        tk.Label(
            main_frame,
            text="🎉 Victory!",
            font=self.fonts['title'],
            bg=self.colors['bg_primary'],
            fg=self.colors['success']
        ).pack(pady=(0, 10))
        winner_color = self.colors['x_color'] if winner == "X" else self.colors['o_color']
        tk.Label(
            main_frame,
            text=f"Player {winner} wins!",
            font=self.fonts['score'],
            bg=self.colors['bg_primary'],
            fg=winner_color
        ).pack(pady=10)
        button_frame = tk.Frame(main_frame, bg=self.colors['bg_primary'])
        button_frame.pack(pady=20)
        tk.Button(
            button_frame,
            text="🎮 New Game",
            font=self.fonts['small'],
            bg=self.colors['accent'],
            fg='white',
            padx=15,
            pady=5,
            command=lambda: [dialog.destroy(), new_game_callback()],
            cursor='hand2'
        ).pack(side='left', padx=10)
        tk.Button(
            button_frame,
            text="❌ Close",
            font=self.fonts['small'],
            bg=self.colors['error'],
            fg='white',
            padx=15,
            pady=5,
            command=dialog.destroy,
            cursor='hand2'
        ).pack(side='right', padx=10)

    def show_draw_dialog(self, new_game_callback):
        dialog = Toplevel(self.window)
        dialog.title("🤝 Draw")
        dialog.configure(bg=self.colors['bg_primary'])
        dialog.resizable(False, False)
        dialog.grab_set()
        width, height = 300, 200
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
        main_frame = tk.Frame(dialog, bg=self.colors['bg_primary'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        tk.Label(
            main_frame,
            text="🤝 Draw!",
            font=self.fonts['title'],
            bg=self.colors['bg_primary'],
            fg=self.colors['warning']
        ).pack(pady=(0, 10))
        tk.Label(
            main_frame,
            text="Nobody won this time",
            font=self.fonts['score'],
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary']
        ).pack(pady=10)
        button_frame = tk.Frame(main_frame, bg=self.colors['bg_primary'])
        button_frame.pack(pady=20)
        tk.Button(
            button_frame,
            text="🎮 New Game",
            font=self.fonts['small'],
            bg=self.colors['accent'],
            fg='white',
            padx=15,
            pady=5,
            command=lambda: [dialog.destroy(), new_game_callback()],
            cursor='hand2'
        ).pack(side='left', padx=10)
        tk.Button(
            button_frame,
            text="❌ Close",
            font=self.fonts['small'],
            bg=self.colors['error'],
            fg='white',
            padx=15,
            pady=5,
            command=dialog.destroy,
            cursor='hand2'
        ).pack(side='right', padx=10)

    def show_instructions(self):
        dialog = Toplevel(self.window)
        dialog.title("📖 How to Play")
        dialog.configure(bg=self.colors['bg_primary'])
        dialog.resizable(False, False)
        dialog.grab_set()
        width, height = 400, 350
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
        main_frame = tk.Frame(dialog, bg=self.colors['bg_primary'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        tk.Label(
            main_frame,
            text="📖 How to Play",
            font=self.fonts['title'],
            bg=self.colors['bg_primary'],
            fg=self.colors['text_primary']
        ).pack(pady=(0, 20))
        instructions_text = """
🎯 Goal:
Get three identical symbols in a row
(horizontal, vertical or diagonal)

🎮 How to play:
• Players take turns to place their symbol
• Click on an empty cell to play
• The first player to get 3 in a row wins
• If all cells are filled and no one wins, it's a draw

🏆 Scoring:
• Each win gives 1 point
• Stats are kept between games
• Use the menu to reset scores
        """
        tk.Label(
            main_frame,
            text=instructions_text,
            font=self.fonts['small'],
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary'],
            justify='left'
        ).pack(pady=10)
        tk.Button(
            main_frame,
            text="✅ Got it",
            font=self.fonts['score'],
            bg=self.colors['success'],
            fg='white',
            padx=20,
            pady=10,
            command=dialog.destroy,
            cursor='hand2'
        ).pack(pady=20)

    def show_about(self):
        dialog = Toplevel(self.window)
        dialog.title("ℹ️ About")
        dialog.configure(bg=self.colors['bg_primary'])
        dialog.resizable(False, False)
        dialog.grab_set()
        width, height = 350, 250
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
        main_frame = tk.Frame(dialog, bg=self.colors['bg_primary'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        tk.Label(
            main_frame,
            text="🎮 Tic Tac Toe",
            font=self.fonts['title'],
            bg=self.colors['bg_primary'],
            fg=self.colors['text_primary']
        ).pack(pady=(0, 10))
        tk.Label(
            main_frame,
            text="Python Edition",
            font=self.fonts['score'],
            bg=self.colors['bg_primary'],
            fg=self.colors['accent']
        ).pack(pady=(0, 20))
        info_text = """
✨ Improved version of the classic game

🎨 Features:
• Modern and attractive interface
• Animations and visual effects
• Scoring system
• Multiple games

💻 Developed with Python and Tkinter
        """
        tk.Label(
            main_frame,
            text=info_text,
            font=self.fonts['small'],
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary'],
            justify='center'
        ).pack(pady=10)
        tk.Button(
            main_frame,
            text="❌ Close",
            font=self.fonts['score'],
            bg=self.colors['error'],
            fg='white',
            padx=20,
            pady=5,
            command=dialog.destroy,
            cursor='hand2'
        ).pack(pady=10)
