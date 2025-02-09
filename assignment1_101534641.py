"""
Author: Samin Qureshi
Assignment: #1
"""

# Variable declarations with data types
member_name = "Alex Alliton"  # str
target_weight_kg = 20.5  # float
max_reps = 25  # int
is_membership_active = True  # bool

# Dictionary holding workout statistics
workout_data = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 15),
    "Taylor": (40, 35, 25)
}

# Compute total workout minutes and add to dictionary
workout_totals = {name + "_Total": sum(minutes) for name, minutes in workout_data.items()}
workout_data.update(workout_totals)

# Construct a 2D list of workout details
workout_matrix = [list(minutes) for name, minutes in workout_data.items() if isinstance(minutes, tuple)]

# Extracting specific workout details
yoga_running = [row[:2] for row in workout_matrix]
weightlifting_last_two = [row[2] for row in workout_matrix[-2:]]

print("Yoga and Running Minutes for all friends:", yoga_running)
print("Weightlifting Minutes for the last two friends:", weightlifting_last_two)

# Identify highly active friends
print("\nFriends with great activity levels:")
for name, total in workout_totals.items():
    if total >= 120:
        print(f" - Great job staying active, {name.replace('_Total', '')}!")

# Interactive friend lookup
while True:
    query = input("\nEnter a friend's name to view their workout stats (or 'exit' to quit): ").strip()
    if query.lower() == 'exit':
        print("Goodbye!")
        break
    
    # Case-insensitive lookup
    normalized_data = {key.lower(): val for key, val in workout_data.items()}
    if query.lower() in normalized_data:
        friend_key = query.capitalize()
        stats = workout_data.get(friend_key, (0, 0, 0))
        total = workout_data.get(f"{friend_key}_Total", sum(stats))
        
        print(f"\n{friend_key}'s Workout Stats:")
        print(f" - Yoga: {stats[0]} minutes")
        print(f" - Running: {stats[1]} minutes")
        print(f" - Weightlifting: {stats[2]} minutes")
        print(f" - Total Workout Minutes: {total}")
    else:
        print(f"\nFriend '{query}' not found in the records. Please check the name and try again.")

# Finding the most and least active friends
total_minutes = {name: total for name, total in workout_totals.items()}
highest_achiever = max(total_minutes, key=total_minutes.get).replace("_Total", "")
lowest_achiever = min(total_minutes, key=total_minutes.get).replace("_Total", "")

print(f"\nFriend with the highest total workout minutes: {highest_achiever} ({total_minutes[highest_achiever+'_Total']} minutes)")
print(f"Friend with the lowest total workout minutes: {lowest_achiever} ({total_minutes[lowest_achiever+'_Total']} minutes)")
