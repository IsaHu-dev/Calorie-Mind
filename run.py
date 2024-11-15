import gspread  # Library for Google Sheets operations
import requests  # For API requests to fetch nutritional data
from google.oauth2.service_account import Credentials  # Google authentication
from dataclasses import dataclass  # For defining structured data
from datetime import datetime  # For timestamping entries

# Configure API access and credentials for Google Sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",  # Access spreadsheets
    "https://www.googleapis.com/auth/drive.file",   # Access specific Drive files
    "https://www.googleapis.com/auth/drive",        # Full Drive access
]

CREDS = Credentials.from_service_account_file("creds.json")  # Load credentials
SCOPED_CREDS = CREDS.with_scopes(SCOPE)  # Apply API access scopes
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)  # Initialize Sheets client
SHEET = GSPREAD_CLIENT.open("calorietracker")  # Open the "calorietracker" spreadsheet
WORKSHEET = SHEET.worksheet("Entries")  # Worksheet for meal entries
GOALS_WORKSHEET = SHEET.worksheet("Goal")  # Worksheet for daily goals
WEEKTOTAL_WORKSHEET = SHEET.worksheet("WeekTotal")  # Worksheet for weekly totals

# API details for fetching nutritional information
API_KEY = "0brAMYcW8oY8uL4wFW6pEA==5CQZgsWVqQWDKyCr"
API_URL = "https://api.calorieninjas.com/v1/nutrition"


@dataclass
class Food:
    """Represents a food item with nutritional details."""
    name: str  # Name of the food
    calories: int  # Caloric value
    protein: int  # Protein content in grams
    fat: int  # Fat content in grams
    carbs: int  # Carbohydrate content in grams


