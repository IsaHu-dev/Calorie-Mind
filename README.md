# Calorie-Mind

## About

Calorie Mind is user-friendly app designed to help you take control of your daily nutrition and meet your fitness goals. Whether you're trying to manage your weight, fuel your workouts, or simply eat healthier, Calorie Mind provides all the tools you need to make mindful eating choices. With features like custom food entries, daily goal tracking, insightful progress analysis, and weekly summaries, Calorie Mind is your go-to guide for a balanced lifestyle. Think Calories with Calorie Mind.

### Target Users

Calorie Mind is designed for individuals aiming to promote healthier lifestyles through mindful calorie management and tracking. Target users include fitness-conscious individuals looking to optimize their nutrition, heart disease centres, and well-being clinics that aim to support clients in achieving balanced dietary habits. Calorie Mind is ideal for all ages who wish to be informed of their calorie intake for better health and a good lifestyle.

 # How to Use Calorie Mind

- Add Your meals
    - Select option 1 to add meals for the day.
    - You will be prompted to input a food item. If you're unsure about the nutritional information, simply enter the food name. Calorie Mind will retrieve the data via an API, providing the correct details for calories, protein, fat, and carbohydrates.

- Record New Daily Goals
    - Select option 2 to set your daily goals for macronutrients.
      You will be prompted to input your target goals for Protein, Fat, and Carbs. This allows you to tailor your intake to your personal nutrition needs. 

- View Daily Goal Analysis:
    - Select option 3 to review your daily goal analysis.
    - The console will display a percentage calculation showing how much of your daily goals have been met based on your food entries.

- Calculate Weekly Totals:
    - Calorie Mind will calculate and display the total values for Calories, Protein, and Fat over the last seven days, helping you track your progress and adjust your diet if needed.

# Features

   ![Image of Console](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/console.png)
   

## Existing Features

- Calorie Mind provides a straightforward, command-driven interface, facilitating efficient navigation and nutrition tracking via a number selection. Each feature supports mindful eating practices, enabling dietary adjustments aligned with health and fitness objectives.

    1. Add your Dinner - Input dinner entries.
    
    - Select 1 to add a dinner entry. If nutritional information is unknown, the application initiates an API request to retrieve accurate values (calories, protein, fat, and carbs). 
    
    - You can log more than one meal per day

    - Ensures the food intake logs for daily tracking.    

     2. Record New Daily Goals
    
    - Set daily macronutrient targets for protein, fat, and carbs. This feature helps you stay aligned 
      with your nutrition goals and maintain a balanced diet.

    - This function sums up your new daily goals.

     3. Review Your Daily Goal's Analysis

    - Your daily goals are calculated as a percentage printed to the console, showing your progress toward your targets. It compares the consumed data and goal data, then outputs it as a percentage.

    - It calculates the sum of your daily protein, fats and carbs entries and outputs a percentage of your daily goal.     

     4. Calculate Weekly Totals

     - Track your weekly progress by calculating the total calories, protein, and fat consumed over the last seven days - to help assess and adjust your diet over time.

     - The app utilizes the gspread and google-auth libraries to interact with Google Sheets, using them as a cloud-based database for data storage and retrieval. Therefore, Google Worksheets serves as a lightweight database, enabling seamless data updates and retrievals from designated worksheets.
     
     5. q for Quit

     - Quit the program at any time by selecting' q'. The program exits.
       A message is printed to the console: "Great job! You've successfully logged all your calories for the day!"    

 ### Additional notes: 

  Use of Libraries

  - The gspread library manages API communication with Google Sheets, while google-auth handles authentication to ensure secure access to the spreadsheet data.

  - For example, the gspread library plays a significant role in collecting data for weekly totals by retrieving the last 7 entries from the Google Sheet. Based on a date timestamp recorded with each entry, these entries are accessed from the "Week Total" sheet, allowing for calculation and display of weekly data collection.  

   Entries Worksheet

   ![Daily Entries worksheet](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/entries.png)
   Goals Worksheet

   ![Daily Goals worksheet](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/goals.png)
   Weekly Totals Worksheet

   ![Weekly Totals worksheet](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/weeklytotals.png)    


 ### UX Design (Basic): 

  - Improved console output readability by adding line spacing for clearer print results.(\n)

