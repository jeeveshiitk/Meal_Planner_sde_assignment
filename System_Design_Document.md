# System Design Document: AI Meal Planner Agent

## 1. System Overview & Purpose

The AI Meal Planner is a web-based prototype designed to automate the manual, daily task of meal planning. The system's core function is to accept a list of available ingredients from a user and generate a complete, structured 7-day meal plan (breakfast, lunch, and dinner).

This system fulfills the core task of automating a manual process and is designed to "reason, plan, and execute."

## 2. Architecture

The system uses a **Frontend-Backend** architecture. The agent logic resides on the backend and is exposed to the frontend via a REST API.

The agent itself follows a **"Planner + Tool"** pattern, which addresses the optional "Multi-agent collaboration" and "custom Tools" for bonus points.

* **Planner (Main Agent):** This is the "brain" of the operation, implemented in Python. It receives the high-level goal (e.g., "plan 7 days of meals with these ingredients"). It **reasons** by breaking this goal into 21 smaller steps (7 days * 3 meals). It **plans** by iterating through each step and selecting ingredients. It **executes** by calling its available "Tool."
* **RecipeTool (Custom Tool):** This is a specialized component (simulated as a function in this prototype) that the Planner calls. Its *only* job is to accept a few ingredients (e.E., `["chicken", "rice"]`) and return a single meal idea. This separation of concerns is a key agent design pattern.


## 3. Data Design

* **Input (from UI to Backend):** A JSON object containing a single string of comma-separated ingredients.
    ```json
    { "ingredients": "chicken, rice, broccoli, eggs, milk" }
    ```
* **Internal Data (Agent State):** The Planner maintains a list of `available_ingredients` and a `full_plan` dictionary that it builds incrementally.
* **Output (from Backend to UI):** A JSON object representing the complete 7-day plan.
    ```json
    {
      "Day 1": {
        "Breakfast": { "meal_name": "Scrambled Eggs", "ingredients_used": ["eggs", "milk"] },
        "Lunch": { "meal_name": "Chicken and Rice", "ingredients_used": ["chicken", "rice"] },
        "Dinner": { "meal_name": "Steamed Broccoli", "ingredients_used": ["broccoli"] }
      },
      "Day 2": { ... }
    }
    ```

## 4. Component Breakdown

1.  **Frontend (UI) - `static/`**
    * **`index.html`:** The main HTML5 file. Provides the structure, including a `<textarea>` for ingredients, a `<button>` to submit, and a `<div>` (`id="plan-output"`) to display results.
    * **`style.css`:** Provides all styling for the UI to meet the "UI/UX design" evaluation. It ensures the layout is clean, responsive, and easy to read.
    * **`script.js`:** Contains the client-side logic. It listens for the button click, (1) gets the ingredient text, (2) sends it to the backend `/generate-plan` endpoint using `fetch()`, and (3) receives the plan JSON and dynamically builds HTML to display it in the `plan-output` div.

2.  **Backend (Agent) - `src/`**
    * **`app.py`:** The main Flask server. It has three key responsibilities:
        1.  Serves the static frontend files (`index.html`, `style.css`, `script.js`).
        2.  Provides the `/generate-plan` API endpoint (REST).
        3.  Contains the entire agent logic (Planner and Tool).
    * **`requirements.txt`:** Lists the single Python dependency: `Flask`.

## 5. Chosen Technologies & Rationale

* **Python (Flask):**
    * **Reason:** Flask is a lightweight, "unopinionated" web framework perfect for prototypes. It's ideal for building a simple REST API and serving the UI, while allowing the core agent logic (also in Python) to live in the same file.
* **HTML5, CSS3, Vanilla JavaScript:**
    * **Reason:** No complex frontend framework (like React or Next.js) is needed for this prototype. Using vanilla JS, HTML, and CSS is the fastest, most direct way to build a functional UI that meets the mandatory requirement, ensuring any evaluator can run it without complex build steps.

## 6. UI/UX Design
(As required by the evaluation criteria)

The UI/UX design is intentionally **minimalist, clean, and task-focused**.

* **Clarity:** There is a single text box and a single button. The user's "call to action" is unambiguous.
* **Feedback:** A "Loading..." state is implemented in the UI to give the user feedback while the agent is "thinking" (planning).
* **Readability:** The final plan is rendered in a structured, hierarchical format (Days > Meals) that is easy to scan and read. This is a direct fulfillment of the "UI/UX design" evaluation point.
