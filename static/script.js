document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const ingredientsInput = document.getElementById('ingredients-input');
    const planOutput = document.getElementById('plan-output');

    generateBtn.addEventListener('click', async () => {
        const ingredients = ingredientsInput.value;
        if (!ingredients.trim()) {
            alert('Please enter at least one ingredient.');
            return;
        }

        // 1. Set UI to loading state
        planOutput.innerHTML = '<p class="placeholder">🤖 Agent is thinking... planning your week...</p>';
        generateBtn.disabled = true;
        generateBtn.textContent = 'Generating...';

        try {
            // 2. Call the backend agent
            const response = await fetch('/generate-plan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ingredients: ingredients }),
            });

            if (!response.ok) {
                throw new Error(`Agent error: ${response.statusText}`);
            }

            const plan = await response.json();

            // 3. Render the plan in the UI
            renderPlan(plan);

        } catch (error) {
            console.error('Error:', error);
            planOutput.innerHTML = `<p class="placeholder" style="color: red;">Error: ${error.message}</p>`;
        } finally {
            // 4. Restore UI
            generateBtn.disabled = false;
            generateBtn.textContent = 'Generate Plan';
        }
    });

    function renderPlan(plan) {
        if (!plan || Object.keys(plan).length === 0) {
            planOutput.innerHTML = '<p class="placeholder">Could not generate a plan.</p>';
            return;
        }
        
        // Clear placeholder
        planOutput.innerHTML = ''; 

        // Iterate through the plan object (e.g., "Day 1", "Day 2")
        for (const day in plan) {
            const dayDiv = document.createElement('div');
            dayDiv.className = 'plan-day';
            
            const dayTitle = document.createElement('h3');
            dayTitle.textContent = day;
            dayDiv.appendChild(dayTitle);

            const meals = plan[day];
            
            // Iterate through meals (e.g., "Breakfast", "Lunch")
            for (const mealType in meals) {
                const meal = meals[mealType];
                const mealDiv = document.createElement('div');
                mealDiv.className = 'plan-meal';
                
                const mealName = meal.meal_name || 'N/A';
                const ingredientsUsed = meal.ingredients_used ? meal.ingredients_used.join(', ') : '...';
                
                mealDiv.innerHTML = `
                    <strong>${mealType}:</strong> ${mealName}
                    <br>
                    <span class="ingredients">(Uses: ${ingredientsUsed})</span>
                `;
                dayDiv.appendChild(mealDiv);
            }
            
            planOutput.appendChild(dayDiv);
        }
    }
});