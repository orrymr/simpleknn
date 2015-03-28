class Neighbour:
	def __init__(self, data, cl, dist):
		self.data = data
		self.cl = cl
		self.dist = dist


def knn(trainingData, newPoint, k):
	for data in trainingData:
		if len(data) != 2:
			raise Exception("problem, training data should be a tuple of length 2")

	nearestNeighbours = []

	for dataPoint in trainingData:
		distance = dist (dataPoint[0], newPoint)
		nearestNeighbours.append(Neighbour(dataPoint[0], dataPoint[1], distance))

	nearestNeighbours.sort(key = lambda x: x.dist)

	nearestNeighbours = nearestNeighbours[0:k]

	for point in nearestNeighbours:
		print "*********"
		print point.data
		print point.cl
		print point.dist
		print "**********"
				

def dist(one, two):
	dist = 0
	for el in zip(one, two):
		dist += (el[0] - el[1]) ** 2
	dist = dist ** 0.5
	return dist
