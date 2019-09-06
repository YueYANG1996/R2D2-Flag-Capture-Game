def action(movement, Droids, speed, time):
	for move in movement:
		direction = move[1]
		droid = Droids[move[0]]
		if direction == 'east':
			droid.roll(0, 90, 0)
			droid.roll(speed, 90, time)
		elif direction == 'south':
			droid.roll(0, 180, 0)
			droid.roll(speed, 180, time)
		elif direction == 'west':
			droid.roll(0, 270, 0)
			droid.roll(speed, 270, time)
		elif direction == 'north':
			droid.roll(0, 0, 0)
			droid.roll(speed, 0, time)
		else:
			droid.animate(5)
