# def add_calc(number1, number2):
#     answer = number1 + number2
#     return answer

# added_number = add_calc(5,5)
# print(added_number + 20)

# Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.
# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.
# Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.
# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

def percentage(homework, assesment_score,final_exam):
    total=homework+assesment_score+final_exam
    average= float((total/175)*100)
    avg_format_float = "{:.2f}".format(average)
    return average

name = str(input('Enter student name: '))
homework = int(input('Enter homework score out of 25: '))
assesment_score = int(input('Enter assesment score out of 50: '))
final_exam = int(input('Enter final exam score out of 100: '))
average_score= float(percentage(homework,assesment_score,final_exam))
avg_format_float = "{:.2f}".format(average_score)

print(f'{name} scored a percentage of {avg_format_float}%')

def grade_score(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'

grade=average_score
grading=grade_score(grade)

print (f'{name} got an final average score of {avg_format_float}%, they achieved the following grade : {grading}')


