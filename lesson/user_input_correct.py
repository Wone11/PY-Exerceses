def correct_stream(user, correct):
	return [1 if user[i] == correct[i] else -1 for i in range(len(user))]

print(correct_stream(['Solomon','Soulax','Gandayiki'],['Solomon','Soulax','Gandayiki']))