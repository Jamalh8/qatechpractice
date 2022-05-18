
class Students():
    def __init__(self, name, age, class_='Student'):
        self.name = name
        self.age = age
        self.class_ = class_

    def scores(self,test1,test2,test3):
        avg_score = (test1+test2+test3)/3
        avg_format_score = "{:.2f}".format(avg_score)
        return avg_format_score

student1 = Students("Tom", 20)
student2 = Students("Kat", 25, "Science")
student3 = Students("Gary", 45, "English")

student1_scores = student1.scores(70,45,99)
student2_scores = student2.scores(78,85,87)
student3_scores = student3.scores(45,76,29)

print(student1.name, student1.age, student1.class_, student1.scores(70,45,99))
print(student2.name, student2.age, student2.class_, student2.scores(78,85,87))
print(student3.name, student3.age, student3.class_, student3.scores(45,76,29))
print('\n')
print (f'{student1.name}, is aged {student1.age}, scored an average of {student1_scores}% on their tests.')
print (f'{student2.name}, is aged {student2.age}, scored an average of {student2_scores}% on their tests.')
print (f'{student3.name}, is aged {student3.age}, scored an average of {student3_scores}% on their tests.')