# Installation Guide for Git, Python, and VS Code

This guide will walk you through the installation of Git, Python, and Visual Studio Code (VS Code) on both Windows (using `winget`) and macOS (using `brew`). These are essential tools for running and contributing to the **Interactive Story Game** project or any coding project.

## Installation on Windows using `winget`

`winget` is a package manager for Windows that allows you to easily install software through the command line. We’ll use it to install Git, Python, and Visual Studio Code.

### 1. Install Git

1. Open the **Command Prompt** by searching for "cmd" in the Start menu.
2. Run the following command to install Git:
   ```bash
   winget install Git.Git
   ```
3. Verify the installation by running:
   ```bash
   git --version
   ```
   This should display the version of Git installed.

### 2. Install Python

1. In the **Command Prompt**, run the following command to install Python:
   ```bash
   winget install Python.Python.3
   ```
2. Verify the installation by running:
   ```bash
   python --version
   ```
   This will display the version of Python installed.

3. Optionally, to ensure you have the latest version of `pip` (Python's package installer), run:
   ```bash
   python -m pip install --upgrade pip
   ```

### 3. Install Visual Studio Code

1. In the **Command Prompt**, run the following command to install Visual Studio Code:
   ```bash
   winget install Microsoft.VisualStudioCode
   ```
2. Once installed, you can open VS Code by typing:
   ```bash
   code
   ```

Now you’re ready to run Python programs, manage Git repositories, and edit code with Visual Studio Code on Windows!

---

## Installation on macOS using `brew`

`brew` (Homebrew) is a package manager for macOS that allows you to easily install software via the terminal. We’ll use `brew` to install Git, Python, and Visual Studio Code.

### 1. Install Homebrew (if not already installed)

If you don’t have Homebrew installed, follow these steps:

1. Open **Terminal** (you can find it using Spotlight search or in Applications > Utilities).
2. Run the following command to install Homebrew:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Once the installation is complete, verify it by running:
   ```bash
   brew --version
   ```

### 2. Install Git

1. Open **Terminal** and run the following command to install Git:
   ```bash
   brew install git
   ```
2. Verify the installation by running:
   ```bash
   git --version
   ```
   This should display the version of Git installed.

### 3. Install Python

1. In **Terminal**, run the following command to install Python:
   ```bash
   brew install python
   ```
2. Verify the installation by running:
   ```bash
   python3 --version
   ```
   This will display the version of Python 3 installed.

3. Optionally, upgrade `pip`:
   ```bash
   python3 -m pip install --upgrade pip
   ```

### 4. Install Visual Studio Code

1. In **Terminal**, run the following command to install Visual Studio Code:
   ```bash
   brew install --cask visual-studio-code
   ```
2. Once installed, you can open VS Code by typing:
   ```bash
   code
   ```

Now you’re ready to run Python programs, manage Git repositories, and edit code with Visual Studio Code on macOS!

---

## Next Steps: Set Up Your Development Environment

### 1. Clone the Repository

After installing Git, Python, and Visual Studio Code, you're ready to clone the **Interactive Story Game** repository:

1. Open **Command Prompt** (Windows) or **Terminal** (macOS).
2. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/Briqo-org/interactive-story-game.git
   ```

3. Navigate into the project directory:
   ```bash
   cd interactive-story-game
   ```

### 2. Run the Python Game

1. Open the folder in VS Code by running:
   ```bash
   code .
   ```

2. Run the Python script to start the game:
   - On macOS:
     ```bash
     python3 interactive_story_game.py
     ```
   - On Windows:
     ```bash
     python interactive_story_game.py
     ```

Now you're ready to play the interactive story game and start contributing!

---

## Alternative Installation Methods

If you prefer not to use `winget` (Windows) or `brew` (macOS), here are manual installation methods:

### Manual Installation for Windows and macOS

- **Git:**
  - [Download Git for Windows and macOS](https://git-scm.com/)
- **Python:**
  - [Download Python for Windows and macOS](https://www.python.org/downloads/)
- **Visual Studio Code:**
  - [Download VS Code for Windows and macOS](https://code.visualstudio.com/Download)

---

## Additional Setup (Optional)

### Python Virtual Environment (Optional but Recommended)

For better project isolation, you can use a virtual environment. Here’s how to set it up:

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv  # macOS
   python -m venv venv   # Windows
   ```

2. **Activate the virtual environment:**
   - On macOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies (if any):**
   ```bash
   pip install -r requirements.txt
   ```

### Install Python Extensions for VS Code

To make development easier, install the Python extension in VS Code:

1. Open VS Code.
2. Go to the **Extensions** tab (or press `Ctrl+Shift+X`).
3. Search for "Python" and install the extension provided by Microsoft.

---

## Conclusion

You now have Git, Python, and Visual Studio Code installed on your Windows or macOS machine. You're all set to work on Python projects like the **Interactive Story Game**. Happy coding!
```
