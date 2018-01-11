from player import Player
from settings import Settings

def run_game(ai_settings, player, npc):
	
	player.option = player.make_choice(ai_settings)
	npc.option = npc.rand_choice(ai_settings)
	print('')
	print(player.name + " chose: " + player.option)
	print(npc.name + " chose: " + npc.option)
	print('')

	player.check_fight(player.option, npc.option)
	npc.check_fight(npc.option, player.option)
				
	print(player.name + " score: " + str(player.score))
	print(npc.name + " score: " + str(npc.score))
	print('')
	
	check_win(ai_settings, player)
	check_win(ai_settings, npc)
	

def check_win(ai_settings, player):
		
	if player.score == ai_settings.winning_score:
		player.I_WON = 1
		ai_settings.game_status = 0
		
def who_won(player, npc):
	if player.I_WON == 1:
		print(player.name + " won.")
	elif npc.I_WON == 1:
		print(npc.name + " won.")
	else:
		print("Something went wrong. No winner")
