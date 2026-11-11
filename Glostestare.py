import random

class word:
	def __init__(self, w:str, w2:str):
		self.english = w.lower()
		self.swedish = w2.lower()

words = [
	{ "English" : ["demand"], "Swedish" : ["krav"]},
	{ "English" : ["clash with"], "Swedish" : ["kollidera med"]},
	{ "English" : ["conscience"], "Swedish" : ["samvete"]},
	{ "English" : ["participate in"], "Swedish" : ["delta i"]},
	{ "English" : ["deliver"], "Swedish" : ["leverera"]},
	{ "English" : ["assign"], "Swedish" : ["tilldela"]},
	{ "English" : ["slip"], "Swedish" : ["remsa"]},
	{ "English" : ["accountant"], "Swedish" : ["revisor"]},
	{ "English" : ["adjacent"], "Swedish" : ["angränsande"]},
	{ "English" : ["sample"], "Swedish" : ["prov / prova"]},
	{ "English" : ["attach"], "Swedish" : ["fästa"]},
	{ "English" : ["switch"], "Swedish" : ["strömbrytare"]},
	{ "English" : ["wrist"], "Swedish" : ["handled"]},
	{ "English" : ["label"], "Swedish" : ["märke, sätta etiket på"]},
	{ "English" : ["participant"], "Swedish" : ["deltagare"]},
	{ "English" : ["comply with"], "Swedish" : ["lyda"]},
	{ "English" : ["request"], "Swedish" : ["begäran"]},
	{ "English" : ["refuse"], "Swedish" : ["vägra"]},
	{ "English" : ["agony"], "Swedish" : ["vånda, stark plåga"]},
	{ "English" : ["refusal"], "Swedish" : ["vägran"]},
	{ "English" : ["inquiry"], "Swedish" : ["förfrågan"]},
	{ "English" : ["plea"], "Swedish" : ["vädjan"]},
	{ "English" : ["disobey"], "Swedish" : ["inte lyda"]},
	{ "English" : ["conduct"], "Swedish" : ["utföra"]},
	{ "English" : ["vocational"], "Swedish" : ["yrkes-"]},
	{ "English" : ["reassurance"], "Swedish" : ["försäkran"]},
	{ "English" : ["tissue"], "Swedish" : ["vävnad"]},
	{ "English" : ["obedience"], "Swedish" : ["lydnad"]},
	{ "English" : ["subject"], "Swedish" : ["försöksperson"]},
	{ "English" : ["alter"], "Swedish" : ["ändra"]},
	{ "English" : ["depict"], "Swedish" : ["skildra"]},
	{ "English" : ["penetrate"], "Swedish" : ["tränga in i"]},
	{ "English" : ["diverse"], "Swedish" : ["mångfaldig"]},
	{ "English" : ["deception"], "Swedish" : ["bedrägeri"]},
	{ "English" : ["survey"], "Swedish" : ["undersöka / undersökning"]},
	{ "English" : ["regret"], "Swedish" : ["ångra"]},
	{ "English" : ["volunteer"], "Swedish" : ["frivillig"]},
	{ "English" : ["conclude"], "Swedish" : ["komma fram till"]},
	{ "English" : ["compassion"], "Swedish" : ["medkänsla"]},
	{ "English" : ["remote"], "Swedish" : ["avlägsen"]},
	{ "English" : ["compliance"], "Swedish" : ["tillmötesgående"]},
	{ "English" : ["abuse"], "Swedish" : ["misshandla"]},
	{ "English" : ["distant"], "Swedish" : ["avlägsen"]},
	{ "English" : ["combat"], "Swedish" : ["strid"]},
	{ "English" : ["aim"], "Swedish" : ["sikta"]},
	{ "English" : ["compassionate"], "Swedish" : ["barmhärtig"]},
	{ "English" : ["appeal"], "Swedish" : ["vädjan"]},
	{ "English" : ["commitment"], "Swedish" : ["engagemang"]},
	{ "English" : ["pregnancy"], "Swedish" : ["graviditet"]},
	{ "English" : ["display"], "Swedish" : ["visa"]},
	{ "English" : ["command"], "Swedish" : ["order"]},
	{ "English" : ["legitimacy"], "Swedish" : ["legitimitet"]},
	{ "English" : ["confirm"], "Swedish" : ["bekräfta"]},
	{ "English" : ["percieve"], "Swedish" : ["uppfatta"]},
	{ "English" : ["legitimate"], "Swedish" : ["rättmätig"]},
	{ "English" : ["assume command"], "Swedish" : ["ta över befället"]},
	{ "English" : ["feign"], "Swedish" : ["låtsas"]},
	{ "English" : ["disgust"], "Swedish" : ["avsky"]},
	{ "English" : ["defiance"], "Swedish" : ["trots"]},
	{ "English" : ["unplug"], "Swedish" : ["koppla ur"]},
	{ "English" : ["liberate"], "Swedish" : ["befria"]},
	{ "English" : ["recall"], "Swedish" : ["komma ihåg"]},
	{ "English" : ["justifiable"], "Swedish" : ["rättmätig"]}, # SAME SWEDISH WORD
	{ "English" : ["offensive"], "Swedish" : ["kränkande"]},
	{ "English" : ["object"], "Swedish" : ["protestera"]},
	{ "English" : ["capture"], "Swedish" : ["fånga"]},
]



