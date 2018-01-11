from settings import Settings
from random import choice


class Player():
	
	def __init__(self, name='none'):
		self.option = 'none'
		self.score = 0
		self.name = name
		self.I_WON = 0
		

	def rand_choice(self, ai_settings):
		
		self.option = choice(ai_settings.options)
		
		return self.option
	
	
	def make_choice(self, ai_settings):
		
		self.option = input("Your choice: ").lower().title()
		
		if self.option not in ai_settings.options:
			print("No such option.")
			self.option = self.make_choice(options)
			
		return self.option
		
	def check_fight(self, player_choice, enemy_choice):
		
		if (player_choice == 'Paper' and enemy_choice == 'Rock') or \
		   (player_choice == 'Rock' and enemy_choice == 'Scisors') or \
		   (player_choice == 'Scisors' and enemy_choice == 'Paper'):
			   
			   self.score += 1
			   
