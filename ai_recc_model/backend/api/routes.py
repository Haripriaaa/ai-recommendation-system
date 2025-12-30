from recommender.model import COURSES
from recommender.recommend import get_recommendations
from recommender.online_learning import update_preferences

def search_courses(query):
    query = query.lower()

    # 1. Search results (keyword match)
    search_results = [
        c for c in COURSES if query in c["title"].lower()
    ]

    # 2. If nothing found, return empty safely
    if not search_results:
        return [], []

    # 3. Extract categories ONLY from searched results
    searched_categories = {c["category"] for c in search_results}

    # 4. Recommend ONLY related courses (same category, not duplicates)
    recommendations = [
        c for c in COURSES
        if c["category"] in searched_categories and c not in search_results
    ]

    return search_results, recommendations



def recommend_courses(user_id):
    return get_recommendations(user_id)


def user_clicked_course(user_id, course_id):
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if course:
        update_preferences(user_id, course)
        return {"message": "User behaviour recorded"}
    return {"error": "Course not found"}
