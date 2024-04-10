import csv

person_scores = {}

with open("newcsv.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        name = row[0]
        score = int(row[2])
        if name in person_scores:
            person_scores[name].append(score)
        else:
            person_scores[name] = [score]

for person, scores in person_scores.items():
    print(f"სტუდენტის ქულა: {person}: {scores}")
    average_score = sum(scores) / len(scores)
    print(f"საშუალო ქულები: {person}: {average_score}")

