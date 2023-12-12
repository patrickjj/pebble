
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
        title: formData.get('titleInput'),
        ingredients: formData.get('ingredientsInput'),
        instructions: formData.get('instructionsInput')
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
                <p><strong>Instructions:</strong> ${recipe.instructions.substring(0, 5)}</p>
                <hr>
            `;
            recipeElement.classList.add('recipe');
            const deleteButton = document.createElement('i');
            deleteButton.classList.add('fas', 'fa-times', 'delete-icon');
            deleteButton.addEventListener('click', () => deleteRecipe(recipe.id));
            recipeElement.appendChild(deleteButton);
            recipesDiv.appendChild(recipeElement);
        });
    }
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