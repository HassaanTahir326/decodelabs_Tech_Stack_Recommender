import os
import pandas as pd

# path to our csv file, no matter where we run the script from
DEFAULT_DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "raw_skills.csv",
)


def load_job_roles(csv_path=DEFAULT_DATA_PATH):
    # load the csv into a table (DataFrame)
    df = pd.read_csv(csv_path)

    # split "Python;SQL;AWS" into ["Python", "SQL", "AWS"]
    df["skills_list"] = df["skills"].apply(_split_skills)

    # turn that list into one clean string for TF-IDF, e.g. "python sql aws"
    df["skills_text"] = df["skills_list"].apply(
        lambda tags: " ".join(_tokenize(tag) for tag in tags)
    )

    return df


def _split_skills(raw):
    # breaks "Python;SQL" into ["Python", "SQL"]
    return [tag.strip() for tag in str(raw).split(";") if tag.strip()]


def _tokenize(tag):
    # "Machine Learning" -> "machine_learning" (so it stays ONE word/token)
    return tag.strip().lower().replace(" ", "_")


def build_user_query(user_skills):
    # do the same cleanup for whatever skills the user typed in
    return " ".join(_tokenize(skill) for skill in user_skills)