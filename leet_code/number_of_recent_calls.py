# 933

class RecentCounter:

	def __init__(self):
		self.recent_calls = []

	def ping(self, t: int) -> int:

		self.recent_calls.append(t)

		while True:
			if len(self.recent_calls) > 0 :
				if self.recent_calls[0] == None:
					del self.recent_calls[0]
					return None
				if t - self.recent_calls[0] > 3000:
					del self.recent_calls[0]
				else:
					return len(self.recent_calls)



if __name__ == '__main__':
	# Your RecentCounter object will be instantiated and called as such:
	obj = RecentCounter()
	times = [None, 1, 100, 3001, 3002]
	# t = 2

	for t in times:
		param_1 = obj.ping(t)
		print(f't: {t} - {param_1}')