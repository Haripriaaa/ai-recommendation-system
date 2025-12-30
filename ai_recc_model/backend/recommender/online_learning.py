# online_learning.py

# This dictionary stores user preferences
# Example: { user_id: { "Programming": 2, "AI": 1 } }
user_preferences = {}


def update_preferences(user_id, course):
    """
    Updates user preferences when a user clicks a course.
    This is the online learning step.
    """

    category = course["category"]

    # If user is new, initialize their preferences
    if user_id not in user_preferences:
        user_preferences[user_id] = {}

    # Increase count for the clicked category
    if category not in user_preferences[user_id]:
        user_preferences[user_id][category] = 1
    else:
        user_preferences[user_id][category] += 1
