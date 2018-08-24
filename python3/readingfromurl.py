#!//usr/bin/env python3
"""Fetch a list of words from a URL.

	Args:
	    url: the url of a UTF_8 text document.

	Returns:
	    A list of strings conataining the words from the document
	"""
import sys
from urllib.request import urlopen

def fetch_words(url):
	"""Fetch a list of words from a URL.

	Args:
	    url: the url of a UTF_8 text document.

	Returns:
	    A list of strings conataining the words from the document
	"""
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words


def print_words(items):
	"""print a list of words from a URL.

	Args:
	    items: list of strings.

	"""
	for item in items:
		print(item)


def main(url):
	words = fetch_words(url)
	print(words)


if __name__ == '__main__':
	main(sys.argv[1]) # 0th argument is file name in the command
