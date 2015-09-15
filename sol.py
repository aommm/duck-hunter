import json

# Load data
file  = open('data.json', 'r')
words = json.load(file)['quiz']
# Sort, so as to put equal words next to eachother
words.sort() 

for i in range(0, len(words),2):
	# If word does not have identical neighbour, it's all alone
	if (words[i] != words[i+1]):
		print("odd duck: %s" % words[i])
		break
