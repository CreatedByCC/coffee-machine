![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![MIT License](https://img.shields.io/badge/License-MIT-green)
![100 Days of Code](https://img.shields.io/badge/100DaysOfCode-Day%2015-orange)

# ☕ Coffee Machine
A simple console‑based coffee machine simulation built in Python.
The program allows users to order drinks, insert coins, check machine resources, and track profit — all while managing ingredient usage automatically.

## 💡 What I Learned
- How to structure a program using functions
- How to manage state using dictionaries
- How to validate resources before performing an action
- How to simulate real‑world processes (payments, change, inventory)
- How to write clean, readable, modular Python code

## 🧩 How It Works
1. The user selects a drink from the menu.  
2. The program looks up the drink and retrieves its ingredient requirements.  
3. The machine checks whether enough water, milk, and coffee are available.  
4. If resources are sufficient, the user is prompted to insert coins.  
5. The MoneyMachine calculates the total amount and checks if it covers the drink cost.  
6. If payment is successful, the machine deducts ingredients and “makes” the drink.  
7. The user can type `report` to view current resources or `off` to shut down the machine. 

## 📸 Example Output
```
What would you like? latte
how many quarters?: 10
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0
Here is $0.0 dollars in change.
Here is your latte ☕️. Enjoy!
```

## 🚀 How to Play
Run `main.py` in a Python environment and follow the prompts:

## 📁 Files
- `main.py`: Main game logic

## 🙏 Acknowledgements
- Thanks to Dr. Angela Yu and the team behind the 100 Days of Code: Python Bootcamp for the original project structure and assets.
- This version was adapted and expanded by me as part of my creative developer-educator journey.
- Built with care to reinforce beginner-friendly logic and clean game design.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
