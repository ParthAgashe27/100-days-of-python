student_scores = {
    'Akash': 76, 
    'Ajay': 94,
    'Sanjay': 72,
    'Vijay': 68,
    'Yash': 82
}

student_grade = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grade[student] = 'Outstanding'
        
    elif score >= 81:
        student_grade[student] = 'Exceeds Expectations'
       
    elif score >= 71:
        student_grade[student] = 'Acceptable'
        
    else:
        student_grade[student] = 'Fail'
    
print(student_grade)
     


