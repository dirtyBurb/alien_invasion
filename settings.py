class Settings():
	"""A class to store all of the settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's static settings."""
		
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Ship Settings
		self.ship_limit = 3

		# Bullet Settings
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 5
		
		# Alien Settings
		self.fleet_drop_speed = 100

		# How quickly the game speeds up
		self.speedup_scale = 1.5
		# How quickly the alien point values increase
		self.score_scale = 1.5

		# High score should never be reset.

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = 20
		self.bullet_speed_factor = 15
		self.alien_speed_factor = 5
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Icrease speed settings."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)





