class bcolors:
  HEADER = '\033[95m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'

redBold = bcolors.FAIL + bcolors.BOLD
end = bcolors.ENDC
green = bcolors.OKGREEN
pink = bcolors.HEADER
yellow = bcolors.WARNING
begin = "\n\x1b[32m=>\x1b[0m "
fail = redBold+ "\x1b[31mx\x1b[0m "
a = yellow+"(a) "+end
b = yellow+"(b) "+end
c = yellow+"(c) "+end
d = yellow+"(d) "+end

class Question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

question_prompts = [
begin + "What’s wrong with the API request if you get a 401 status code?\n"+a+"Wrong API key\n"+b+"Wrong ws user\n"+c+"Missing permissions\n"+d+"All of the above apply\n",
begin + "Submit a /payments request with card number 41111111455511420, what status and error code do you receive?\n"+a+"500 + 000\n"+b+"500 + 101\n"+c+"422 + 000\n"+d+"422 + 101\n",
begin + "If you use a non-existing psp reference in a capture request (/capture), what error code do you get?\n"+a+"167\n"+b+"906\n"+c+"15_011\n"+d+"175\n",
begin + "Which API response with http status code 422 and error code 100 is correct?\n"+a+"\n\"status\": 422,\n\"errorCode\": \"100\",\n\"message\": \"Required parameter 'amount' is not provided.\",\n\n\"errorType\": \"validation\",\n\"pspReference\": \"8816649936729799\"\n"+b+"\n\"status\": 422,\n\"errorCode\": \"100\",\n\"message\": \"Required string 'amount' is not provided.\",\n\n\"errorType\": \"validation\",\n\"pspReference\": \"8816649936729799\"\n"+c+"\n\"status\": 422,\n\"errorCode\": \"100\",\n\"message\": \"Required object 'amount' is not provided.\",\n\"errorType\": \"validation\",\n\"pspReference\": \"8816649936729799\"\n",
begin + "Submit a /payments request with a 901 error code, what status code do you receive?\n"+a+"401\n"+b+"403\n"+c+"404\n",
begin + "What do you need to do to the API request to get a 400 status code (Bad Request)?\n"+a+"Removed bracket\n"+b+"Removed comma\n"+c+"Misspelled keyword\n"+d+"All of the above apply\n",
begin + "Which psp had a HTTP 200 status code?\n"+a+"8616649935235915\n"+b+"8836649987396098\n"+c+"8636617760070844\n",
]

questions = [
Question(question_prompts[0], "d"),
Question(question_prompts[1], "d"),
Question(question_prompts[2], "a"),
Question(question_prompts[3], "c"),
Question(question_prompts[4], "b"),
Question(question_prompts[5], "d"),
Question(question_prompts[6], "b")
]

def start(questions):
	instructions()
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score += 1
			print(green + "✅ Correct!"+end)
		else:
			print(redBold+"💥 EHHH Wrong"+end)
	print("you got " + str(score) + "/" + str(len(questions)) + " correct!")
	showPassOrFail(score)




def instructions():
	print(pink + """
  /$$$$$$  /$$$$$$$  /$$$$$$                           /$$          
 /$$__  $$| $$__  $$|_  $$_/                          |__/          
| $$  \ $$| $$  \ $$  | $$          /$$$$$$  /$$   /$$ /$$ /$$$$$$$$
| $$$$$$$$| $$$$$$$/  | $$         /$$__  $$| $$  | $$| $$|____ /$$/
| $$__  $$| $$____/   | $$        | $$  \ $$| $$  | $$| $$   /$$$$/ 
| $$  | $$| $$        | $$        | $$  | $$| $$  | $$| $$  /$$__/  
| $$  | $$| $$       /$$$$$$      |  $$$$$$$|  $$$$$$/| $$ /$$$$$$$$
|__/  |__/|__/      |______/       \____  $$ \______/ |__/|________/
                                        | $$                        
                                        | $$                        
                                        |__/""" + yellow + """
HOW TO PLAY:
There's 7 questions, each question has 1 answer
Only fill in the letter when submitting your answer eg: a

You need a score of 4 to pass, good luck! ⚡️""" + end)


def showPassOrFail(score):
	if score > 4:
		print(green + """
			          .'-'.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\ /.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     . /.\ .   '
      *            *..*         :""" + end)
	else:
		print(redBold + """YOU FAIL, TRY AGAIN 💩""" + end)


start(questions)
