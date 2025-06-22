# This file contains configurations and constants for the project.
# You can import and use these values in your main modules to make the UI, colors, texts, or animations configurable.
# Currently, it's not used directly by the UI, but it's useful for future improvements or to centralize global settings.

# Tic Tac Toe Game Configuration

# Window configuration
WINDOW_CONFIG = {
    'width': 500,
    'height': 600,
    'title': '🎮 Tic Tac Toe - Modern Edition',
    'resizable': False
}

# Color themes (modern dark and light)
COLOR_THEMES = {
    'dark': {
        'bg_primary': '#1a1a2e',
        'bg_secondary': '#16213e',
        'bg_card': '#0f4c75',
        'accent': '#3282b8',
        'success': '#4CAF50',
        'warning': '#FF9800',
        'error': '#f44336',
        'text_primary': '#ffffff',
        'text_secondary': '#bbbbbb',
        'x_color': '#e74c3c',
        'o_color': '#3498db',
        'hover': '#2196F3'
    },
    'light': {
        'bg_primary': '#f5f5f5',
        'bg_secondary': '#e0e0e0',
        'bg_card': '#ffffff',
        'accent': '#2196F3',
        'success': '#4CAF50',
        'warning': '#FF9800',
        'error': '#f44336',
        'text_primary': '#212121',
        'text_secondary': '#757575',
        'x_color': '#e74c3c',
        'o_color': '#3498db',
        'hover': '#1976D2'
    }
}

# Fonts configuration
FONTS = {
    'family': 'Segoe UI',
    'title_size': 24,
    'score_size': 14,
    'button_size': 28,
    'small_size': 10
}

# Animation settings
ANIMATIONS = {
    'button_flash_duration': 200,  # ms
    'winner_highlight_delay': 1500,  # ms
    'draw_dialog_delay': 1000,  # ms
    'start_animation_delay': 50  # ms between buttons
}

# Game symbols
GAME_SYMBOLS = {
    'X': '❌',
    'O': '⭕',
    'empty': ''
}

# Board configuration
BOARD_CONFIG = {
    'size': 3,
    'button_width': 4,
    'button_height': 2,
    'padding': 2
}

# Game messages
MESSAGES = {
    'winner': "🎉 We have a winner!",
    'draw': "🤝 Draw!",
    'player_x_wins': "Player ❌ X wins!",
    'player_o_wins': "Player ⭕ O wins!",
    'draw_message': "Nobody won this time",
    'turn_message': "Player {symbol} {player}'s turn",
    'scores_reset': "✨ Scores have been reset",
    'games_played': "Games played: {count}"
}

# Menu configuration
MENU_ITEMS = {
    'game': {
        'label': 'Game',
        'items': [
            ('New Game', 'new_game'),
            ('Reset Scores', 'reset_scores'),
            ('separator', None),
            ('Quit', 'quit')
        ]
    },
    'help': {
        'label': 'Help',
        'items': [
            ('How to Play', 'show_instructions'),
            ('About', 'show_about')
        ]
    }
}

# Instructions text
INSTRUCTIONS_TEXT = """
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

# About text
ABOUT_TEXT = """
✨ Improved version of the classic game

🎨 Features:
• Modern and attractive interface
• Animations and visual effects
• Scoring system
• Multiple games

💻 Developed with Python and Tkinter
"""

# Default settings
DEFAULT_THEME = 'dark'
DEFAULT_PLAYER = 'X'
