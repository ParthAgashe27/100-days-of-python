student_scores = [85, 942, 78, 90, 88]
highest_score = student_scores[0]  # Initialize highest_score with the first score
for score in student_scores:    # Iterate through each score in the list
    if score > highest_score:  # Compare current score with highest_score
        highest_score = score
print(f"The highest score is: {highest_score}")

