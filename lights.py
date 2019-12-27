# lights.py
class Lights(object):
	def cycleLights(self):
		t = threading.currentThread()
		head  = 0               # Index of first 'on' pixel
		tail  = -10             # Index of last 'off' pixel
		color = 0xFF0000        # 'On' color (starts red)

		while getattr(t, "do_run", True):
			self.strip.setPixelColor(head, color) # Turn on 'head' pixel
			self.strip.setPixelColor(tail, 0)     # Turn off 'tail'
			self.strip.show()                     # Refresh strip
			time.sleep(1.0 / 50)             # Pause 20 milliseconds (~50 fps)

			head += 1                        # Advance head position
			if(head >= self.numpixels):           # Off end of strip?
				head    = 0              # Reset to start
				color >>= 8              # Red->green->blue->black
				if(color == 0): color = 0xFF0000 # If black, reset to red

			tail += 1                        # Advance tail position
			if(tail >= self.numpixels): tail = 0  # Off end? Reset

	def lightsEndingSequence(self):
		# make lights green
		for i in range(0, self.numpixels):
			self.strip.setPixelColor(i, 0xFF0000)
		self.strip.show()

		time.sleep(5)

		# turn lights off
		for i in range(0, self.numpixels):
			self.strip.setPixelColor(i, 0)
		self.strip.show() 