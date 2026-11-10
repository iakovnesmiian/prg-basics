def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    if points >= 14:
        gade = 'Good'
    if points >= 10:
        grade = 'Satisfactory'
    else: 
        grade = 'Failed'
    return grade 

test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')