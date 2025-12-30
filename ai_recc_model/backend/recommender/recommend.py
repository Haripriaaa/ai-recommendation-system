# recommend.py

from .model import COURSES
from .online_learning import user_preferences


def get_recommendations(user_id):
    """
    Returns personalized course recommendations
    based on learned user preferences.
    """

    # If user has no preferences yet, return all courses
    if user_id not in user_preferences:
        return COURSES

    preferred_categories = user_preferences[user_id]

    # Sort courses based on preference count
    sorted_courses = sorted(
        COURSES,
        key=lambda course: preferred_categories.get(course["category"], 0),
        reverse=True
    )

    return sorted_courses
