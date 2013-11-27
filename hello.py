import sys

def main():
	username = sys.argv[1]
	vowels = ["a", "e", "i", "o", "u"]
	print "username", username
	print "has " + str(len(username)) + " characters"
	print "username starts with the letter " + username[0] + " "
	print "and ends with the letter " + username[len(username) - 1]


if __name__ == '__main__':
	main()