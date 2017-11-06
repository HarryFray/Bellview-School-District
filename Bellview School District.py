from random import randint

class SchoolDistrict(object):
    weights = [.1, .1, .1, .7]
    total_student = 0
    def __init__(self,name,gender,scores,sport):
        self.name = name
        self.gender = gender
        self.scores = scores
        SchoolDistrict.total_student += 1

    def year_grade(self):
        weighted_score = 0
        for weight in range(0,4):
            weighted_score += self.scores[weight]*self.weights[weight]
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
        if self.gender == 'male': pronoun = 'him'
        else: pronoun = 'her'
        return '%ss weighted average was %s giving %s a letter grade of %s'\
               %(self.name,weighted_score,pronoun,letter_grade)


''' attempting to practice with subclasses and super classes here giving this class inheritence of School District '''



def gen_scores(n):
    scores = []
    for ii in range(1,n):
     scores.append(randint(60,105))
    return scores


kid1 = SchoolDistrict('nick','male',gen_scores(5),'soccer')
kid2 = SchoolDistrict('joe','male',gen_scores(5),'football')
kid3 = SchoolDistrict('julia','female',gen_scores(5),'gymnastics')
kid4 = SchoolDistrict('marcus','male',gen_scores(5),'bowling')


print kid1.year_grade()
print kid2.year_grade()
print kid3.year_grade()
print kid4.year_grade()
