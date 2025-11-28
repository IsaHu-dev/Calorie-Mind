# Calorie-Mind

## About

Calorie Mind is a user-friendly app designed to help you take control of your daily nutrition and meet your fitness goals. Whether you're trying to manage your weight, fuel your workouts, or simply eat healthier, Calorie Mind provides all the tools you need to make mindful eating choices. With features like custom food entries, daily goal tracking, insightful progress analysis, and weekly summaries, Calorie Mind is your go-to guide for a balanced lifestyle. Think Calories with Calorie Mind.

### Target Users

Calorie Mind is designed for individuals aiming to promote healthier lifestyles through mindful calorie management and tracking. Target users include fitness-conscious individuals looking to optimize their nutrition, heart disease centres, and well-being clinics that aim to support clients in achieving balanced dietary habits. Calorie Mind is ideal for all ages who wish to be informed of their calorie intake for better health and a good lifestyle.

 # How to Use Calorie Mind

- Add Your meals
    - Select option 1 to add meals for the day.
    - You will be prompted to input a food item. If you're unsure about the nutritional information, enter the food name and answer (n) to the question. Calorie Mind will retrieve the data matching the correct details to the food item for calories, protein, fat, and carbohydrates.

- Record New Daily Goals
    - Select option 2 to set your daily goals for macronutrients.
    - You will be prompted to input your target goals for Protein, Fat, and Carbs. This allows you to tailor your intake to your personal nutrition needs. 
    - This option allows you to override the default macronutrient goals with custom values.

- View Daily Goal Analysis:
    - Select option 3 to review your daily goal analysis.
    - The console will display a percentage calculation showing how much of your daily goals have been met based on your food entries.

- Calculate Weekly Totals:
    - Select option 4 - Calorie Mind will calculate and display the total values for Calories, Protein, and Fat over the last seven days, helping you track your progress and adjust your diet if needed.

# Features

   ![Image of Console](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/console.png)
   

## Existing Features

Calorie Mind provides a straightforward, command-driven interface that is user-friendly and allows you to track your daily calories via a number selection. 

1 - Add your daily meals, typically breakfast, lunch and dinner - Input food items of your choice.

  - The app allows the user to select n (no) or y (yes) when the user is asked "Do you know the calorie and macronutrient values? If nutritional information is unknown, the application initiates an API request to retrieve accurate values (calories, protein, fat, and carbs). 

  - You can log more than one meal per day

  - Daily food calorie and macronutrient intakes are logged into the designated worksheet: Entries.

2 - Record New Daily Goals  

  - Set daily macronutrient targets for protein, fat, and carbs. This feature helps you stay aligned with your nutrition goals and maintain a balanced diet.

  - This function allows users to input new daily goals and replace them with custom values.

      The application is pre-configured with the following default daily macronutrient targets:   
         
     -   protein goal = 100

     -   fat goal = 70
         
     -   carbs goal = 200

     - New daily food calorie and macronutrient goals are logged into the designated Google worksheet: Goal.

3 - Review Your Daily Goal's Analysis  

  - The daily macronutrient entries are totalled, and a percentage is calculated for each macronutrient (protein, fat, and carbohydrates) relative to the daily set goals.
   
  - Your daily goals are calculated as a percentage, showing your progress toward your targets. It compares the consumed data and goal data, then outputs it as a percentage.

     i.e,. this is the percentage calculation: 

      -   Protein: (34 / 100) * 100 = 34%
      -   Fat: (4 / 70) * 100 = 5.71%                 
      -   Carbs: (45 / 200) * 100 = 22.5%

  - These calculations help create a logical nutrition plan, whether it’s for weight loss, muscle gain, or maintaining a healthy diet. Calorie Mind is not merely about weight loss.


4 - Calculate Weekly Totals

  - Track your weekly progress by calculating the total calories, protein, and fat consumed over the last seven days.

  - The gspread library retrieves the last 7 entries from Google Sheet for a weekly data analysis. Each entry is recorded with a timestamp, which is used to identify and access the relevant data from the "Week Total" sheet. This functionality enables the accurate calculation of the weekly totals, providing a clear overview of weekly progress. 

  -  Weekly totals are displayed on the console.

  -  Weekly totals are logged into the designated Google worksheet: Week Total.

5 - q for Quit

  - Quit the program at any time by selecting' q'. The program exits.
    A message is printed to the console: "Great job! You've successfully logged all your calories for the day!"    

 
 ### Additional notes: 

  Use of Libraries

  - The gspread library manages API communication with Google Sheets, while google-auth handles authentication to ensure secure access to the spreadsheet data.

  - Google Sheets acts as a lightweight cloud-based database, allowing seamless data storage, updates, and retrieval from designated worksheets.
 
   
   ![Daily Entries worksheet](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/entries.png)
    Entries Worksheet

   ![Daily Goals worksheet](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/goals.png)
    Goals Worksheet

   ![Weekly Totals worksheet](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/weeklytotals.png)    
    Weekly Totals Worksheet

### Google Sheets Link

- Please click on this link to view the Google worksheets and Entries, Goal and Worktotal sheets:
  https://docs.google.com/spreadsheets/d/1AolucGwHaHIfdgWZprr5FXCtpJqEvPUGCzdBgGhvJrc/edit?usp=sharing. Access is granted with this link.

### Basic UX Design: 

  - Improved console output readability by adding line spacing for clearer print results.

## Future Features

  - Add a GUI interface and upgrade from a mock terminal.
  - Expand Weekly Totals features to alert users if they skipped a day. It currently calculates the last seven days.
  - Add a leaderboard on scores once the GUI is designed and implemented.

