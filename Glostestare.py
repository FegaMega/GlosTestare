import random

class word:
	def __init__(self, w:str, w2:str):
		self.english = w.lower()
		self.swedish = w2.lower()

wordsWeek46 = [
	{ "English" : ["demand"], "Swedish" : ["krav"]},
	{ "English" : ["clash with"], "Swedish" : ["kollidera med"]},
	{ "English" : ["conscience"], "Swedish" : ["samvete"]},
	{ "English" : ["participate in"], "Swedish" : ["delta i"]},
	{ "English" : ["deliver"], "Swedish" : ["leverera"]},
	{ "English" : ["assign"], "Swedish" : ["tilldela"]},
	{ "English" : ["slip"], "Swedish" : ["remsa"]},
	{ "English" : ["accountant"], "Swedish" : ["revisor"]},
	{ "English" : ["adjacent"], "Swedish" : ["angränsande"]},
	{ "English" : ["sample"], "Swedish" : ["prov", "prova"]},
	{ "English" : ["attach"], "Swedish" : ["fästa"]},
	{ "English" : ["switch"], "Swedish" : ["strömbrytare"]},
	{ "English" : ["wrist"], "Swedish" : ["handled"]},
	{ "English" : ["label"], "Swedish" : ["märke", "sätta etiket på"]},
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
	{ "English" : ["survey"], "Swedish" : ["undersöka", "undersökning"]},
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

wordsWeek47 = [
	{ "English" : ["battered"], "Swedish" : ["illa tilltygad"]},
	{ "English" : ["resort to"], "Swedish" : ["ta till", "hemfalla åt"]},
	{ "English" : ["preoccupied with"], "Swedish" : ["helt upptagen av"]},
	{ "English" : ["stroll"], "Swedish" : ["promenera", "vandra"]},
	{ "English" : ["lavish"], "Swedish" : ["överdådig", "påkostad"]},
	{ "English" : ["blister"], "Swedish" : ["blåsa"]},
	{ "English" : ["tend"], "Swedish" : ["vårda", "sköta"]},
	{ "English" : ["solemn"], "Swedish" : ["högtidlig"]},
	{ "English" : ["right on target"], "Swedish" : ["rakt på sak"]},
	{ "English" : ["delicate"], "Swedish" : ["ömtålig", "känslig"]},
	{ "English" : ["mutual"], "Swedish" : ["ömsesidig"]},
	{ "English" : ["stagger"], "Swedish" : ["vackla"]},
	{ "English" : ["startle"], "Swedish" : ["skrämma", "överraska"]},
	{ "English" : ["peasant"], "Swedish" : ["boende"]},
	{ "English" : ["mountain range"], "Swedish" : ["bergskedja"]},
	{ "English" : ["humble"], "Swedish" : ["ödmjuk"]},
	{ "English" : ["hesitating"], "Swedish" : ["tvekande"]},
	{ "English" : ["wreckage"], "Swedish" : ["vrakspillor"]},
	{ "English" : ["injury"], "Swedish" : ["(kroppslig) skada"]},
	{ "English" : ["exposure"], "Swedish" : ["förfrysning"]},
	{ "English" : ["extensive"], "Swedish" : ["omfattande"]},
	{ "English" : ["corpse"], "Swedish" : ["lik"]},
	{ "English" : ["calculate"], "Swedish" : ["räkna ut"]},
	{ "English" : ["supervise"], "Swedish" : ["övervaka", "granska"]},
	{ "English" : ["select"], "Swedish" : ["välja ut"]},
	{ "English" : ["grief"], "Swedish" : ["sorg"]},
	{ "English" : ["grisly"], "Swedish" : ["gräslig", "ohygglig"]},
	{ "English" : ["limb"], "Swedish" : ["lem", "arm", "ben"]},
	{ "English" : ["encourage"], "Swedish" : ["uppmuntra"]},
	{ "English" : ["attend"], "Swedish" : ["delta i"]},
	{ "English" : ["gaze"], "Swedish" : ["blick", "stirrande"]},
	{ "English" : ["anniversary"], "Swedish" : ["årsdag"]},
	{ "English" : ["vigorous"], "Swedish" : ["kraftfull"]},
	{ "English" : ["assure"], "Swedish" : ["försäkra"]},
	{ "English" : ["worm"], "Swedish" : ["mask"]},
	{ "English" : ["communion"], "Swedish" : ["gemenskap", "nattvard"]},
	{ "English" : ["spirit"], "Swedish" : ["humör", "sinnessstämming", "energi", "gnista"]},
	{ "English" : ["sacrifice"], "Swedish" : ["offer"]},
	{ "English" : ["score"], "Swedish" : ["göra mål"]},
	{ "English" : ["estate"], "Swedish" : ["gods", "(lant)egendom"]},
]

words = [
	{ "English" : ["alter"], "Swedish" : ["ändra"]},
	{ "English" : ["gene-editing"], "Swedish" : ["redigering av gener", "förbättring av gener"]},
	{ "English" : ["the mainstream"], "Swedish" : ["det normala", "det accepterade"]},
	{ "English" : ["confined to"], "Swedish" : ["begränsad till"]},
	{ "English" : ["edit"], "Swedish" : ["redigera", "bättra på"]},
	{ "English" : ["lecture"], "Swedish" : ["föreläsning"]},
	{ "English" : ["genetic engineering"], "Swedish" : ["genetisk ingenjörskonst"]},
	{ "English" : ["tinker"], "Swedish" : ["pilla", "mixtra"]},
	{ "English" : ["reckless"], "Swedish" : ["vårdslös", "lättsinnig"]},
	{ "English" : ["genome"], "Swedish" : ["genuppsättning"]},
	{ "English" : ["tissue"], "Swedish" : ["vävnad"]},
	{ "English" : ["consensus"], "Swedish" : ["samsyn", "allmän mening"]},
	{ "English" : ["alteration"], "Swedish" : ["ändring"]},
	{ "English" : ["inhibit"], "Swedish" : ["hämma"]},
	{ "English" : ["disability"], "Swedish" : ["handikapp", "rörelsehinder", "funktionsvariation"]},
	{ "English" : ["extend"], "Swedish" : ["sträcka sig"]},
	{ "English" : ["enhance"], "Swedish" : ["stegra", "stärka", "förbättra"]},
	{ "English" : ["sense"], "Swedish" : ["sinne"]},
	{ "English" : ["limb"], "Swedish" : ["lem", "arm", "ben"]},
	{ "English" : ["competitive sport"], "Swedish" : ["tävlingssport"]},
	{ "English" : ["detect"], "Swedish" : ["upptäcka"]},
	{ "English" : ["be conflicted by"], "Swedish" : ["stå i strid med", "stå i konflikt med"]},
	{ "English" : ["monitor"], "Swedish" : ["övervaka", "kontrollera"]},
	{ "English" : ["crackdown on"], "Swedish" : ["hårdare kontroll av", "tillslag mot"]},
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

def findDifferncesStrStr(answer:str, correctAnswer: str) -> str:
	string = ""
	for i in range(correctAnswer.__len__()):
		if i < answer.__len__() and answer[i] == correctAnswer[i]:
			string += "\33[32m"
		else:
			string += "\33[31m"
		string += correctAnswer[i]
	string += "\33[0m"			
	return string

def findDifferncesStrList(answer:str, correctAnswers: list) -> str:
	string = ""
	for i in range(len(correctAnswers)-1):
		string += findDifferncesStrStr(answer, correctAnswers[i]) + ", "

	string += findDifferncesStrStr(answer, correctAnswers[len(correctAnswers)-1])
	return string

while len(words) > 0:

	i = random.randint(0, len(words)-1)
	swedishToEnglish = bool(random.randint(0, 1))
	swedishToEnglish = 1
	
	if swedishToEnglish:
		Answers = words[i]["Swedish"]

		hintWord = formatHintWord(Answers)

		answer = askForTranslation("Swedish : "+ hintWord + " ; English : ")
	
		if answer == words[i]["English"][0]:
			dif = findDifferncesStrList(answer, words[i]["English"])
			print ("Correct!")
			words.pop(i)
		else:
			dif = findDifferncesStrList(answer, words[i]["English"])
			print("Incorrect : " + dif)

	else:
		answer = input("English : " + words[i].english + " ; Swedish : ").rstrip()
		if answer.lower() == words[i].swedish.lower():
			print ("Correct")
			words.pop(i)
		else:
			print("Incorrect : "+ words[i].swedish)
