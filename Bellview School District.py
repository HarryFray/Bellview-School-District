class SchoolDistrict(object):
    weights = [.2, .2, .2, .4]
    total_student = 0
    def __init__(self,name,gender,qgrade1,qgrade2,qgrade3,final):
        self.name = name
        self.gender = gender
        self.qgrade1 = qgrade1
        self.qgrade2 = qgrade2
        self.qgrade3 = qgrade3
        self.final = final
        SchoolDistrict.total_student += 1

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



# import randint from random
kid1 = SchoolDistrict('nick','male',54,90,55,100)
kid2 = SchoolDistrict('joe','male',70,90,100,100)
kid3 = SchoolDistrict('julia','male',60,30,23,80)
kid4 = SchoolDistrict('marcus','male',2,100,55,100)


print kid1.year_grade()
print kid2.year_grade()
print kid3.year_grade()
print kid4.year_grade()