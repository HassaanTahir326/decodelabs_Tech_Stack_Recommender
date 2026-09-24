import sys
import os

# so "python src/main.py" also works, not just "python -m src.main"
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.recommender import TechStackRecommender


def get_user_skills():
    print("=== Tech Stack Recommender ===")
    print("Enter at least 3 skills, one at a time. Type 'done' to finish.\n")

    skills = []
    while True:
        skill = input(f"Skill #{len(skills) + 1}: ").strip()

        if skill.lower() == "done":
            if len(skills) < 3:
                print("Need at least 3 skills, keep going.")
                continue
            break

        if skill:
            skills.append(skill)

    return skills


def print_results(results):
    print("\nTop Recommended Career Paths:")

    # if fallback was used, let the user know
    if results and results[0].get("fallback"):
        print("(No close match found, showing trending roles instead)")

    for rank, item in enumerate(results, start=1):
        percent = item["score"] * 100
        print(f"{rank}. {item['role']} - match: {percent:.1f}%")


def main():
    recommender = TechStackRecommender()
    skills = get_user_skills()
    results = recommender.recommend(skills, top_n=3)
    print_results(results)


if __name__ == "__main__":
    main()