## Future Features

  - Add a GUI interface and upgrade from a mock terminal.
  - Expand Weekly Totals features to alert the user if they skipped a day. It currently calculates the last seven days.
  - Add a leaderboard on scores once the GUI is designed and implemented.

## Flowchart

![Flowchart](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/flowchart.png)

# Testing

## Manual Testing

| Test Case                         | Expected Result                                                                     | Test Result |
|-----------------------------------|-----------------------------------------------------------------------              |-------------|
| Run program                       | Click run program.  The app will appear with a multiple choice selection.           | ✅ PASS          |
| Select option 1                   | Prompt user to enter their protein, fat and carbs.                                  | ✅ PASS          |
| Select option 1                   | Prompt user to select if they know the macronutrient values. Select n (no) or y (yes).                                                                                                                    | ✅ PASS          |
| Select option 1                   | Retrieve API from Calorie Ninjas                                                    | ✅ PASS          |
| Handles invalid input data        | The app recognises an unrecognised item, the console will display a message "Food item not recognized"                                                      | ✅ PASS          |
| Select option 2                   | Prompt to input your daily target goals for Protein, Fat, and Carbs.                | ✅ PASS          |
| Detects no user input             | The console will display a message "No entry has been made yet" (when it detects self.today list is empty)                | ✅ PASS          |
| Select option 3                   | The console will display a percentage calculation showing how much of your daily goals have been met based on food entries.                                                                                                                  | ✅ PASS          |
| Handles invalid input data        | The console will display a messsage "Please enter valid round numbers for each goal."| ✅ PASS          |
| Selection option 4.               | Calculates weekly totals of calories and macronutrients. Retrieves from Google worksheet and sums up the last 7 entries.    | ✅ PASS          |
| Select q                          | Select q for quit. Exits mock terminal program.                                     | ✅ PASS          |


   ![Calorie and Macronutrient entries](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/usertesting.png)
   
## Bugs/Updates after Testing

At the start of coding the app, I ran into some bugs. The following bugs I encountered are as follows:

- Indentation Fixes: Corrected indentation issues, especially in the calculate_goal_percentage method.

- Issue: Previously, the application would throw an error when the API could not find a specified food item. 
  Solution: Added exception handling to manage cases where the API does not recognize the food item or if there’s invalid input. Now, when this occurs, the application catches the error and prints a helpful message— “Food item not recognised”— to the console. 

- Add a conditional check for invalid user input or when the user inputs a decimal point or letters to enter calories and macronutrients. 
  The application would reset to the main menu if users entered non-integer values, such as decimals, letters, or special characters.

-  A bug was identified where the value 0 was incorrectly rejected as valid input for nutrient values. To resolve this, a new function,         get_nutrient_input, has been implemented. This function enforces input validation by ensuring the provided value is a non-negative integer, 
  specifically allowing both 0 and positive integers as valid inputs.

   The screenshot below (Figure 1.0) demonstrates the issue where the value 0 was not accepted. This bug has been resolved in the current implementation.

Figure 1.0 
  ![Bug fix](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/roundnumber.png)

All bugs are presently fixed.

## Code Style and Readability

- Format code with Black Python Formatter to maintain consistent code style and readability.

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
  - [Calorie Ninja API documentation](https://calorieninjas.com/api)
  - [Stack Overflow](https://stackoverflow.com/questions/10004850/python-classes-and-oop-basics)

 ## Code Attribution

  - This project uses modified code for the Google Sheets API and client setup, based on the "Love Sandwiches" walkthrough by Code Institute. The   
    remaining code is original and was developed independently for this project.

  ![Code Attribution](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/codeatt.png)

  ## Acknowledgements
  - Thanks to Moritz Wach - mentor for PP3 guidance.

 