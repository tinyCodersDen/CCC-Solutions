# The problem name is "Multiple Choice"
x = int(input())
correct_responses = 0
student_responses = []
for t in range(x):
    v = input('')
    student_responses.append(v)
for q in range(x):
    d = input('')
    if d==student_responses[q]:
        correct_responses+=1
print(correct_responses)