class FoodTracker:
    """Manages food intake tracking, goal management, and data logging."""

    def __init__(self):
        self.today = []  # List of today's food entries
        self.protein_goal = 100  # Default protein goal in grams
        self.fat_goal = 70  # Default fat goal in grams
        self.carbs_goal = 300  # Default carbohydrate goal in grams

    def main_menu(self):
        """
        Displays the main menu and handles user interaction.
        Users can log meals, set goals, review progress, and calculate weekly totals.
        """
        done = False
        while not done:
            print(
                "\n(1) Add your meals for today\n"
                "(2) Record new daily goals\n"
                "(3) Review your daily goal's analysis\n"
                "(4) Calculate weekly totals\n"
                "(q) Quit\n"
            )
            choice = input("Enter your choice: ") # Prompt user for choice

            if choice == "1":  # Log a new meal
                food_name = input("What did you have today? Log a meal - Food Item: ")
                use_api = input("Do you know the calorie and macronutrient values? (y/n): ").strip().lower()

                if use_api == "n":  # Fetch nutritional data via API
                    food = self.fetch_nutrition(food_name)
                    if food:
                        self.add_food(food)
                else:  # Manually input nutritional data
                    calories = self.get_nutrient_input("Calories")
                    protein = self.get_nutrient_input("Protein")
                    fat = self.get_nutrient_input("Fat")
                    carbs = self.get_nutrient_input("Carbs")
                    food = Food(food_name, calories, protein, fat, carbs)
                    self.add_food(food)

            elif choice == "2":  # Record new nutritional goals
                self.record_new_goals()

            elif choice == "3":  # Display daily goal analysis
                self.calculate_goal_percentage()

            elif choice == "4":  # Calculate weekly nutritional totals
                self.calculate_weekly_totals()

            elif choice.lower() == "q":  # Exit the program
                done = True
                print("Great job! You've logged all your calories for the day!")

            else: # Invalid choice
                print("Invalid choice, please try again.")

    def add_food(self, food: Food):
        """Add a food entry and log it in Google Sheets."""
        self.today.append(food)  # Add to today's entries
        self.add_to_google_sheets(food)  # Log in Sheets

    def add_to_google_sheets(self, food: Food):
        """Log a food entry in the 'Entries' worksheet."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp
        row = [timestamp, food.name, food.calories, food.protein, food.fat, food.carbs]
        WORKSHEET.append_row(row)  # Append the entry to Google Sheets
        print("Entry added to Google Sheets successfully.")

    def update_goals_sheet(self):
        """Log daily totals and goals in the 'Goal' worksheet."""
        protein_sum = sum(food.protein for food in self.today)
        fats_sum = sum(food.fat for food in self.today)
        carbs_sum = sum(food.carbs for food in self.today)
        timestamp = datetime.now().strftime("%Y-%m-%d")
        row = [timestamp, protein_sum, fats_sum, carbs_sum, self.protein_goal, self.fat_goal, self.carbs_goal]
        GOALS_WORKSHEET.append_row(row)
        print("Daily consumed data and goals added to the goals worksheet.")

    def record_new_goals(self):
        """
        Prompts the user for new daily goals and updates them in Google Sheets.
        """
        while True:
            try:
                self.protein_goal = int(input("Enter your new protein goal: "))
                self.fat_goal = int(input("Enter your new fat goal: "))
                self.carbs_goal = int(input("Enter your new carb goal: "))
                self.update_goals_sheet()  # Save the new goals
                print("New goals set and logged successfully.")
                break
            except ValueError:
                print("Please enter valid numbers for each goal.")

    def calculate_percentage(self, consumed, goal):
        """
        Calculates the percentage of a goal achieved.
        Returns 0 if the goal is 0. A conditional check is used to determine if the self.today list is empty.
        """
        if goal == 0:
            return 0  # Avoid division by zero
        percentage = (consumed / goal) * 100
        return min(percentage, 100)  # Cap at 100%

    def calculate_goal_percentage(self):
        """Analyze and display the percentage of daily goals achieved."""
        if not self.today:
            print("No entries logged yet.")
            return
        protein_sum = sum(food.protein for food in self.today) # Summing up protein values from all food items logged today 
        fats_sum = sum(food.fat for food in self.today) 
        carbs_sum = sum(food.carbs for food in self.today) 

        protein_score = self.calculate_percentage(protein_sum, self.protein_goal) # protein_score = (protein_sum / protein_goal) * 100
        fat_score = self.calculate_percentage(fats_sum, self.fat_goal) # fat_score = (fats_sum / fat_goal) * 100
        carbs_score = self.calculate_percentage(carbs_sum, self.carbs_goal) # carbs_score = (carbs_sum / carbs_goal) * 100

        print("\nDaily Goal Achievement:")
        print(f"Protein: {protein_score:.2f}% of goal reached") # Display the protein goal percentage, rounded to 2 decimals
        print(f"Fat: {fat_score:.2f}% of goal reached")
        print(f"Carbs: {carbs_score:.2f}% of goal reached")
        self.update_goals_sheet()  # Log results

    def calculate_weekly_totals(self):
        """Calculate and log weekly totals for macronutrients and calories."""
        entries = WORKSHEET.get_all_values()
        last_7_entries = entries[-7:] if len(entries) >= 7 else entries  # Limit to last 7 entries
        total_calories = sum(int(entry[2]) for entry in last_7_entries)
        total_protein = sum(int(entry[3]) for entry in last_7_entries)
        total_fat = sum(int(entry[4]) for entry in last_7_entries)
        total_carbs = sum(int(entry[5]) for entry in last_7_entries)

        timestamp = datetime.now().strftime("%Y-%m-%d")
        row = [timestamp, total_calories, total_protein, total_fat, total_carbs]
        WEEKTOTAL_WORKSHEET.append_row(row)  # Log totals in Google Sheets
        print("Weekly totals added to Google Sheets successfully.")

    def fetch_nutrition(self, food_name):
        """Fetch nutritional data for a food item using an API."""
        headers = {"X-Api-Key": API_KEY}
        params = {"query": food_name}
        try:
            response = requests.get(API_URL, headers=headers, params=params, timeout=10) # Make a GET request to the API with the specified URL, headers, and query parameters
            response.raise_for_status() # This prevents further processing if the request fails
            data = response.json()
            if data["items"]: # Check if the API returned any data for the food item
                item = data["items"][0]
                food = Food(
                    name=food_name,
                    calories=int(item.get("calories", 0)), # Get calories, default to 0 if not present
                    protein=int(item.get("protein_g", 0)), # Get protein content in grams, default to 0
                    fat=int(item.get("fat_total_g", 0)), # Get total fat content in grams, default to 0
                    carbs=int(item.get("carbohydrates_total_g", 0)), # Get total carbohydrates in grams, default to 0
                )
                # Display the retrieved nutrition data to the user for confirmation
                print(f"Nutrition data retrieved for {food_name}:")
                print(f"Calories: {food.calories}, Protein: {food.protein}g, Fat: {food.fat}g, Carbs: {food.carbs}g")
                return food # Return the constructed Food object for further use (e.g., adding to today's log)
            else:
                print("Food item not recognized.") # Handle cases where the API doesn't recognize the food item
                return None
        except requests.RequestException as e:
            print(f"Error fetching nutrition data: {e}")
            return None

    def get_nutrient_input(self, nutrient_name):
        """Prompt user for nutrient input, validate, and handle errors by reverting to question."""
        while True:
            try:
                value = int(input(f"{nutrient_name}: "))  #Prompt the user for input and convert to a float for flexibility
                if value < 0:
                    print("Please enter a non-negative number.")
                    continue # Skip the rest of the loop and prompt the user again.
                return value # If the input passes all checks, return the value and exit the loop.
            except ValueError: # Catch cases where the input is not a valid number.
                print("Invalid input. Please enter a number.") # Inform the user about the error and prompt again.

if __name__ == "__main__":
    tracker = FoodTracker()  # Create an instance of the `FoodTracker` class, initializing the tracker for food-related operations.
    tracker.main_menu()  # Start the main menu. This serves as the entry point for the user to interact with the program.

