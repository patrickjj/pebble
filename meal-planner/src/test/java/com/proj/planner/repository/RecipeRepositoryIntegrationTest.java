package com.proj.planner.repository;

import com.proj.planner.models.Recipe;
import com.proj.planner.repository.RecipeRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@DataJpaTest
public class RecipeRepositoryIntegrationTest {

    @Autowired
    private RecipeRepository recipeRepository;

    @Test
    public void testSaveRecipe() {
        Recipe recipe = new Recipe();
        recipe.setName("Test Recipe");
        recipe.setDescription("Test Description");

        Recipe savedRecipe = recipeRepository.save(recipe);

        Optional<Recipe> fetchedRecipe = recipeRepository.findById(savedRecipe.getId());
        assertTrue(fetchedRecipe.isPresent());
        assertEquals("Test Recipe", fetchedRecipe.get().getName());
        assertEquals("Test Description", fetchedRecipe.get().getDescription());
    }

    @Test
    public void testFindAllRecipes() {
        Recipe recipe1 = new Recipe();
        recipe1.setName("Recipe 1");
        recipe1.setDescription("Description 1");
        recipeRepository.save(recipe1);

        Recipe recipe2 = new Recipe();
        recipe2.setName("Recipe 2");
        recipe2.setDescription("Description 2");
        recipeRepository.save(recipe2);

        List<Recipe> recipes = recipeRepository.findAll();

        assertEquals(2, recipes.size());
    }

}
