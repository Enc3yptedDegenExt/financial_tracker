## Step 1: Clone the Repository from GitHub
1. Open your terminal or command prompt (on Windows, use Command Prompt, PowerShell, or WSL if enabled).
2. Navigate to a directory where you want to store the project (e.g., `cd ~/projects`).
3. Clone the repository: 
 git clone https://github.com/Enc3yptedDegenExt/financial_tracker.git

 4. Change into the project directory: cd financial_tracker

### Step 2: Set Up a Virtual Environment
Virtual environments isolate dependencies, which is best practice for Python projects.

1. In the terminal (from the project root): python -m venv .venv
- This creates a virtual environment named `.venv` in the project folder.

2. Activate the virtual environment:
- **Windows (Command Prompt)**: `.venv\Scripts\activate`
- **Windows (WSL or Linux)**: `source .venv/bin/activate`
- **macOS**: `source .venv/bin/activate`
- Your terminal prompt should change to indicate the virtual environment is active (e.g., `(.venv)`).
3. Install dependencies:
pip install flask
- If there's a `requirements.txt` file (e.g., containing `flask`), run `pip install -r requirements.txt` instead.

### Step 3: Install and Set Up VS Code
1. Download and install VS Code from the official website: [code.visualstudio.com](https://code.visualstudio.com/).
- Install the Python extension by Microsoft (search for "Python" in VS Code's Extensions view, or install via Ctrl+Shift+X).
- Optional: Install extensions like "Flask" or "GitLens" for better Flask and Git support.

2. Open the project in VS Code:
- Launch VS Code.
- Go to **File > Open Folder** and select the `financial_tracker` folder you cloned.
- VS Code will load the project, detecting Python files and suggesting configurations.

3. Configure VS Code for Python:
- Press Ctrl+Shift+P (or Cmd+Shift+P on macOS) to open the Command Palette.
- Type and select **Python: Select Interpreter**.
- Choose the interpreter from your virtual environment (e.g., `./.venv/bin/python` or similar).
- This ensures VS Code uses the isolated environment with Flask installed.

### Step 4: Run the App in VS Code
1. Open the integrated terminal in VS Code: Press Ctrl+` (backtick) or go to **Terminal > New Terminal**.
- Ensure the virtual environment is activated (run the activation command if needed).

2. Run the application:
python app.py

3. Access the App:
- Open a web browser and go to `http://localhost:5000`
