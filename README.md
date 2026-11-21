# standard-calculator.py
Command-line calculator supporting add, subtract, multiply, divide, percentage, modulus, square root with error handling for division by zero easily.
# 🧮 MILI'S_CALCULATOR :
A standard Python desktop calculator designed to perform basic arithmetic operations with built-in error handling.
# preview: 
MIli's calculator.png
# ✨ Features
- Modern, custom-styled graphical user interface (GUI).
- Supports standard and advanced arithmetic operations: Addition(+), Subtraction(-), Multiplication(*), Division(/),modulus(mod),square root,percentage(%)
- Clean grid layout for effortless calculation flow.
- Custom Dark & Orange Theme: Designed with a dark mode background, high-contrast orange operator buttons(+,-,*,/), light gray utility keys(C,mod,root), and dark gray number keys(0-9)
- It can also store your history in a table format where the id is a primary key and 1st column of integer type, expression defines your calculation that you want to do perform which text type and result which stores your result as a text type in the databases. i use sqlite3 databases.

# why sqlite3?
- It's built into Python. The sqlite3 module ships with Python, so there's nothing to install. Anyone who clones your repo can run it right away.
- No server needed. Databases like MySQL or PostgreSQL run as a separate service you have to set up. SQLite is just a single file (history.db) that your program reads and writes directly.
- It's reliable. Writes are transactional, so if the program crashes mid-save, you won't end up with a half-written, corrupted history.
- You can query it. With SQL you can later do things like SELECT * FROM calc_history ORDER BY id DESC LIMIT 10 to show the last 10 calculations, or delete old entries. That's much harder with a plain text file.
- It's a useful skill. SQL basics carry over to almost every other database you'll use later, and SQLite itself is used in phones, browsers, and many apps.
  
# 🛠️ How It Works:

This application is powered by Python’s built-in "Tkinter" library. Here is a breakdown of how the core components operate:

1. Window Setup & Styling ('Tk' & Widgets):
   - The main application window is instantiated using 'tk.Tk()', with customized dimensions and a tailored color theme (such as a striking dark mode or custom accent colors).
   - An entry/label widget acts as the "display screen", updating dynamically as buttons are clicked.

2. Grid Layout Manager ('grid()'):
   - The calculator buttons ('0-9', '+', '-', '*', '/', '=', 'C') are dynamically generated or placed using Tkinter's '.grid()' geometry manager, ensuring they align neatly into rows and columns.

3. Event Handling & Logic:
   - Each button is linked ('command=...') to specific Python functions. 
   - When a number or operator is pressed, it appends to a running string expression.
   - When the equals ('=') button is triggered, Python safely evaluates the expression (using built-in logic) and renders the computed result onto the screen.

4. Expression Evaluation & Safety: Listens for button clicks, appends inputs to construct expressions, dynamically updates the display screen, and safely handles math errors like division by zero.

   ## 🚀 How to Run

Clone the repository:
   ```bash
   git clone [https://github.com/MILIHAZRA/standard-calculator.py.git]
