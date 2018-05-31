#Creator:Cory Richard
#Date Updated:3/16/2018
"""
I made this quiz to review topics learned about programming in 
Python from Udacity's Intro to Programming Course. 

"""
import random

textBlanksRemaining= '''
======================================================================
The following blanks remain:
======================================================================'''
textQuizIntro= """Good luck on this quiz... I must warn you, just in case 
you are the kind of person that value's his/her mental sanity....
This quiz is harder than an undergraduate Thermodynamics Final, so take it at your own risk :)
I made it to practice some concepts from the Udacity Intro to Programming Course"""

easy_quiz="""__1__ is an __2__ programming language created by the Benevolent Dictator for Life, 
Guido van Rossum in the early 1990s. __2__ means the source code is translated into 
machine language instructions for the computer to execute. When learning a new programming language, 
it is popular for one of the first commands to be executed to be a simple:
__3__ "__4__ world!"
Which produces a line of text. Although not particularly useful in and of itself, 
it demonstrates generating __5__ to the user, which is a valuabe concept in general. 
Another useful tool is using __6__ to store integers and strings among other things. 
For example, typing:
x="__4__ World"
and then entering the command:
__3__ x
In __1__ will produce the same output as:
__3__ "__4__ World"
Using __6__ will undoubtedly become more exciting and challenging as programs become
more complex!
	"""

medium_quiz="""You can create a __1__ in Python by using the keyword __2__ followed by parentheses.
The __3__ aka parameters are placed between the parentheses
and the parentheses are followed by a __4__. The __3__ between parentheses are also __5__. 
A __1__ can also be defined without any __3__ required at all.

A __1__ is normally used to __6__ an object. A function's __6__ is specified by the __7__ keyword.
Whether on accident or by design, when an output is not specified, a __1__ will return __8__ by default.

An __6__ can be a string integer, list, tuple, or  adictionary to name a few. 
More on these data types will be tested in the hard version of the quiz."""

hard_quiz="""In python, some objects are __1__ or changeable, and other objects are __2__, or unchangeable. 
However, it is possible to break this seemingly straight-forward rule; in order to change an __2__ object,
a new object has to be created in memory and then reassigned to the variable that needs tobe changed. 
Due to this design, it is better to use a __1__ object when it is possible that the value will need to be changed
throughout the programs, as using an __2__ will require morememory to run. 
Some of the __1__ objects are lists and dictionaries. __2__ objects are strings, tuples, and integers.

To create a list, you should place the comma separated values between square __3__. To create a tuple, 
the same comma separated values should be placed between a pair of __4__. You can then __5__ the values in a list
and a tuple by using the variable assigned and sqaure __3__.
Other methods used to __5__ include __6__ and __7__ loops. The __6__ is particularly useful 
when you need to iterate over every element of a list or tuple from state t finish,
whereas __7__ is useful when a condition needs to occur for the loop to break. 
Usually, these loops are __8__, but they do have different impacts on the resources a program requires to run. """
	
easy_answers=['Python', 'interpreted', 'print', 'Hello','output','variables']
medium_answers=['function','def','arguments','colon','inputs','output','return','None']
hard_answers=['mutable','immutable','brackets','parentheses','index','for','while','interchangeable']

# no input needed, will prompt user to select diffulty and setup the game
#outputs [quiz,[answers]]! 
def level_selector():
	"""
	Inputs: 
		None
	Behavior:
		Selects the level for the quiz
	Output:
		List of [quiz, [answers]]
	"""
	print 'Select a difficulty by entering easy, medium, or hard'
	while True:
		user_input = raw_input("Select difficulty: ")
		if user_input=='easy':
			print 'You have chosen '+user_input+'!!!!!'
			return [easy_quiz,easy_answers]
		elif user_input=='medium':
			print 'You have chosen '+user_input+'!!!!!'
			return [medium_quiz,medium_answers]
		elif user_input=='hard':
			print 'You have chosen '+user_input+'!!!!!'
			return [hard_quiz,hard_answers]
		else:
			print """Invalid input. Try again sir/ma'am."""

def printAndShuffleAnswers(currentQuestion,answers):
	"""
	Inputs:
		currentQuestion:The index of the blank being answered
		answers: The list of answers for the quiz
	Behavior:
		Randomly huffles the answers list, starting at current question, and returns the randomized list
	Output:
		A shuffled list of remaining answers
	"""
	print 'The following words are options:'
	shuffled_answers=answers[currentQuestion:]
	random.shuffle(shuffled_answers)
	for word in shuffled_answers:
		print word

def quizLogicGuess( question, answers, blank, quiz):
	"""
	Inputs:
		question: Index value of blank being answered
		answers: list of answers for quiz
		blank: current blank from blank the blank list
		quiz: quiz selected
	Behavior:
		This makes the user take a set of guesses for the question
	Output:
		Returns the updated quiz, returns -1 if user runs out of guesses
	"""
	guesses=0
	maxAttempts=5
	while True:
			print 'You have '+str(maxAttempts-guesses)+' attempt(s) remaining'
			user_input=raw_input('What should be substituted for '+blank+'? Your guess: ')
			if guesses==maxAttempts-1:
				print'Thanks for trying! Press Enter to close window'
				return -1
			elif user_input==answers[question]:
				quiz=quiz.replace(blank,answers[question])
				return quiz
			else:
				guesses+=1


def quizLogic(quiz, answers, blank_list):
	"""
	Inputs:
		quiz: quiz selected
		answers: list of answers for quiz
		blank_list: list of blanks for the quiz
	Behavior:
		Processes the quiz
	Output:
		Returns either completed quiz or -1 if user ran out of attempts
	"""
	outOfGuesses=-1
	question=0
	for blank in blank_list:
		printAndShuffleAnswers(question,answers)
		quiz=quizLogicGuess(question,answers,blank, quiz)
		if quiz==outOfGuesses:
			break
		question+=1
		print textBlanksRemaining
		print quiz
	return quiz

def blanks_generator(answers):
	"""
	Inputs:
		answers: list of answers for quiz
	Behavior:
		Generates a list of blanks for each answer
	Output:
		Returns a list of blanks
	"""
	count=0
	blank_list=[]
	for value in answers:
		count+=1
		blank="__"+str(count)+"__"
		blank_list.append(blank)
	return blank_list

def quiz():
	"""
	Inputs: 
		None
	Behavior:
		Initiates the quiz
	Output:
		Text to user
	"""
	levelSelectorQuiz=0
	levelSelectorAnswers=1
	print textQuizIntro  	
	print 'You will get 5 attempts per question'
	quizAndAnswers=level_selector()
	quiz=quizAndAnswers[levelSelectorQuiz]
	answers=quizAndAnswers[levelSelectorAnswers]
	blank_list=blanks_generator(answers) #generate list of blanks
	print quiz
	quiz=quizLogic(quiz,answers,blank_list)
	if quiz==-1:
		print'Thanks for trying! Press Enter to close window'
		raw_input()
	else:
		print 'Good Job!! Press Enter to exit'
		raw_input()

print quiz()