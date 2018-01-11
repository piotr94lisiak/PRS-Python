from player import Player
from settings import Settings
import game_function as gf
import time

ai_settings = Settings()

player = Player(name = 'Peter')
npc = Player(name = 'NPC')

while ai_settings.game_status == 1:
	
	gf.run_game(ai_settings, player, npc)
	
gf.who_won(player, npc)
time.sleep(5)