## Flowchart

![Flowchart](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/flowchart.png)

# Testing

## Manual Testing

| Test Case                         | Expected Result                                                                     | Test Result |
|-----------------------------------|-----------------------------------------------------------------------              |-------------|
| Run program                       | Click run program.  The app will appear with a multiple choice selection.           | ✅ PASS          |
| Prompt user input                 | Prompt user to enter a food item.                                                   | ✅ PASS          |
| Prompt user input                 | Prompt user to select if they know the macronutrient values. Select n (no) or y (yes).    | ✅ PASS          |
| User input 'y' (y)                | Prompt user to enter their protein, fat and carbs.                                  | ✅ PASS          |
| User input 'n' (no)               | Retrieve API from Calorie Ninjas.                                                   | ✅ PASS          |
| Outputs results to console        | Outputs daily nutrients result to console.                                          | ✅ PASS          |
| Daily nutrients appends worksheet | User inputs daily nutrients, which are appended to the 'Entries' worksheet.         | ✅ PASS          |
| Handles invalid input data        | If the API does not recognize a food item, the app displays the message: 'Food item not recognized'.                                                                                                                                       | ✅ PASS          |
| Select option 2                   | Prompt user to input your daily target goals for Protein, Fat, and Carbs.                | ✅ PASS          |
| No user input detected            | The console will display a message "No entry has been made yet"                     | ✅ PASS          |
| Handles invalid input data        | Prompt the user to input a nutrient value, validate it as a non-negative integer (round number).                         | ✅ PASS  
| Daily goals appends to worksheet  | Default goals added to worksheet if there are no new daily goal entries (option 2). | ✅ PASS          |
| Daily goals appends to worksheet  | User inputs new goals, which are appended to the 'Goal' worksheet.                  | ✅ PASS          |
| Select option 3                   | The console will display a percentage calculation showing how much of your daily goals have been met based on food entries.                                                                                                                  | ✅ PASS          |
| Select option 4                   | Calculates weekly totals of calories and macronutrients. Retrieves from Google worksheet and sums up the last 7 entries.    | ✅ PASS          |
| Outputs results to console        | Outputs weekly totals result to console.                                            | ✅ PASS          |
| Weekly totals appends to worksheet| User inputs option 4. Weekly totals appends to worksheet 'Week Totals'.             | ✅ PASS          |
| Handles invalid input data        | Identifies empty or invalid non-numeric entries in Google worksheet columns.        | ✅ PASS          |
| Select q                          | Select q for quit. Exits mock terminal program.                                     | ✅ PASS          |


   ![Calorie and Macronutrient entries](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/usertesting.png)
   
## Bugs/Updates after Testing

At the beginning of coding the app, I ran into some bugs. The following bugs I encountered are as follows:

- Indentation Fixes: Corrected indentation issues, especially in the calculate_goal_percentage method.

- Issue: Previously, the application would throw an error when the API could not find a specified food item. 
  
  Solution: Added exception handling to manage cases where the API does not recognize the food item or if there’s invalid input. Now, when this occurs, the application catches the error and prints a helpful message— “Food item not recognised” to the console. 

- Issue: The application would reset to the main menu if users entered non-integer values, such as decimals, letters, or special characters. 

  Solution: Add a conditional check to handle invalid user input. Prompt the user to enter a nutrient value, validate it as a non-negative integer, and skip returning to the main menu.

-  A bug was identified where the value 0 was incorrectly rejected as valid input for nutrient values. To resolve this, a new function, 'get_nutrient_input', has been    implemented. This function enforces input validation by ensuring the provided value is a non-negative integer, specifically allowing both 0 and positive integers as valid inputs.

   The screenshot below (Figure 1.0) demonstrates the issue where the value 0 was not accepted. This bug has been resolved in the current implementation.

Figure 1.0 
  ![Bug fix](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/roundnumber.png)


- Issue: At the end of the project, the application threw an error when there were empty columns in Google worksheets.

  Solution: In the calculate_weekly_totals function, a validation step is added to ensure only numeric values are summed.

All bugs are presently fixed.

## Code Style and Readability

- The code is formatted with the Black Python Formatter to maintain consistent code style and readability.

## Validator Testing

- Passed the CI Python Linter. "All clear no errors found"

- Please note that the validation testing was completed prior to adding comments to the code.

 ![CI Python Linter](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/cilinter.png)

- Fully passed the PYLINT VALIDATOR - a pep8 tool.
![Pylint](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/pylint.png)

# Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

The steps for deployment are as follows:

- Create a new Heroku app
- Set the build packs to Python and NodeJS in that order
- Link the Heroku app to the Github repository 'Calorie Mind'
- Click on Deploy

## Credits 

  - The python code for the app Calorie Mind was refactored to adopt an object-oriented approach. I sourced this youtube tutorial and used it as a rough guide: https://www.youtube.com/watch?v=0-LDsQpKYFU

  - [Real Python](https://realpython.com/.com/)
  - [Calorie Ninja API documentation](https://calorieninjas.com/api) - The API is used only.
  - [Stack Overflow](https://stackoverflow.com/questions/10004850/python-classes-and-oop-basics)
  - [w3schools - Python](https://www.w3schools.com/python/ref_string_isdigit.asp)

 ## Code Attribution

  - This project uses modified code for the Google Sheets API and client setup, based on the "Love Sandwiches" walkthrough by Code Institute. The remaining code is original and was developed independently for this project.

  ![Code Attribution](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/codeatt.png)

  ## Acknowledgements
  - Thanks to Moritz Wach - mentor for PP3 guidance.

 