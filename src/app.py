import time
import json
import random
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__, static_folder='../static', template_folder='../static')

# --- Agent Components ---

def mock_recipe_tool(ingredients):
    """
    This is the "Custom Tool" (simulated).
    In a real system, this might call a RAG pipeline or a fine-tuned model.
    It takes a few ingredients and returns a single meal idea.
    """
    time.sleep(0.1) # Simulate a short API call
    
    # Simple mock logic
    if "eggs" in ingredients:
        return {"meal_name": "Scrambled Eggs", "ingredients_used": ["eggs"]}
    if "chicken" in ingredients and "rice" in ingredients:
        return {"meal_name": "Chicken & Rice", "ingredients_used": ["chicken", "rice"]}
    if "chicken" in ingredients:
        return {"meal_name": "Grilled Chicken", "ingredients_used": ["chicken"]}
    if "spinach" in ingredients:
        return {"meal_name": "Spinach Salad", "ingredients_used": ["spinach"]}
    if "bread" in ingredients:
        return {"meal_name": "Toast", "ingredients_used": ["bread"]}
    
    # Default fallback
    return {"meal_name": f"Mixed {ingredients[0]} Bowl", "ingredients_used": [ingredients[0]]}

def run_planner_agent(ingredients_list):
    """
    This is the "Planner" agent logic.
    It reasons, plans, and executes by calling the tool.
    """
    full_plan = {}
    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    meals_types = ["Breakfast", "Lunch", "Dinner"]
    
    if not ingredients_list:
        return {"Error": "No ingredients provided."}

    # The "Planner" reasons and breaks down the task
    for day in days:
        full_plan[day] = {}
        for meal in meals_types:
            # Plan: Select ingredients for this meal
            # Simple logic: just pick one or two random ones.
            # A real agent would track remaining ingredient state.
            selected_ingredients = random.sample(ingredients_list, k=min(2, len(ingredients_list)))
            
            # Execute: Call the "Recipe Tool"
            meal_idea = mock_recipe_tool(selected_ingredients)
            full_plan[day][meal] = meal_idea
            
    return full_plan

# --- API Endpoints ---

@app.route('/')
def index():
    """Serves the main HTML UI."""
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    """Serves the static CSS/JS files."""
    return send_from_directory('../static', path)

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    """
    This is the main API endpoint for the agent.
    The UI calls this.
    """
    try:
        data = request.get_json()
        ingredients_str = data.get('ingredients', '')
        ingredients_list = [ing.strip().lower() for ing in ingredients_str.split(',') if ing.strip()]
        
        # Call the "Planner" agent
        final_plan = run_planner_agent(ingredients_list)
        
        return jsonify(final_plan)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    print("AI Agent Server running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
