"""A module to track daily food intake, nutritional goals."""

import gspread
import requests
from google.oauth2.service_account import Credentials
from dataclasses import dataclass
from datetime import datetime

# Set up the Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('calorietracker')
WORKSHEET = SHEET.worksheet("Entries")
GOALS_WORKSHEET = SHEET.worksheet("Goal")
WEEKTOTAL_WORKSHEET = SHEET.worksheet("WeekTotal")

API_KEY = "0brAMYcW8oY8uL4wFW6pEA==5CQZgsWVqQWDKyCr"
API_URL = "https://api.calorieninjas.com/v1/nutrition"


@dataclass
class Food:
    """Data class to store food item details."""
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int


class FoodTracker:
    """Tracks daily food intake, goals, and updates Google Sheets."""

    def main_menu(self):
        """Displays the main menu and handles user input."""
        done = False
        while not done:
            print(
                "\n(1) Add your meals for today\n"
                "(2) Record new daily goals\n"
                "(3) Review your daily goal's analysis\n"
                "(4) Calculate weekly totals\n"
                "(q) Quit\n"
            )

            choice = input("Enter your choice: ")

            if choice == "1":
                food_name = input(
                    "\nWhat did you have today? Log a meal - Food Item: "
                )
                use_api = input(
                    "\nDo you know the calorie and macronutrient values? "
                    "(y/n): "
                ).strip().lower()

                if use_api == 'n':
                    food = self.fetch_nutrition(food_name)
                    if food:
                        self.add_food(food)
                else:
                    calories = self.get_nutrient_input("Calories")
                    protein = self.get_nutrient_input("Protein")
                    fat = self.get_nutrient_input("Fat")
                    carbs = self.get_nutrient_input("Carbs")

                    food = Food(food_name, calories, protein, fat, carbs)
                    self.add_food(food)

            elif choice == "2":
                self.record_new_goals()

            elif choice == "3":
                self.calculate_goal_percentage()

            elif choice == "4":
                self.calculate_weekly_totals()

            elif choice.lower() == 'q':
                done = True
                print("Great job! You've logged all your calories for the day!")

            else:
                print("\nInvalid choice, please try again.")

    def __init__(self):
        self.today = []  # Stores daily food entries
        self.protein_goal = 100
        self.fat_goal = 70
        self.carbs_goal = 300

    def add_food(self, food: Food):
        """Adds a food entry to the list and logs it in Google Sheets."""
        self.today.append(food)
        self.add_to_google_sheets(food)

    def add_to_google_sheets(self, food: Food):
        """Appends a food entry to Google Sheets."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [
            timestamp, food.name, food.calories, food.protein,
            food.fat, food.carbs
        ]
        WORKSHEET.append_row(row)
        print("\nEntry added to Google Sheets successfully.")

    def update_goals_sheet(self):
        """Updates Google Sheets with consumed and goal data for the day."""
        protein_sum = sum(food.protein for food in self.today)
        fats_sum = sum(food.fat for food in self.today)
        carbs_sum = sum(food.carbs for food in self.today)

        timestamp = datetime.now().strftime("%Y-%m-%d")
        row = [
            timestamp, protein_sum, fats_sum, carbs_sum,
            self.protein_goal, self.fat_goal, self.carbs_goal
        ]

        GOALS_WORKSHEET.append_row(row)
        print("\nDaily consumed data and goals added to the goals worksheet.")

    def record_new_goals(self):
        """Prompts the user for new goals and updates the goals worksheet."""
        while True:
            try:
                self.protein_goal = int(input("Enter your new protein goal: "))
                self.fat_goal = int(input("Enter your new fat goal: "))
                self.carbs_goal = int(input("Enter your new carb goal: "))

                if any(
                    goal % 1 != 0 for goal in [
                        self.protein_goal, self.fat_goal, self.carbs_goal
                    ]
                ):
                    raise ValueError("Goals must be round numbers.")

                self.update_goals_sheet()
                print("\nNew goals set and logged successfully.")
                break

            except ValueError:
                print("Please enter valid round numbers for each goal.")

    def calculate_percentage(self, consumed, goal):
        """Calculate the percentage of the goal achieved."""
        if goal == 0:
            return 0
        percentage = (consumed / goal) * 100
        return min(percentage, 100) if percentage <= 100 else 100 - (
            percentage - 100
        )

    def calculate_goal_percentage(self):
        """Calculates and displays the percentage of daily goals reached."""
        if not self.today:
            print("No entry has been made yet.")
            return

        protein_sum = sum(food.protein for food in self.today)
        fats_sum = sum(food.fat for food in self.today)
        carbs_sum = sum(food.carbs for food in self.today)

        protein_score = self.calculate_percentage(protein_sum, self.protein_goal)
        fat_score = self.calculate_percentage(fats_sum, self.fat_goal)
        carbs_score = self.calculate_percentage(carbs_sum, self.carbs_goal)

        print("\nDaily Goal Achievement:")
        print(f"Protein: {protein_score:.2f}% of goal reached")
        print(f"Fat: {fat_score:.2f}% of goal reached")
        print(f"Carbs: {carbs_score:.2f}% of goal reached\n")

        self.update_goals_sheet()

    def calculate_weekly_totals(self):
        """Calculate weekly totals for calories and macronutrients."""
        entries = WORKSHEET.get_all_values()
        last_7_entries = entries[-7:] if len(entries) >= 7 else entries

        total_calories = sum(int(entry[2]) for entry in last_7_entries)
        total_protein = sum(int(entry[3]) for entry in last_7_entries)
        total_fat = sum(int(entry[4]) for entry in last_7_entries)
        total_carbs = sum(int(entry[5]) for entry in last_7_entries)

        timestamp = datetime.now().strftime("%Y-%m-%d")
        row = [
            timestamp, total_calories, total_protein,
            total_fat, total_carbs
        ]
        WEEKTOTAL_WORKSHEET.append_row(row)
        print("\nWeekly totals added to Google Sheets successfully.")

        print("\nWeekly Totals (Last 7 Days):")
        print(f"Total Calories: {total_calories}")
        print(f"Total Protein: {total_protein}g")
        print(f"Total Fat: {total_fat}g")
        print(f"Total Carbs: {total_carbs}g\n")

    def fetch_nutrition(self, food_name):
        headers = {"X-Api-Key": API_KEY}
        params = {"query": food_name}

        try:
            response = requests.get(
                API_URL, headers=headers, params=params, timeout=10
            )
            response.raise_for_status()
            data = response.json()

            if data["items"]:
                item = data["items"][0]

                food = Food(
                    name=food_name,
                    calories=int(item.get("calories", 0)),
                    protein=int(item.get("protein_g", 0)),
                    fat=int(item.get("fat_total_g", 0)),
                    carbs=int(item.get("carbohydrates_total_g", 0))
                )

                print(f"\nNutrition data retrieved for {food_name}:")
                print(
                    f"Calories: {food.calories}, Protein: {food.protein}g, "
                    f"Fat: {food.fat}g, Carbs: {food.carbs}g"
                )

                return food
            else:
                print("\nFood item not recognized.")
                return None
        except requests.RequestException as e:
            print(f"\nError fetching nutrition data: {e}")
            return None

    def get_nutrient_input(self, nutrient_name):
        """Helper method to get nutrient input from the user."""
        while True:
            try:
                value = int(input(f"{nutrient_name} (round number): "))
                if value <= 0:
                    print("Please enter a positive round number.")
                    continue
                return value
            except ValueError:
                print("\nInvalid input. Please enter a round number.")


if __name__ == "__main__":
    tracker = FoodTracker()
    tracker.main_menu()
