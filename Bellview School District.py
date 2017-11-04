''' updated code that i pushed through bash to my git hub account! neat!! '''


class SchoolDistrict(object):
    weights = [.1, .1, .1, .7]
    total_student = 0
    def __init__(self,name,gender,scores):
        self.name = name
        self.gender = gender
        self.scores = scores
        SchoolDistrict.total_student += 1

    def year_grade(self):
        weighted_score = self.scores[0]*self.weights[0] + self.scores[1]*self.weights[1] \
                         + self.scores[2]*self.weights[2] + self.scores[3]*self.weights[3]
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


from random import randint
def gen_scores(n):
    scores = []
    for ii in range(1,n):
     scores.append(randint(60,105))
    return scores


kid1 = SchoolDistrict('nick','male',gen_scores(5))
kid2 = SchoolDistrict('joe','male',gen_scores(5))
kid3 = SchoolDistrict('julia','male',gen_scores(5))
kid4 = SchoolDistrict('marcus','male',gen_scores(5))


print kid1.year_grade()
print kid2.year_grade()
print kid3.year_grade()
print kid4.year_grade()
