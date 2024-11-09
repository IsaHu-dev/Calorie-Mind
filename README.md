# Calorie-Mind

## About

Calorie Mind is a powerful and user-friendly app designed to help you take control of your daily nutrition and meet your fitness goals. Whether you're trying to manage your weight, fuel your workouts, or simply eat healthier, Calorie Mind provides all the tools you need to make mindful eating choices. With features like custom food entries, daily goal tracking, insightful progress analysis, and weekly summaries, Calorie Mind is your go-to guide for a balanced lifestyle. Think Calories with Calorie Mind.

 # How to Use Calorie Mind

- Add Your Dinner
    - Select option 1 to add your dinner.
    - You will be prompted to input a food item. If you're unsure about the nutritional information, simply enter the food name, and Calorie Mind will retrieve the data via an API, providing the correct details for calories, protein, fat, and carbohydrates.

- Record New Daily Goals
    - Select option 2 to set your daily goals for macronutrients.
      You will be prompted to input your target goals for Protein, Fat, and Carbs. This allows you to tailor your intake to your personal nutrition needs. 

- View Daily Goal Analysis:
    - Select option 3 to review your daily goal analysis.
    - A percentage calculation will be displayed in the console, showing how much of your daily goals   
      have been met based on your food entries.

- Calculate Weekly Totals:
    - Calorie Mind will calculate and display the total values for Calories, Protein, and Fat over the past seven days, helping you track your progress and adjust your diet if needed.
              
## Existing Features

- Calorie Mind provides a straightforward, command-driven interface, facilitating efficient navigation and nutrition tracking via a number selection. Each feature supports mindful eating practices, enabling dietary adjustments aligned with health and fitness objectives.

    1. Add your Dinner - Input dinner entries.
    
    - Select 1 to add a dinner entry. If nutritional information is unknown, the application initiates an API request to retrieve accurate values (calories, protein, fat, and carbs).
    
    - Ensures the logging of food intake for daily tracking.    

     2. Record New Daily Goals
    
    - Set daily macronutrient targets for protein, fat, and carbs. This feature helps you stay aligned 
      with your nutrition goals and maintain a balanced diet.

     3. Review Your Daily Goal's Analysis

        Your daily goals are calculated as a percentage printed to the console, showing your progress toward your targets. It compares the consumed data and goal data, then outputs it as a percentage.

     4. Calculate Weekly Totals

     - Track your weekly progress by calculating the total calories, protein, and fat consumed over the last seven days - to help assess and adjust your diet over time.

     5. q for Quit

     - Quit the program at any time by selectiong 'q'. The program exits.
       A message is printed to the console "Great job! You've successfully logged all your calories for the day!"   


## Future Features

- Add a GUI interface - upgrade from a mock terminal.
- Expand Meal Entry Options. Include Breakfast and Lunch in Totals Calculations
- Extend the New Daily Goals and Weekly Totals features to incorporate Breakfast and Lunch data, allowing users to view cumulative 
  weekly values across all meals.
- Add functionality to calculate and display percentage goal completion for Breakfast and Lunch entries, enabling users to monitor 
  progress toward daily targets on a meal-specific basis.

# Testing

## Manual Testing


| Test Case                         | Expected Result                                                                     | Test Result |
|-----------------------------------|-----------------------------------------------------------------------              |-------------|
| run program                       | Click run program.  The app will appear with a multiple choice selection            | ✅ PASS          |
| Select option 1                   | Prompt for user to enter their protein, fat and carbs.                              | ✅ PASS          |
| Select option 1                   | Prompt user to select if they know the macronutrient values. Select n or y.                                                                                                                        | ✅ PASS          |
| Select option 1                   | Retrieve from API Calorie Ninjas                                                    | ✅ PASS          |                                
| Select option 2                   | Prompt to input your daily target goals for Protein, Fat, and Carbs.                                                                                                                    | ✅ PASS          |
| Select option 3                   | A percentage calculation will be displayed in the console, showing how much of your daily goals   have been met based on food entries.                                                                                      | ✅ PASS          |                       
| Select option 4                   | Calculates weekly totals. Retrieves from Google worksheet and sums up the last 7 entries.                                                                                                                  | ✅ PASS          |                           
| Select q                          | Select q for quit. Exits mock terminal program.                                     | ✅ PASS          |

## Bugs/Updates after Testing

At the start of coding the app, I had run into some bugs. The following bugs I encountered are as follows:

- Indentation Fixes: Corrected indentation issues, especially in the calculate_goal_percentage method.

- Incorrect nested function:  Moved calculate_percentage out as a separate method within FoodTracker.

- Syntax Adjustments: Cleaned up syntax and formatting for readability.

All bugs are presently fixed.
