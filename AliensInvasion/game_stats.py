

class GameStats():

    def __init__(self, game_Settings):

        self.game_Settings = game_Settings
        self.reset_stats()
        # Starts the game in inactive mode
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.game_Settings.ship_limit
        self.score = 0





