import datetime
import random

choices = [True, False]
print(datetime.datetime.now())
if random.choice(choices):
	raise Exception('Error at %s' % datetime.datetime.now())
