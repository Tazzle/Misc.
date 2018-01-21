import random

methinks_weasel = "METHINKS IT IS LIKE A WEASEL"
possible_letters = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

initial_generated_sentence = ''
generated_sentence = ''
for x in range (0,28):
	generated_sentence += random.choice(possible_letters)
	#used for comparison at end
	initial_generated_sentence = generated_sentence


def generate(matched_letters, generated_sentence):
	result = generated_sentence
	index_to_skip = matched_letters
	for index in range(0, 28):
		#if letter not already matched, then generate a new random letter
		if index not in index_to_skip:
			result = result[:index] + random.choice(possible_letters) + result[index+1:]		
			print generated_sentence
			print result
			print ''
	return result
		

iteration_count = 0
matched_letters = []
while len(matched_letters) < 28:
	iteration_count += 1
	list_of_tuples = zip(methinks_weasel, generated_sentence)
	for index, (x, y) in enumerate(list_of_tuples):
		if x == y and index not in matched_letters:
			matched_letters.append(index)
	if(len(matched_letters)) > 0:
		generated_sentence = generate(matched_letters, generated_sentence)
	else:
		print ""
		print "No matches in generated sentence, try again!"
		break

print ''
print("Number of iterations: " + str(iteration_count))
print("Initial: " + initial_generated_sentence)
print("Final: " + generated_sentence)



#EXAMPLE RESULTS (run as 'time python methinks.py' in Linux or UNIX to get execution time)

# Number of iterations: 144
# Initial: H BOCBBZIR GVEURBORTAVNUV FL
# Final: METHINKS IT IS LIKE A WEASEL

# real	0m0.133s
# user	0m0.040s
# sys	0m0.042s



# Number of iterations: 78
# Initial: EOWXJVGQCTCDDHOLZDWRAFCEUQPV
# Final: METHINKS IT IS LIKE A WEASEL

# real	0m0.048s
# user	0m0.026s
# sys	0m0.017s



# Number of iterations: 97
# Initial: OQIPSFCXXGORNEATRVL NEGR OHR
# Final: METHINKS IT IS LIKE A WEASEL

# real	0m0.055s
# user	0m0.031s
# sys	0m0.019s



# Number of iterations: 106
# Initial: EUOFQAIPOIDAJPEIFIMCTOIFGCCW
# Final: METHINKS IT IS LIKE A WEASEL

# real	0m0.049s
# user	0m0.027s
# sys	0m0.017s



# Number of iterations: 108
# Initial: QPYPXZCSHXNQO KHW XOEDUMWEUB
# Final: METHINKS IT IS LIKE A WEASEL

# real	0m0.049s
# user	0m0.027s
# sys	0m0.017s


