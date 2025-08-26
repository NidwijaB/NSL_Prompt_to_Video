# NSL_Prompt_to_Video
Nepal Sign Language — Prompt to Video Project

---

##  Description

**NSL_Prompt_to_Video** is an accessibility‑focused application that takes user‑provided prompts or text, searches a **Nepal Sign Language (NSL)** knowledge base, and returns the matching sign language videos, all within an easy‑to‑use graphical interface.  

Its goal is to make sign language resources more approachable and interactive, helping bridge communication gaps through a simple, intuitive workflow.

---

## Setup Guide

### 1️⃣ Open the Project Folder
1. Locate where you cloned the repository.  
   Example:
   ```bash
   C:\Users\user\Documents\PYTHONPROJECTS\NSL_Prompt_to_Video
   ```
2. Open **Command Prompt (CMD)**.
3. Navigate to the project folder:
   ```bash
   cd C:\Users\user\Documents\PYTHONPROJECTS\NSL_Prompt_to_Video
   ```

---

### 2️⃣ Create a Virtual Environment
Run:
```bash
python -m virtualenv venvnsl
```
> 💡 If you get an error saying `'virtualenv' is not found`, see [Section 4](#4️⃣-if-virtualenv-is-missing) below.

---

### 3️⃣ Activate the Virtual Environment & Install Requirements
Activate (Windows):
```bash
venvnsl\Scripts\activate
```
Install dependencies:
```bash
pip install -r install/requirements.txt
```

---

### 4️⃣ If `virtualenv` is Missing
1. Find where Python is installed (example path):
   ```bash
   C:\Users\user\AppData\Local\Programs\Python\Python312\Scripts
   ```
2. In CMD, navigate there:
   ```bash
   cd C:\Users\user\AppData\Local\Programs\Python\Python312\Scripts
   pip install virtualenv
   ```
3. Return to [Step 2](#2️⃣-create-a-virtual-environment).

---

### 5️⃣ Using PyCharm (Optional)
1. Install **PyCharm Community Edition**.
2. Open the project folder.
3. Go to:
   ```
   File → Settings → Project → Python Interpreter
   ```
4. Select the interpreter from:
   ```
   <project_folder>\venvnsl\Scripts\python.exe
   ```

---

### 6️⃣ Running from the Command Line
1. Navigate to the repo:
   ```bash
   cd C:\Users\user\Documents\PYTHONPROJECTS\NSL_Prompt_to_Video
   ```
2. Activate the virtual environment:
   ```bash
   venvnsl\Scripts\activate
   ```
3. Run the main script:
   ```bash
   Script\main.py
   ```

---

## 💡 Tips
- Each time you open a new CMD session, activate the virtual environment before running the script.
- Use a Python version compatible with the project’s requirements.
