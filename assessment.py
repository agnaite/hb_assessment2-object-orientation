class Student(object):
    """A student"""

    def __init__(self, first_name, last_name, address):
        """A student has a first and last name and an address"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.score = None

    def get_score(self, exam):
        """Returns a percentage score for the exam passed in"""

        if self.score is not None:
            return "{} scored: {:.2f}%.".format(self.first_name,
                                           (float(self.score)/len(exam.questions)) * 100)
        else:
            return "{} has not taken any exams.".format(self.first_name)

class Question(object):
    """A question"""

    def __init__(self, question, correct_answer):
        """A question and a correct answer"""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Prints question, accepts an answer and returns true or false"""

        answer = raw_input(self.question + " > ")
        return self.correct_answer == answer


class Exam(object):
    """An exam"""

    def __init__(self, name):
        """An exam that takes a name and has a list of questions"""

        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        """Makes a Question and adds it to the questions list"""

        question = Question(question, answer)
        self.questions.append(question)

    def administer(self):
        """Adminsters all the exam questions and returns the user's score"""

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return score


def take_test(exam, student):
    """Takes adminsters an exam to a student"""

    student.score = exam.administer()

    return student.score

def example():
    """Creates a student and exam"""

    exam = Exam('German II')

    exam.add_question("Translate: 'Let's go swimming'", "Gehen wir schwimmen")
    exam.add_question("Translate: 'What time is it?", "Wie viel Uhr ist es?")
    exam.add_question("Translate: 'What's for dinner?'", "Was gibst zum Abendbrot?")

    student = Student("Joanna", "Schmidt", "345 Florida Dr")

    take_test(exam, student)
    print student.get_score(exam)
