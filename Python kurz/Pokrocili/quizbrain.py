class QuizBrain:
    
    def __init__(self, q_list):
        self.q_num = 0
        self.score = 0
        self.question_l = q_list

    def next_question(self):
        current_question = self.question_l[self.q_num]
        self.q_num += 1
        user_answer = input(f"Otazka c. {self.q_num}: {current_question.text} (True/False): ") 
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Spravna odpoved.")
            self.score += 1
        else: print("Bohuzel spatne.")
        print(f"Spravna odpoved je {correct_answer}\nVase skore je {self.score} / {self.q_num}")
    
    def has_ques(self):
        if self.q_num < len(self.question_l):
            return True
        else: return False

        