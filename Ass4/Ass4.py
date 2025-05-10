

from mrjob.job import MRJob 

class GradeCalculator(MRJob):

    def mapper(self, _, line):
        name, score = line.split(',')
        score = int(score)

        yield name, score

    def reducer(self, key, values):
        total_score = 0
        num_scores = 0
        for score in values:
            total_score += score
            num_scores += 1
        average_score = total_score / num_scores

        if average_score >= 90:
            grade = 'A'
        elif average_score >= 80:
            grade = 'B'
        elif average_score >= 70:
            grade = 'C'
        elif average_score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        yield key, grade

if __name__ == '__main__':
    GradeCalculator.run()
