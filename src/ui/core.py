import tkinter as tk
from src.ui.style import UIConfig
from src.ui.widgets import UIWidgets
from src.ui.dialogs import Dialogs
from src.game_logic.game_logic import check_winner, is_draw

class TicTacToeUI:
    def __init__(self):
        self.window = tk.Tk()
        self.config = UIConfig(self.window)
        self.colors = self.config.colors
        self.fonts = self.config.fonts
        self._setup_main_window()
        self._init_game_state()
        self.widgets = UIWidgets(self)
        self.dialogs = Dialogs(self)
        self._create_menu()
        self._create_ui()
        self.show_player_selection_window()
        self.window.mainloop()

    def _setup_main_window(self):
        # Use the theme's bg_primary color from settings for initial background
        from src.config.settings import COLOR_THEMES
        theme = 'dark'  # Default theme
        theme_colors = COLOR_THEMES[theme]
        self.colors.update(theme_colors)
        self.window.title("Tic Tac Toe")
        self.window.configure(bg=self.colors['bg_primary'])
        # Set a more square and compact window size
        self.window.geometry("100x100")
        self.window.minsize(320, 320)
        self.window.resizable(False, False)
        self._center_window(420, 420)

    def _center_window(self, width, height):
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def _init_game_state(self):
        self.score_x = 0
        self.score_o = 0
        self.games_played = 0
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = None
        self.game_over = False
        self.winning_line = []

    def _create_menu(self):
        menubar = tk.Menu(self.window)
        # Game menu
        game_menu = tk.Menu(menubar, tearoff=0)
        game_menu.add_command(label="New Game", command=self.new_game)
        game_menu.add_command(label="Reset Scores", command=self.reset_scores)
        game_menu.add_separator()
        game_menu.add_command(label="Quit", command=self.window.quit)
        menubar.add_cascade(label="Game", menu=game_menu)
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="How to Play", command=self.dialogs.show_instructions)
        help_menu.add_command(label="About", command=self.dialogs.show_about)
        # Settings menu
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Change Theme", command=self.show_theme_dialog)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.window.config(menu=menubar)

    def show_theme_dialog(self):
        import tkinter as tk
        from src.config.settings import COLOR_THEMES
        dialog = tk.Toplevel(self.window)
        dialog.title("Change Theme")
        dialog.configure(bg=self.colors['bg_primary'])
        dialog.resizable(False, False)
        dialog.grab_set()
        width, height = 320, 180
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
        main_frame = tk.Frame(dialog, bg=self.colors['bg_primary'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        tk.Label(
            main_frame,
            text="Select a theme:",
            font=self.fonts['title'],
            bg=self.colors['bg_primary'],
            fg=self.colors['text_primary']
        ).pack(pady=(0, 10))
        theme_var = tk.StringVar(value='dark' if self.colors['bg_primary'] == COLOR_THEMES['dark']['bg_primary'] else 'light')
        def apply_theme():
            theme = theme_var.get()
            theme_colors = COLOR_THEMES[theme]
            self.colors.update(theme_colors)
            self._apply_theme_to_ui()
            dialog.destroy()
        for theme in COLOR_THEMES:
            tk.Radiobutton(
                main_frame,
                text=theme.capitalize(),
                variable=theme_var,
                value=theme,
                font=self.fonts['score'],
                bg=self.colors['bg_primary'],
                fg=self.colors['text_primary'],
                selectcolor=self.colors['bg_card'],
                activebackground=self.colors['bg_card']
            ).pack(anchor='w')
        tk.Button(
            main_frame,
            text="Apply",
            font=self.fonts['score'],
            bg=self.colors['accent'],
            fg='white',
            padx=15,
            pady=5,
            command=apply_theme,
            cursor='hand2'
        ).pack(pady=10)

    def _apply_theme_to_ui(self):
        # Update main window background
        self.window.configure(bg=self.colors['bg_primary'])
        # Update all frames and labels recursively
        for widget in self.window.winfo_children():
            self._recursive_update_theme(widget)
        # Update board buttons
        for r, row in enumerate(self.buttons):
            for c, btn in enumerate(row):
                # Always use white for empty cells, x_color/o_color for played
                if self.board[r][c] == 'X':
                    btn.config(text='❌', bg=self.colors['x_color'], fg='white', relief='sunken', state='disabled')
                elif self.board[r][c] == 'O':
                    btn.config(text='⭕', bg=self.colors['o_color'], fg='white', relief='sunken', state='disabled')
                else:
                    btn.config(text='', bg='white', fg=self.colors['bg_primary'], relief='raised', state='normal')
        # Update score and turn labels
        self.score_label_x.config(fg=self.colors['x_color'], bg=self.colors['bg_primary'])
        self.score_label_o.config(fg=self.colors['o_color'], bg=self.colors['bg_primary'])
        self.turn_label.config(fg=self.colors['accent'], bg=self.colors['bg_primary'])
        self.games_label.config(fg=self.colors['text_secondary'], bg=self.colors['bg_primary'])

    def _recursive_update_theme(self, widget):
        # Update background and foreground for frames and labels
        try:
            if isinstance(widget, tk.Frame):
                widget.config(bg=self.colors['bg_primary'])
            elif isinstance(widget, tk.Label):
                widget.config(bg=self.colors['bg_primary'], fg=self.colors['text_primary'])
            elif isinstance(widget, tk.Button):
                # Buttons are handled separately
                pass
        except:
            pass
        for child in widget.winfo_children():
            self._recursive_update_theme(child)

    def _create_ui(self):
        outer = tk.Frame(self.window, bg=self.colors['bg_primary'])
        outer.pack(fill='both', expand=True)
        outer.grid_rowconfigure(0, weight=1)
        outer.grid_rowconfigure(1, weight=0)
        outer.grid_rowconfigure(2, weight=1)
        outer.grid_columnconfigure(0, weight=1)
        main_frame = tk.Frame(outer, bg=self.colors['bg_primary'])
        main_frame.grid(row=1, column=0)
        self._create_score_frame(main_frame)
        self._create_board_frame(main_frame)
        self._create_games_label(main_frame)
        self._create_controls_frame(main_frame)

    def _create_score_frame(self, parent):
        scores_frame = tk.Frame(parent, bg=self.colors['bg_primary'])
        scores_frame.pack(pady=(0, 0))
        self.score_label_x = tk.Label(
            scores_frame, text=f"X: {self.score_x}", font=self.fonts['score'],
            fg=self.colors['x_color'], bg=self.colors['bg_primary']
        )
        self.score_label_x.pack(side='left', padx=(0, 10))
        self.turn_label = tk.Label(
            scores_frame, text="", font=self.fonts['turn'],
            fg=self.colors['accent'], bg=self.colors['bg_primary']
        )
        self.turn_label.pack(side='left', padx=(0, 10))
        self.score_label_o = tk.Label(
            scores_frame, text=f"O: {self.score_o}", font=self.fonts['score'],
            fg=self.colors['o_color'], bg=self.colors['bg_primary']
        )
        self.score_label_o.pack(side='left')

    def _create_board_frame(self, parent):
        board_frame = tk.Frame(parent, bg=self.colors['bg_primary'])
        board_frame.pack(pady=(6, 0))
        self.buttons = self.widgets.create_board_buttons(board_frame, self.handle_click)

    def _create_games_label(self, parent):
        self.games_label = tk.Label(
            parent, text=f"Games: {self.games_played}", font=self.fonts['score'],
            fg=self.colors['text_secondary'], bg=self.colors['bg_primary']
        )
        self.games_label.pack(pady=(4, 0))

    def _create_controls_frame(self, parent):
        controls_frame = tk.Frame(parent, bg=self.colors['bg_primary'])
        controls_frame.pack(pady=(6, 0))
        new_game_btn = tk.Button(
            controls_frame, text="New", font=self.fonts['score'],
            bg=self.colors['accent'], fg='white', relief='flat', padx=12, pady=4,
            command=self.new_game, cursor='hand2', activebackground=self.colors['hover']
        )
        new_game_btn.pack(side='left', padx=6)
        reset_btn = tk.Button(
            controls_frame, text="Reset", font=self.fonts['score'],
            bg=self.colors['bg_card'], fg=self.colors['text_secondary'], relief='flat',
            padx=12, pady=4, command=self.reset_scores, cursor='hand2',
            activebackground=self.colors['hover']
        )
        reset_btn.pack(side='left', padx=6)

    def handle_click(self, row, col):
        if self.board[row][col] == "" and not self.game_over:
            self.board[row][col] = self.current_player
            if self.current_player == "X":
                symbol = "❌"
                color = self.colors['x_color']
            else:
                symbol = "⭕"
                color = self.colors['o_color']
            button = self.buttons[row][col]
            button.config(
                text=symbol,
                bg=color,
                fg='white',
                relief='sunken',
                state='disabled'
            )
            if check_winner(self.board, self.current_player):
                self.game_over = True
                self.games_played += 1
                if self.current_player == "X":
                    self.score_x += 1
                else:
                    self.score_o += 1
                self.update_score_display()
                self.highlight_winning_line()
                self.window.after(1500, lambda: self.dialogs.show_winner_dialog(self.current_player, self.new_game))
            elif is_draw(self.board):
                self.game_over = True
                self.games_played += 1
                self.update_score_display()
                self.window.after(1000, lambda: self.dialogs.show_draw_dialog(self.new_game))
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_turn_display()

    def highlight_winning_line(self):
        player = self.current_player
        for r in range(3):
            if all(self.board[r][c] == player for c in range(3)):
                for c in range(3):
                    self.buttons[r][c].config(bg=self.colors['success'])
                return
        for c in range(3):
            if all(self.board[r][c] == player for r in range(3)):
                for r in range(3):
                    self.buttons[r][c].config(bg=self.colors['success'])
                return
        if all(self.board[i][i] == player for i in range(3)):
            for i in range(3):
                self.buttons[i][i].config(bg=self.colors['success'])
            return
        if all(self.board[i][2-i] == player for i in range(3)):
            for i in range(3):
                self.buttons[i][2-i].config(bg=self.colors['success'])

    def new_game(self):
        self.reset_board()
        self.show_player_selection_window()

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.winning_line = []
        for row in self.buttons:
            for btn in row:
                btn.config(
                    text="",
                    bg='white',
                    fg=self.colors['bg_primary'],
                    relief='raised',
                    state='normal'
                )
                self.widgets.add_hover_effects(btn)

    def reset_scores(self):
        self.score_x = 0
        self.score_o = 0
        self.games_played = 0
        self.update_score_display()
        from tkinter import messagebox
        messagebox.showinfo("Scores", "✨ Scores have been reset")

    def update_score_display(self):
        self.score_label_x.config(text=f"X: {self.score_x}")
        self.score_label_o.config(text=f"O: {self.score_o}")
        self.games_label.config(text=f"Games: {self.games_played}")

    def update_turn_display(self):
        if self.current_player:
            color = self.colors['x_color'] if self.current_player == "X" else self.colors['o_color']
            self.turn_label.config(text=f"Turn: {self.current_player}", fg=color)

    def animate_start(self):
        for i, row in enumerate(self.buttons):
            for j, btn in enumerate(row):
                self.window.after(i * 100 + j * 50, lambda b=btn: self.flash_button(b))

    def flash_button(self, button):
        original_bg = button['bg']
        button.config(bg=self.colors['accent'])
        self.window.after(200, lambda: button.config(bg=original_bg))

    def show_player_selection_window(self):
        import tkinter as tk
        import tkinter.font as tkfont
        selection_window = tk.Toplevel(self.window)
        selection_window.title("Select Player")
        try:
            selection_window.iconbitmap('')
        except:
            pass
        selection_window.configure(bg=self.colors['bg_primary'])
        selection_window.resizable(False, False)
        selection_window.grab_set()
        width, height = 260, 220  # More compact and square
        x = (selection_window.winfo_screenwidth() // 2) - (width // 2)
        y = (selection_window.winfo_screenheight() // 2) - (height // 2)
        selection_window.geometry(f'{width}x{height}+{x}+{y}')
        main_frame = tk.Frame(selection_window, bg=self.colors['bg_primary'])
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        title_label = tk.Label(
            main_frame,
            text="Who starts?",
            font=self.fonts['title'],
            bg=self.colors['bg_primary'],
            fg=self.colors['text_primary']
        )
        title_label.pack(pady=(0, 12))
        desc_label = tk.Label(
            main_frame,
            text="Select the player who will start the game",
            font=self.fonts['small'],
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary']
        )
        desc_label.pack(pady=(0, 10))
        def set_player(player):
            self.current_player = player
            self.update_turn_display()
            self.window.deiconify()
            selection_window.destroy()
            self.animate_start()
        button_frame = tk.Frame(main_frame, bg=self.colors['bg_primary'])
        button_frame.pack(pady=8)
        btn_width = 2
        btn_height = 1
        btn_padx = 10
        # Use a smaller, matching font for both symbols
        base_font = self.fonts['symbol']
        symbol_font = tkfont.Font(family=base_font.actual('family'), size=36, weight=base_font.actual('weight'))
        x_button = tk.Button(
            button_frame,
            text="❌",
            font=symbol_font,
            width=btn_width,
            height=btn_height,
            bg=self.colors['x_color'],
            fg='white',
            relief='raised',
            bd=4,
            command=lambda: set_player("X"),
            cursor='hand2',
            activebackground=self.colors['hover']
        )
        x_button.pack(side='left', padx=btn_padx)
        o_button = tk.Button(
            button_frame,
            text="⭕",
            font=symbol_font,
            width=btn_width,
            height=btn_height,
            bg=self.colors['o_color'],
            fg='white',
            relief='raised',
            bd=4,
            command=lambda: set_player("O"),
            cursor='hand2',
            activebackground=self.colors['hover']
        )
        o_button.pack(side='right', padx=btn_padx)
        def hover_x_enter(e):
            x_button.config(bg='#c0392b')
        def hover_x_leave(e):
            x_button.config(bg=self.colors['x_color'])
        def hover_o_enter(e):
            o_button.config(bg='#2980b9')
        def hover_o_leave(e):
            o_button.config(bg=self.colors['o_color'])
        x_button.bind("<Enter>", hover_x_enter)
        x_button.bind("<Leave>", hover_x_leave)
        o_button.bind("<Enter>", hover_o_enter)
        o_button.bind("<Leave>", hover_o_leave)
        selection_window.protocol("WM_DELETE_WINDOW", lambda: None)
        self.window.wait_window(selection_window)
