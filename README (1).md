# Tech Stack Recommender

This is my Project 3 for the DecodeLabs internship.

## What it does

You type in at least 3 skills (like Python, SQL, AWS) and the program
tells you which job role fits you best — for example "Data Scientist"
or "Cloud Architect".

It's a simple recommendation system, like how Netflix suggests movies,
but here it suggests career paths based on your skills.

## How it works (in simple terms)

1. You enter your skills.
2. The program turns your skills and each job role's skills into
   numbers (this is called TF-IDF).
3. It compares your numbers with each job role's numbers to see how
   close they are (this is called Cosine Similarity).
4. It shows you the Top 3 job roles that match you best.

## Folder structure

```
tech_stack_recommender/
├── data/
│   └── raw_skills.csv     -> list of job roles and their skills
├── src/
│   ├── data_loader.py     -> reads and cleans the CSV file
│   ├── vectorizer.py      -> turns text into numbers and compares them
│   ├── recommender.py     -> puts everything together, gives Top 3
│   └── main.py            -> the file you actually run
├── requirements.txt       -> list of libraries needed
└── README.md
```

## How to run it

1. Install the required libraries:
```
pip install -r requirements.txt
```

2. Run the program:
```
python -m src.main
```

3. Type in at least 3 skills when it asks, then type `done`.

## Example

```
Skill #1: Python
Skill #2: Cloud Computing
Skill #3: Automation
Skill #4: done

Top Recommended Career Paths:
1. Data Engineer      match: 55.8%
2. Network Engineer   match: 41.1%
3. Cloud Architect    match: 39.9%
```

## Tools used

- Python
- pandas (to read the CSV file)
- scikit-learn (for TF-IDF and Cosine Similarity)
