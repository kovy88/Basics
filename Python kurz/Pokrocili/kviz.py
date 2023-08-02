from question import Question
from data import question_data
from quizbrain import QuizBrain
question_list = []

for i in question_data:
    q_text = i["question"]
    q_answer = i["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_list.append(new_q)
      
quiz = QuizBrain(question_list)
while quiz.has_ques():
    quiz.next_question()

print(f"Dokoncil jste kviz\nVase skore je {quiz.score} / {quiz.q_num}")