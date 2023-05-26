import csv
import random

skills = ["database", "backend", "smart contracts", "solidity", "bitcoin", "ethereum", "hyperledger"]

with open('user_table.csv', mode='w', newline='') as csv_file:
    fieldnames = ['score', 'name', 'skill']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(1000):
        name = f"User{i}"
        num_skills = random.randint(3, 7)
        user_skills = random.sample(skills, num_skills)
        score = round(random.uniform(70, 100), 2)

        for skill in user_skills:
            writer.writerow({'score': score, 'name': name, 'skill': skill})
