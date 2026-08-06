import requests
from datetime import datetime

WEIGHT_POUNDS = 150  # User's weight in pounds
today_time = datetime.now().strftime("%H:%M:%S")
today_date = datetime.now().strftime("%d/%m/%Y")

activity = input("Enter the activity you performed: ")

calories_endpoint = "https://api.api-ninjas.com/v1/caloriesburned"

calories_headers = {
    "X-Api-Key": "API_KEY"  # Replace with your actual API key
}

calories_params = {
    "activity": activity,
    "weight": WEIGHT_POUNDS,
    "duration": int(input("Enter the duration in minutes: "))
}

response = requests.get(url=calories_endpoint, headers=calories_headers, params=calories_params)
results = response.json()

if len(results) == 0:
    print("No match found for that activity.")
    exit()
elif len(results) == 1:
    matched_activity = results[0]
else:
    # multiple matches - show the user their names and let THEM pick
    for i, entry in enumerate(results):
        print(f"{i}: {entry['name']}")
    choice = int(input("Which one matches what you did? Enter the number: "))
    matched_activity = results[choice]

calories_burned = matched_activity['total_calories']

sheety_endpoint = "YOUR_SHEETY_ENDPOINT"  # Replace with your actual Sheety endpoint
sheety_headers = {
    "Authorization": "YOUR_SHEETY_API_KEY"  # Replace with your actual Sheety API key
}
sheety_input = {
    "workout": { 
        "date": today_date,
        "time": today_time,
        "exercise": activity.title(),
        "duration": f"{calories_params["duration"]} minutes",
        "calories": calories_burned
    }
}

sheet_response = requests.post(url=sheety_endpoint, json=sheety_input, headers=sheety_headers)
if sheet_response.status_code == 200:
    print("Workout logged successfully!")
else:
    print("Failed to log workout.")
    print(sheet_response.text)
