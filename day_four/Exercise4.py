class Bucket:
	name = str()
	max_volume = float()
	current_volume = float()

	def __init__(self, name, max_volume, current_volume):
		self.name = name
		self.max_volume = max_volume
		self.current_volume = current_volume

	def getBucket(self):
		return self.name

	def getMaxVolume(self):
		return self.max_volume

	def getCurrentVolume(self):
		return self.current_volume

	def setCurrentVolume(self, new_volume):
		self.current_volume = new_volume

	def transfer(self, second_bucket):
		difference = self.max_volume - self.current_volume

		if second_bucket.getCurrentVolume() > difference:
			#Add as much as the current bucket can hold
			self.current_volume = self.current_volume + difference
			second_bucket.setCurrentVolume( second_bucket.getCurrentVolume() - difference )

		else:
			#Add the entier contents of bucket2 to the current bucket
			self.current_volume = self.current_volume + second_bucket.getCurrentVolume()
			second_bucket.setCurrentVolume(0.0)

bucket1 = Bucket("Home Depot Pail", 20, 5.1)

bucket2 = Bucket("bucket", 5, 2.5)

print(bucket1.getCurrentVolume())
print(bucket2.getCurrentVolume())

bucket2.transfer(bucket1)

print(bucket1.getCurrentVolume())
print(bucket2.getCurrentVolume())