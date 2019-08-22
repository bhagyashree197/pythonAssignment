class NotANumberException(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return self.value

class InAppropriateNumberOfValue(Exception):
	pass

class OnlyCharactersExpression(Exception):
	pass
class NotABinaryNumberException(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return self.value