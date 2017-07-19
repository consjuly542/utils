from Article import Article
from Question import Question
#year, month, day
from datetime import date

class ArticleStatistics (object):
	"""
	Class for Law Statistics
	"""
	def __init__(self, official_article):
		#official law name - instance of class 
		self.official_article = official_article
		#points from link with frequency: 
		#dictionary: {point_num:frequency}
		self.parts_statistics = {}
		self.questions_cnt = 0
		self.sum_answers_cnt = 0
		self.cur_mean_answers = 0
		self.questions = []
		self.dates = []
		self.first_date = None
		self.last_date = None
		#название кодекса
		self.code = self.official_article.law.lower() \
			if self.official_article.law.lower().find(u'кодекс') != -1 else None

	def add_question(question):
		if question.part_num:
			if question.part_num not in self.parts_statistics:
				self.parts_statistics[question.part_num] = 0
			self.parts_statistics[question.part_num] +=1

		self.questions_cnt += 1
		self.sum_answers_cnt += len(question.answers)

		self.cur_mean_answers = float(self.sum_answers_cnt) / self.questions_cnt

		self.question.append(Question)

		q_date = date(int(question.date[:4]), \
					 int(question.date[5:7]), \
					 int(question.date[8:10]))
		self.date.append(q_date)

		if (self.first_date and self.first_date > q_date) or (self.first_date is None):
			self.first_date = q_date
		if (self.last_date and self.last_date < q_date) or (self.last_date is None):
			self.last_date = q_date




