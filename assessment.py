class Student(object):
    """A student"""

    def __init__(self, first_name, last_name, address):
        """A student has a first and last name and an address"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """A question"""

    def __init__(self, question, correct_answer):
        """A question and a correct answer"""

        self.question = question
        self.correct_answer = correct_answer
        