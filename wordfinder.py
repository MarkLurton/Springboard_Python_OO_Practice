"""Word Finder: finds random words from a dictionary."""
from random import randint


class WordFinder:
    """
    Finds random words from a dictionary.

    >>> wf = WordFinder('words.txt')
    235886 words read

    >>> len(wf.random()) > 0
    True

    >>> wf.random() != wf.random()
    True
    """

    def __init__(self, file):
        self.file = file
        self.words = self.findwords()
        print(f'{len(self.words)} words read')

    def findwords(self):
        """Reads words from file and adds them into a words list"""
        words = []

        with open(f'{self.file}', 'r') as wordfile:
            for line in wordfile:
                words.append(line.strip())
        
        return words

    def random(self):
        """Returns a random word from word list"""
        return self.words[randint(0,len(self.words) - 1)]

class SpecialWordFinder(WordFinder):
    """Find random word from dictionary skipping blank lines"""
    def __init__(self, file):
        super().__init__(file)
        self.words = self.findwords()

    def findwords(self):
        """Read words from file and add them into words list if they are not blank lines"""
        words = []

        with open(f'{self.file}', 'r') as wordfile:
            for line in wordfile:
                if line.strip() != '' and not line.strip().startswith('#'):
                    words.append(line.strip())
        return words
