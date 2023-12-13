
// Get the modal
const modal = document.getElementById('myModal');

// Get the button that opens the modal
const btn = document.getElementById('showModalBtn');

// Get the <span> element that closes the modal
const span = document.getElementsByClassName('close')[0];

// When the user clicks the button, open the modal
btn.onclick = function () {
    modal.style.display = 'block';
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = 'none';
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};

document.getElementById('addRecipeForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const newRecipe = {
        title: formData.get('title'),
        ingredients: formData.get('ingredients'),
        instructions: formData.get('instructions')
    };

    fetch('http://127.0.0.1:5000/recipes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newRecipe)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Recipe added:', data);
            modal.style.display = 'none'; // Close the modal
            displaySuccessMessage(); // Display success message
            fetchAndDisplayRecipes();
            // Call the function to fetch and display recipes again here if needed
        })
        .catch(error => console.error('Error adding recipe:', error));
});

function displaySuccessMessage() {
    const successModal = document.getElementById('successModal');
    const closeBtn = successModal.querySelector('.close');

    successModal.style.display = 'block';

    closeBtn.onclick = function () {
        successModal.style.display = 'none';
    };

    window.onclick = function (event) {
        if (event.target === successModal) {
            successModal.style.display = 'none';
        }
    };

    setTimeout(() => {
        successModal.style.display = 'none';
    }, 4000);
}

function fetchAndDisplayRecipes() {
    fetch('http://127.0.0.1:5000/recipes')
        .then(response => response.json())
        .then(data => createRecipes(data))
        .catch(error => console.error('Error fetching recipes:', error));
}

function createRecipes(data) {
    {
        const recipesDiv = document.getElementById('recipes');
        recipesDiv.innerHTML = ""
        const recipes = data.recipes;
        console.log(recipes);
        recipes.forEach(recipe => {
            const recipeElement = document.createElement('div');
            recipeElement.innerHTML = `
                <h2>${recipe.title}</h2>
                <p><strong>Ingredients:</strong> ${recipe.ingredients.replace(/[\[\]]/g, "").split(",")}</p>
                <p><strong>Rating:</strong> ${recipe.rating ? recipe.rating : ""}</p>
                <button class="open-modal-btn" data-id="${recipe.id}">Edit Recipe</button>
                <div id="myModal-${recipe.id}" class="modal">
                    <div class="modal-content">
                    <span id="updateClose" class="close">&times;</span>
                    <h2>Update Recipe</h2>
                    <form id="updateRecipeForm">
                        <label for="title">Title:</label>
                        <input type="text" id="title" name="title" placeholder="Enter title" class="modal-input" required>
            
                        <label for="ingredients">Ingredients:</label>
                        <textarea id="ingredients" name="ingredients" placeholder="Enter ingredients" class="modal-input" required></textarea>
            
                        <label for="rating">Rating:</label>
                        <textarea id="rating" name="rating" placeholder="Enter Rating" class="modal-input"></textarea>

                        <label for="notes">Notes:</label>
                        <textarea id="notes" name="notes" placeholder="Notes" class="modal-input"></textarea>

                        <label for="region">Region:</label>
                        <textarea id="region" name="region" placeholder="Region/Country of Origin" class="modal-input"></textarea>
                        
                        <label for="link">Link:</label>
                        <textarea id="link" name="link" placeholder="Link to Recipe" class="modal-input"></textarea>

                        <label for="instructions">Instructions:</label>
                        <textarea id="instructions" name="instructions" placeholder="Instructions" class="modal-input"></textarea>
            
                        
                        <button type="submit">Update Recipe</button>
                    </form>
                </div>
                </div>
                <hr>
            `;
            recipeElement.classList.add('recipe');
            const deleteButton = document.createElement('i');
            deleteButton.classList.add('fas', 'fa-times', 'delete-icon');
            deleteButton.addEventListener('click', () => deleteRecipe(recipe.id));
            recipeElement.appendChild(deleteButton);
            recipesDiv.appendChild(recipeElement);
        });
        const openModalButtons = document.querySelectorAll('.open-modal-btn');

        openModalButtons.forEach(openBtn => {
            openBtn.addEventListener('click', async () => {

                const recipeId = openBtn.getAttribute('data-id');
                const updateModal = document.getElementById(`myModal-${recipeId}`);

                // Fetch recipe details based on the recipeId
                const response = await fetch(`http://127.0.0.1:5000/recipes/${recipeId}`);
                const recipeData = await response.json();

                if (response.ok) {
                    const recipe = recipeData.recipes[0];
                    // Populate the modal content with recipe details
                    // Set values for modal inputs, textareas, etc.
                    // Example:
                    updateModal.querySelector('#title').value = recipe.title;
                    updateModal.querySelector('#ingredients').value = recipe.ingredients;
                    updateModal.querySelector('#rating').value = recipe.rating;
                    updateModal.querySelector('#instructions').value = recipe.instructions;
                    updateModal.querySelector('#region').value = recipe.region;
                    updateModal.querySelector('#link').value = recipe.link;
                    updateModal.querySelector('#notes').value = recipe.notes;



                    updateModal.style.display = 'block'; // Open the modal


                    handleUpdateModalDisplay(updateModal, recipeId)
                } else {
                    console.error('Error fetching recipe details');
                }
            });
        });
    }
}

function handleUpdateModalDisplay(updateModal, recipeId) {
    const closeSpan = updateModal.querySelector('.close');

    closeSpan.onclick = function () {
        updateModal.style.display = 'none';
    };

    window.onclick = function (event) {
        if (event.target === updateModal) {
            updateModal.style.display = 'none';
        }
    };

    const updateRecipeForm = updateModal.querySelector('#updateRecipeForm');

    updateRecipeForm.addEventListener('submit', async function (event) {
        event.preventDefault();

        const formData = new FormData(this);
        const updatedRecipe = {
            title: formData.get('title'),
            ingredients: formData.get('ingredients'),
            rating: formData.get('rating'),
            instructions: formData.get('instructions'),
            region: formData.get('region'),
            link: formData.get('link'),
            notes: formData.get('notes')
        };

        try {
            const response = await fetch(`http://127.0.0.1:5000/recipes/${recipeId}/update`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(updatedRecipe)
            });

            if (response.ok) {
                console.log('Recipe updated successfully');
                updateModal.style.display = 'none'; // Close the modal
                fetchAndDisplayRecipes(); // Refresh recipe list after update
            } else {
                console.error('Error updating recipe');
            }
        } catch (error) {
            console.error('Error updating recipe:', error);
        }
    });
}

function deleteRecipe(recipeId) {
    fetch(`http://127.0.0.1:5000/recipes/${recipeId}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                console.log('Recipe deleted successfully');
                fetchAndDisplayRecipes(); // Refresh recipe list after deletion
            } else {
                console.error('Error deleting recipe');
            }
        })
        .catch(error => console.error('Error deleting recipe:', error));
}



// Call the fetchRecipes function when the page loads
window.onload = fetchAndDisplayRecipes;
