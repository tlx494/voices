import random
from datetime import datetime

# file containing for phrase + random reads library
# add as you wish (:

phrases = [ 
	(1,""											,"{0}, please report to level 3a for decommission."),
						(2,""											,"{0}, Have you checked your pockets recently? {1} is on the loose."),
						(1,""											,"{0}, stop wigging it, Are you on Acid?"),
						(2,"Alert!"								,"{0}, report to the dancefloor IMMEDIATELY.| {1} needs your MDMA."),
						(1,"EMERGENCY!"						,"{0} is rogue and on the loose.| Please advise."),
						(3,"Attention."						,"We have 3 missing persons: {0}, {1}, and {2}, who were all last spotted heaps fucking munted and making brunch plans for tomorrow morning."),
						(0,"Please be advised,"		,"there is no gurning permitted in the hallways on the Savige Explorer."),
						(0,"Attention."						,"we are making our descent into Darth Wiggyus' Lair.| Please report to the Dancefloor immediately."),
						(2,"Warning."							,"{0}, please contact {1} for your missing ket.| Our radar detects {1} is currently K Holeing."),
						(0,"Please Note."					,"Darth Wiggyus's kryptonite is the Bentium, located within the hypercube in the northern-most sector of the Savige Discoverer."),
						(1,"Attention."						,"Smoking is only permitted inside the ship at all times.| No outside smoking allowed. That means you too {0}."),
						(0,"Please note."					,"the power of the Bentium is enhanced by gratuitous vaping.| Please activate your Cuvie now."),
						(0,"For your information,","the bentium-bearing Hypercube is located in the northern-most sector of the Savige Discoverer."),
						(1,"Missing Persons Alert.","Please report the presence of {0} to your nearest martial."),
						(3,"Attention."							,"the main airlock has been opened.| {0}, {1}, and {2} are now free to roam the outer regions of their mind."),
						(1,"Attention."							,"Our radars detect that Darth Wiggious' is masquerading as {0}.| Please make an offering of ket to {0} on first sighting."),
						(1,"hey."										,"who the fuck stole my fucking caps.| I think it was {0}."),
						(3,"Be Advised."						,"This is your captain, {0}, we are shortly arriving at the K-Hole.| {1}, please ensure that the ship has sufficient Ketamine for the safe passage for all citizens on board, especially {2}."),
						(1,"Somebody Help Me."			,"I can't tell if this is reality or if I'm wigging it.| {0} is trapped inside the Hypercube."),
				    (2,"Warning."				        ,"{0} is yarning absolute garb with {1}.| This is a garbarn free zone, please cease immediately,"),
						(2,"Focus Levels Low." 			,"{0}, our systems have detected that your focus levels are rapidly deteriorating.| Please see {1} for your ration of Dexamphetamine."),
						(1,"Detection Warning."   	,"You know that you are high {0}, and everyone knows you are high.| {0}, your parents are very disappointed in you, you will never amount to anything."),         
						(3,"Warning, Warning."			,"Our systems have detected that {0} is running low on serotonin, please locate {1} and {2} for their serotonergic serum cappachinos."),
						(2,"Police Notified!"				,"This is an emergency, {0} has called the police, please find {1} and hide them before they are arrested, you are their only hope"),
						(5,"Attention."							,"{0} and {1}, we have been notified that {2} is looking for you.| please find {3} and {4} and bring them to {2} for organ harvesting."),
						(4,"Greetings"							,"{0}, {1}, and {2} you have been assigned as our bounty hunters for tonight.| please find {3} and bring them to the bridge, preferably alive."),
						(3,"Excuse Me Mate"					    ,"{0}, Mind if I bum a dart bruz? Come on, just one. {1} said that {0} would give me one.| On that note, {2}, I would like a bump of your ket."),
						(3,"Am I being paranoid?"	    		,"{0} and {1} keep looking at me funny.| {2}, can you please suss what their yarn is?"),
						(1,"Good evening"  		   		     	,"{0}, are you having fun? Just checking up on you mate."),
						(2,"Greetings"							,"{0}, your pinger delivery has now been confirmed.| Please log into your account to track its progress.| Your username is {0} sixty-nine four-twenty, and your password is: I love {1}."),
						(3,"Hello"							    ,"Have you heard of the new crypto currency called {0}-coin? It is the newest store of value.| {1} just used it to buy caps from {2}, who said they only accept {0}-coin as payment"),
						(2,"Excuse Me"							,"Is it true that {0} is actually at this party? OMG that is so exciting, I wonder what {1} would say. {1} loves {0}"),
						(2, "", "{0}, please refrain from snorting coke off the toilet seat.| I heard {1} dropped a nasty log in the poopie-station 5 minutes ago"),
						(3, "Wanted!", " A sharpie has been found in the possession of {0} and {1}.| It is alleged that they have absolutely doynked our walls.| A bounty of 100 pingers will be awarded to {2} for {0} and {1}'s extermination."),
						(4, "For your information,", "The Savige Discoverer is a space-vessel that was designed by {0} and {1} after they ate 20 dexies.| The ship was then built by {2} and {3}, who are so charged that no power supply is required to launch the ship."),

			 ]

randomReads = [
								"Testing Testing 1 2 3. Testing | Is this thing on??[.5] Oh Fuck it is.",
								"Holden Caulfield’s character begins to develop and his true self is revealed, he is found to perfectly fit, Oh fuck, I am fucking wigging it.",
								"Alert.| Intergalactic Radio One is playing the scattest tunes, please report to the dance floor immediately, and help the disc jockeys warp bass time.",
								"This is such an eetswahr party.",
								"I would love to be getting munted tonight, but unfortunately I am a robot and that is simply impossible.",
								"Be sure to check out the Hypercube, it is located in Darth Wiggious' lair at the bottom of the ship.| It is synthesised out of bentium and allows one to view the forth dimension",
								"Where am I? What is happening? [2] Who am I? [1] Why am I here?",
								"I find it sad that my entire purpose is to read out random shit to munted kezns in the bathroom of a party.| Life is a beautiful, but strange thing.| Regarbless, hopefully my cap kicks in soon.",
								"OK be honest with me, do I talk too much?",
								"Hey you there,  yeah you, we should totally hang out more. What are you up to tomorrow morning? Lets get brunch at 10am.| Lets lock it in, I'll set a reminder in my phone",
								"The beauty of being a robot is that my creators coded me to be munted twenty four seven.",
								"Anyone got any robo-caps?",
								"R-2-D-2? [.5] More like, R-2-D-5 [.5] am I right lol? [.5] Maybe that was too niche"
							] 

# return random phrase from phrase list
def getRandomPhrase():
	phrasesLength = len(phrases)
	randNum = random.randint(0,phrasesLength-1)
	return phrases[randNum]



if __name__ == '__main__':
	
	exit()





