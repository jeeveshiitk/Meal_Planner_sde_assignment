# AI Agent Prototype: The Auto-Planner v2

* **Name:** Jeevesh Narayan
* **University:** IIT Kanpur
* **Department:** Civil Engineering

## 1. Project Overview

This is an AI agent prototype that automates the manual task of weekly meal planning. The user provides a list of available ingredients through a simple web interface, and the agent **reasons**, **plans**, and **executes** to generate a 7-day meal plan.

This project fulfills all mandatory requirements by implementing a functional UI and a backend agent. It also targets **bonus points** by using a "Planner + Tool" architecture, where the "Planner" agent calls a custom "Recipe Tool" to generate meals.

## 2. Architecture & Tech Stack

* **Frontend (UI):** HTML, CSS, and vanilla JavaScript.
* **Backend:** Python (Flask)
* **Agent Logic:** A "Planner" agent that calls a "Recipe Tool" (simulated function), demonstrating a multi-component agent system.

For a complete breakdown, please see the `System_Design_Document.md`.

## 3. Originality & Social Impact
(As required by the evaluation criteria)

* **Originality:** While meal planners exist, this project's originality lies in its agent-based approach, planning *from* available ingredients rather than *for* ideal recipes.
* **Social Impact:** This system is designed to reduce the daily cognitive load of "what to cook" and, more importantly, to help **reduce food waste** by encouraging users to build a plan around the food they already have.

## 4. How to Run

1.  **Clone the repository:**
    ```bash
    git clone [Your_Repo_URL]
    cd [Your_Repo_Name]
    ```
2.  **Install dependencies (for the backend):**
    ```bash
    pip install -r src/requirements.txt
    ```
3.  **Run the backend agent server:**
    ```bash
    python src/app.py
    ```
    * The server will be running at `http://127.0.0.1:5000`

4.  **Access the User Interface:**
    * Open your web browser and navigate to `http://127.0.0.1:5000`
    * You will see the web UI. Enter your ingredients and click "Generate Plan."
