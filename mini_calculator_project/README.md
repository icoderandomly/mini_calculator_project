# Mini Project — Simple Calculator (Python)

**Course:** Computer Science Fundamentals & Career Pathways (ETCCCP105)  
**Author:** Harsh Singh
**Tools:** Visual Studio Code, Git, GitHub  
**Language:** Python  
**Length:** Mini project

---

## Project Description
A console-based calculator that supports addition, subtraction, multiplication and division with basic input validation and error handling. Intended as a beginner-friendly project to demonstrate use of VS Code, Git, and GitHub for development and collaboration.

---

## Features
- Addition, subtraction, multiplication, division
- Input validation and division-by-zero handling
- Simple, well-documented code
- Easy to extend (GUI, tests, more functions)

---

## Files in this repository
```
calculator.py
README.md
.gitignore
docs/
assets/
```

---

## Installation & Usage

1. Clone the repository:
```bash
git clone <https://github.com/icoderandomly/mini_calculator_project/tree/63e3641c8eddedeab46fe4a8a2eff2f590b383cc/mini_calculator_project>
cd mini_calculator_project
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Run the calculator:
```bash
python calculator.py
```

Follow the on-screen prompts. Enter `q` for the first number to exit.

---

## Screenshots

Calculator running:  
![calculator run](assets/calculator_run.png)

Repository view on GitHub :  
![github view](assets/github_repo_view.png)

---

## Development / Git Workflow 

```bash
# create repo locally
git init
git add .
git commit -m "Initial commit: add calculator.py, README, .gitignore"

# Make changes iteratively with meaningful messages
git add calculator.py
git commit -m "Add input validation and loop to allow repeated calculations"

git add README.md
git commit -m "Add README and usage instructions"

git add assets
git commit -m "Add screenshots to assets folder"

git add docs/documentation.md
git commit -m "Add docs: development process and future improvements"

# When ready, push to GitHub (create remote first)
git remote add origin <your-github-repo-url>
git branch -M main
git push -u origin main
```



---

## Documentation
See `docs/documentation.md` for project overview, development process, and future improvements.

---


