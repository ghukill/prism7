# python and shit




class Row(object):

	def __init__(self,id,d):

		# convert
		d = str(d)

		self.id = id
		self.d = d

		# d_1_1
		self.d1 = list(d[:len(d)/2])
		self.d2 = list(d[len(d)/2:])

		self.prism7 = [
			self.d1+self.d2,
			self.d2[::-1]+self.d1[::-1],
			self.d2[::-1][::-1]+self.d1[::-1][::-1],
			self.d1+self.d2,
			self.d2[::-1][::-1]+self.d1[::-1][::-1],
			self.d2[::-1]+self.d1[::-1],
			self.d1+self.d2
		]