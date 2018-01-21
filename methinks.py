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



#EXAMPLE RESULTS

# Number of iterations: 115
# Initial: MESJAOQRGKVRZUVCUQKRQIWAPGKC
# Final: METHINKS IT IS LIKE A WEASEL

# Number of iterations: 120
# Initial: NLMGQTVLYJBPH SQESJYJNW OOEI
# Final: METHINKS IT IS LIKE A WEASEL

# Number of iterations: 166
# Initial:  GTZOQPOEHUVPCQMCNZZISNWVWKR
# Final: METHINKS IT IS LIKE A WEASEL

# Number of iterations: 128
# Initial: UTAZGOGBOXABY GPMKZLBAPSFDKN
# Final: METHINKS IT IS LIKE A WEASEL

# Number of iterations: 86
# Initial: MBPLSK GBKMKPLSAMEHUUHJPUVKC
# Final: METHINKS IT IS LIKE A WEASEL





