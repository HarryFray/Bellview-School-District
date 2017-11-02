

class SchoolDistrict(object):
    weights = [.2, .2, .2, .4]
    total_student = 0
    ''' initializes name, grades, gender and name to be used in the following methods and future nested classes '''
    def __init__(self,name,gender,qgrade1,qgrade2,qgrade3,final):
        self.name = name
        self.gender = gender
        self.qgrade1 = qgrade1
        self.qgrade2 = qgrade2
        self.qgrade3 = qgrade3
        self.final = final
        SchoolDistrict.total_student += 1
''' inputs are grades outputs the weighted averages of the students as well as there letter grade the weight is a class variable found 
above future code will allow for a non specific number of grades to be inputed...quizes homework extra credit ect. '''
    def year_grade(self):
        weighted_score = self.qgrade1*self.weights[0] + self.qgrade2*self.weights[1] \
                         + self.qgrade3*self.weights[2] + self.final*self.weights[3]
        for weight in self.weights:
            if weighted_score >= 90:
                letter_grade = 'A'
            elif weighted_score >= 80:
                letter_grade = 'B'
            elif weighted_score >= 70:
                letter_grade = 'C'
            elif weighted_score >= 60:
                letter_grade = 'D'
            else:
                letter_grade = 'F'
        return '%ss weighted average was %s giving him a letter grade of %s' %(self.name,weighted_score,letter_grade)

class HighSchool(SchoolDistrict):
    def __init__(self):
        pass


''' future code will pull random test scores based on random int, this will come from a seperate file '''
# import randint from random
kid1 = SchoolDistrict('nick','male',54,90,55,100)
kid2 = SchoolDistrict('joe','male',70,90,100,100)
kid3 = SchoolDistrict('julia','male',60,30,23,80)
kid4 = SchoolDistrict('marcus','male',2,100,55,100)


print kid1.year_grade()
print kid2.year_grade()
print kid3.year_grade()
print kid4.year_grade()