sw = []
weirdWords = []
for w in words:
	try: 
		sw.index(w["Swedish"])
		weirdWords.append(w["Swedish"])
	except:
		sw.append(w["Swedish"])

def findSwedishWordsThatAreTheSame(argWord) -> list:
	ReturnList = []
	for w in words:
		if w["Swedish"] == argWord["Swedish"] and w["English"] != argWord["English"]:
			ReturnList.append(w)
	return ReturnList

print("You have", len(words), "words to be tortured by")

# Ask for the translation of the question word, 
# returns the users answer in lowercase and without ending spaces 
def askForTranslation(question:str) -> str:
	answer = input(question).rstrip().lower()
	return answer

def findNonCorrectAnswers(correctAnswerWords, incorrectAnswerWords) -> list:
	returnList = []
	for incorrectAnswers in incorrectAnswerWords:
		for wrongAnswer in incorrectAnswers["English"]:
			if not(wrongAnswer in correctAnswerWords):
				returnList.append(wrongAnswer)
	return returnList


def formatHintWord(answers):
	ReturnWord = ""
	for answer in answers:
		ReturnWord += answer + " / "
	ReturnWord += "\b\b\b" # Remove the ending " / "


	SameTranslation = findSwedishWordsThatAreTheSame(words[i])
	if len(SameTranslation)>0: 
		ReturnWord += " (Does not start with "
		
		WordsToFilter = findNonCorrectAnswers(answers, SameTranslation)

		for word in WordsToFilter:
			ReturnWord += word[0] + ", "

		ReturnWord += "\b\b)" # Remove the ending ", " 

	return ReturnWord

def checkAnswer(answer : str, alternatives:list):
	return answer in alternatives

while len(words) > 0:

	i = random.randint(0, len(words)-1)
	swedishToEnglish = bool(random.randint(0, 1))
	swedishToEnglish = 1
	
	if swedishToEnglish:
		Answers = words[i]["Swedish"]

		hintWord = formatHintWord(Answers)

		answer = askForTranslation("Swedish : "+ hintWord + " ; English : ")
	
		if answer == words[i]["English"][0]:
			print ("Correct")
			words.pop(i)
		else:
			print("Incorrect : " + words[i]["English"][0])

	else:
		answer = input("English : " + words[i].english + " ; Swedish : ").rstrip()
		if answer.lower() == words[i].swedish.lower():
			print ("Correct")
			words.pop(i)
		else:
			print("Incorrect : "+ words[i].swedish)
