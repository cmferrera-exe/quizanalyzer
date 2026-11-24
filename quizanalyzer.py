scores = []

for i in range(1, 6):
    score = int(input(f"Enter score {i}: "))
    scores.append(score)

total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)
ascending = sorted(scores)
descending = sorted(scores, reverse=True)

print("\n===== QUIZ REPORT =====")
print(f"Quiz Scores: {scores}")
print("Number of quizzes: ", len(scores))
print(f"Total score: {total}")
print(f"Average score: {average: .2f}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Ascending: {ascending}")
print(f"Descending: {descending}")
print(f"Original Scores: {scores}")











