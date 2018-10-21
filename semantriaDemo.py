#!/usr/bin/python
# -*- coding: utf-8 -*-

import semantria, time, uuid, os
import scipy.io as spio

#ID to Title mapping
mat = spio.loadmat(r'movie_metadata.mat', struct_as_record=False)
data = mat['m']
idList = (data[0,0].ID).tolist()
for index, id in enumerate(idList):
    idList[index] = idList[index][0] #transform list of lists into single list of ids
titleList = (data[0,0].Title).tolist()

# API Key/Secret
# Set the environment vars before calling this program
# or edit this file and put your key and secret here.
#"8087b301-f1ae-452a-849b-cd48fb881436"
consumerKey = os.getenv('SEMANTRIA_KEY')
#a2c7b881-5e1a-4c7d-9c5e-92249962a586"#
consumerSecret = os.getenv('SEMANTRIA_SECRET')

# Initializes new session with the serializer object and the keys.
session = semantria.Session(consumerKey, consumerSecret)

subscription = session.getSubscription()

#some sample text - only one document
initialTexts = [ 
 "Set in a lonely city on a rainy night, the film takes place in a bicycle shop  that is closed for the night. In the corner of the shop sleeps Red, a red unicycle who languishes in the 'clearance corner', waiting to be purchased. As the camera zooms on him, the sound of rain falling turns into a drumroll, and we go into the dream-sequence. In his dream, Red is being ridden by a circus clown  as part of a juggling act. The clown enters the ring, accompanied by a fanfare, expecting a huge applause, but instead receives only a few scattered claps from different parts of the  audience. Nevertheless, Lumpy starts juggling three balls whilst riding Red, occasionally dropping them as he does. However, Red slides out from underneath Lumpy  and spikes the balls back to him with his bike pedals. The confused clown ponders this for only a second before continuing on with his act. At this point, Red is forced to catch another ball which Lumpy unintentionally throws across the ring. Lumpy continues to ride in the air while juggling the other two balls while Red bounces the green ball up and down. Eventually Lumpy comes to a sudden realization, and looks between his legs, only to discover he's been riding on nothing before he falls to the ground . Red catches the other two balls and begins juggling all three of them, and then balances them on top of each other, after which he receives an uproarous applause. But then the sound of clapping turns into the sound of rain, and Red awakens, left to face bleak reality. Depressed, he returns to the corner where he was previously resting, and goes back to sleep. The short ends with the final image of the neon sign for 'Eben's Bikes'.",
# "The Stooges play three sets of identical triplets, born one year apart. All nine brothers lose track of each other after World War II, unaware that they are all living in the same city. One set  is single, one  is married, and the other  is engaged. Trouble brews when the engaged set of brothers decided to celebrate at a local nightclub. Before they arrive, the unmarried set show up, followed by the fiancees of their brothers. The ladies start hugging and kissing the unsuspecting brothers. Within minutes, the wives of the married brothers show up, thinking their husbands are cheating on them. Hilarity ensues when the nightclub waiter  walks in and sees all nine brothers simultaneously.",
# "Ben Jones  and Marion 'Howdy' Lewis  are two easygoing, modern-day cowboys who make a meager living breaking wild horses. Their frequent employer is Jim Ed Love , a shrewd businessman who always gets the better of them. After they bring him a string of tamed horses and spend the winter rounding up stray cows, he talks them into taking a nondescript roan horse in lieu of some of their wages. Ben finds  that the horse is unrideable. Rather than turning it into soap or dog food, he comes up with the bright idea of taking it to a rodeo and betting other cowhands they cannot ride it, thereby doubling their earnings. Along the way, the duo stop to help two none-too-bright strippers, Mary  and Sister , with their car, which has broken down. Not knowing much about cars, they give them a ride to the nearest garage, but end up getting to know them better  and taking them along to the rodeo. Everything goes as planned; nobody is able to stay on the horse. Then the animal suddenly collapses and Ben spends all the money they've won for veterinary help—and a new stable to replace the one destroyed by the roan when he recovers. In the end, Ben and Howdy end up right back where they started, with only the roan to show for their efforts.",
# "Preetam , a struggling cartoonist, meets Anita  at a tennis match, where she is watching her favorite tennis star. Anita, a wealthy and westernized heiress is controlled by her feminist aunt, Sita Devi . Sita is suspicious of men, and cultivates her attitudes in Anita. However, to receive her fortune, her father's will decrees that Anita must marry within one month of turning 21. Sita Devi doesn't agree with this, and tries to set Anita up with a sham marriage which will soon lead to divorce, thereby giving her both freedom and a fortune. Sita hires Preetam to marry Anita, but doesn't know that the pair have already met. Preetam is kept from Anita after their marriage, but he kidnaps her and takes her to the traditional house of his brother. While at the house, Anita befriends Preetam's sister-in-law, and begins to see the merit in becoming a traditional Indian wife. Preetam is worried that he has lost Anita, and expedites their divorce by providing false, incrimiating evidence to the court. Preetam then leaves mumbai, heartbroken. Anita now recognizes her feelings for Preetam and rushes to meet him at the airport. In the end, the couple is reunited.",
# "Beth Cappadora  and her husband Pat  experience a parent's worst fear when their son Ben vanishes in a crowded hotel lobby during Beth's high school reunion. The ensuing frantic search is unsuccessful, and Beth goes through a sustained nervous breakdown. Unable to cope with her devastation, Beth unintentionally neglects her other children, Vincent ([[Jonathan Jackson  and Kerry . After nine years, the family has seemingly accepted that Ben has gone forever, when a familiar-looking boy  turns up at their house, introduces himself as Sam and offers to mow their lawn. Beth is convinced that Sam is actually her son, and begins an investigation that culminates in the discovery that Ben was kidnapped at the ill-fated high school reunion years ago, by a mentally unstable woman who was a high school classmate of Beth's. This woman brought up Ben as her own child, until she committed suicide. The attempted re-integration of Ben back into the Cappadora family produces painful results for all involved. Eventually the family decides that what's best for Ben is to return him to his adoptive father, but one night Vincent finds him playing basketball outside. Ben reveals that he remembered something from before his abduction, playing with Vincent and Vincent finding him, causing him to feel safe. Vincent, who has carried guilt for letting go of Ben at the reunion is forgiven by Ben who decides to return to living with his real family, but first plays a game of basketball with his brother with their parents secretly watching from their bedroom window.",
# "Porky Pig is trying to get on a plane to play golf. However, Daffy Duck, agent to the stars, complete with business card that flashes like a theater marquis, stops him , and does everything he can to convince him that his preteenager client 'Sleepy LaGoon' can become a star. This annoys Porky so much, as he is trying to get on his plane. Daffy spends most of the cartoon telling Porky about what his client can do, while actually performing various schticks himself, in his usual wild and frenetic way. After trying various ways to escape, Porky locks Daffy in a huge vault and takes off in a plane only to find out that the pilot of the plane is Daffy. Porky then jumps out with a parachute only to notice the parachute is again Daffy. Porky then gets chased back to his office. Finally, having stopped Daffy, Porky relents and asks to see what his client can do. 'Sleepy', a small and droopy-eyed duck who has whiled away the episode slurping a huge all-day sucker which he keeps in a banjo case, finally gets to perform. 'Sleepy' begins to sing a song  are in a strong baritone voice. He starts out well, then tries to hit a high note, and goes into a coughing fit.",
# "Kishen  has a suspicious-minded wife, Kaajal , who thinks he is always having an affair with another woman, even though he is extremely faithful to her and wouldn't dream of betraying her in any way. Prem  has the opposite situation. He is married to Pooja , who seems to be very trusting, even though he has been having several affairs with numerous gorgeous women. There is also Kishen's friend Shekhar , who accidentally falls in love with Sanjana  and marries her. Then Bobby , a call girl, enters the story. When Kishen takes pictures of Prem and his girlfriend, and threatens to send them to his wife, Prem hires Bobby to seduce Kishen. The plan is that Kishen will fall in love with her, and Prem wants to see if Kishen can hide the relationship. Then the lies start happening, as Kaajal thinks Bobby is Shekhar's wife, and Sanjana thinks Bobby is Kishen's wife. It becomes a bundle of confusion and comedy when all the various people and couples start meeting.",
# "School is out and the teenagers head for the beach. All is well until millionaire Harvey Huntington Honeywagon III  comes around, convinced that the beachgoers are so senselessly obsessed with sex that their mentality is below that of a primate – especially Honeywagon's wunderkind pet chimp Clyde, who can surf, drive, and watusi better than anyone on the beach. With the teenagers demoralized and discredited, Honeywagon plans to turn Bikini Beach into a senior citizens retirement home. Meanwhile, foppish British rocker and drag racer Peter Royce Bentley, better known as 'The Potato Bug' , has taken up residence on Bikini Beach. Annoyed by Frankie's reluctance to start their relationship towards marriage, Dee Dee becomes receptive to Potato Bug's advances. In a jealous rage, Frankie challenges The Potato Bug to a drag race, in hopes of winning Dee Dee back.",
# "The evil Lord Conqueror, head of Conqueror's Clan, is given a prophecy by Mud Buddha. It is said that if Conqueror finds two young children by the name of Wind and Cloud he will have good fortune. Mud Buddha tells Conqueror to look for him 10 years later so that he can tell the rest of Conqueror's fortune. Conqueror issues an order that every boy with a birth chart matching Wind's or Cloud's must become a disciple of the Conqueror's Clan. Both Wind and Cloud are found, and Lord Conqueror's servants murder their respective parents. Ten years pass, and Wind and Cloud are now both fully grown and highly skilled martial artists. Lord Conqueror raised them as his own children. He is angered by the disappearance of Mud Buddha and sends his men to find him. After Mud Buddha is found, he reveals that Wind and Cloud will either join or destroy Conqueror. Seeing that Wind and Cloud can lead to misfortune, Conqueror uses his daughter, Charity, to cause Wind and Cloud to fight each other. There was a love triangle involving Wind, Cloud, and Charity. Conqueror arranges a marriage with Wind and Charity. Cloud finds out and is unhappy about it. On the day of the wedding, he takes her away and Conqueror tells Wind to fight for his wife. Wind and Cloud engage in a battle and Lord Conqueror tries to kill Cloud in their duel, but killed his own daughter. This was because she tried to protect Cloud. Cloud and Wind's relationship with Lord Conqueror sours, after Cloud loses an arm to Conqueror in combat and Wind is poisoned by Conqueror's minions. Wind finds out the truth about who killed his parents and fights a fire beast which killed his father. Fortunately, Cloud is found by helpful villagers, one of whom donates his arm to replace Cloud's loss. Wind and Cloud then work together to destroy Lord Conqueror. Together, they defeat the evil warlord, finally exacting their revenge and fulfilling Mud Buddha's prophecy.",
#"Tim Kelly  and Max Ginsberg  have struck it rich by investing in copper stock. But when the stock takes a dive, they are compelled to go back into their former profession — junk dealers. They take in the destitute Mary Riley  as a boarder and she hits it off so well with them that she winds up becoming a partner in their rag & junk company. Mary falls in love with a man named Nathan Burke , the son of wealthy parents. Nathan's mother , however, disapproves of Mary. Eventually it is revealed that Mrs. Burke came from a poor background herself, and her long-ago sweetheart was Max. After this discovery, she gives the couple her blessings. The copper stock soars in value once again, so Kelly and Ginsberg are back in the money."
]

#should have an equal size list of id numbers that index directly 
#to their respective synopses - Kathy
#idNumbers = {}

documents = []
for index, text in enumerate(initialTexts):
    if len(text) > 2048: #exceeds character limit, don't process
        #del idNumbers[index]
        continue
    doc_id = str(uuid.uuid4())
    documents.append({'id': doc_id, 'text': text})
    
for text in initialTexts:
    if len(documents) <= subscription['basic_settings']['incoming_batch_limit']:
        status = session.queueBatch(documents)
        if status in [200, 202]:
            print ("{0} documents queued successfully.".format(len(documents)))
            documents = []
    
length = len(initialTexts)
results = []

while len(results) < length:
    time.sleep(0.5)
    print ("Retrieving your processed results...")
    response = session.getProcessedDocuments()
    for item in response:
        results.append(item)

#Build a python dictionary of "movieName" : "sentiment score"
movieScores = {}

#we have our results array, print them for viewing
# Print sample of analysis results. (There's lots more in there!)
#for index, data in enumerate(results):
#use index to index into our list of movieIDs
for data in results:
    #initialize counts for analysis fields
    analysis = [0.0, 0.0, 0.0, 0.0]
    # Print document sentiment score
    print("Document {0} \n\tSentiment score: {1} / Sentiment polarity: {2}".format(
        data['id'], data['sentiment_score'], data['sentiment_polarity']))
    docScore = data['sentiment_score']

    # Print document themes
    if "themes" in data:
        print("Document themes:")
        for theme in data["themes"]:
            analysis[0] += int(theme['sentiment_score'])
            print("\t {0} \n\t\t(str-score: {1}, sentiment: {2})".format(
                theme['title'].encode('ascii', 'replace'), theme['strength_score'],
                theme['sentiment_score']
            ))
        analysis[0] = analysis[0]/len(data["themes"]) #average the score

    # Print document entities
    if "entities" in data:
        print("Entities:")
        for entity in data["entities"]:
            analysis[1] += int(entity['sentiment_score'])
            print("\t {0}: {1} \n\t\t(sentiment: {2})".format(
                entity['title'].encode('ascii', 'replace'), entity['entity_type'],
                entity['sentiment_score']
            ))
        analysis[1] = analysis[1]/len(data["entities"]) #average the score

    # Print document opinions
    if "opinions" in data:
        print("Opinions:")
        for opinion in data["opinions"]:
            analysis[2] += int(opinion['sentiment_score'])
            print("\t {0}: \n\t\t(s-score: {1}, s-polarity: {2})".format(
                opinion['quotation'].encode('ascii', 'replace'), opinion['sentiment_score'],
                opinion['sentiment_polarity']
            ))
        analysis[2] = analysis[2]/len(data["opinions"]) #average the score

    # Print document topics
    if "topics" in data:
        print("Topics:")
        for topic in data["topics"]:
            analysis[3] += int(topic['sentiment_score'])
            strScore = topic.get("strscore", "None")
            print("\t {0}: \n\t\t(str-score: {1}, s-score: {2}, s-polarity: {3})".format(
                topic['title'].encode('ascii', 'replace'), strScore,
                topic['sentiment_score'], topic['sentiment_polarity']
            ))
        analysis[3] = analysis[3]/len(data["topics"]) #average the score

    #Simple algorithm - multiple docScore by a factor of (1+categoryScore) if
    #they have the same polarity, and 1/(1+categoryScore) if they have diff polarity
    for aScore in analysis:
        if docScore<0 == aScore<0 : #scores have same polarity
            docScore = docScore*(1+aScore)
        else :
            docScore = docScore*(1/(1+aScore))

    #Map movie ID number to movie title
    #get the movie ID that we split from the synopsis string
    #use that id to pass into idList.index(____)
    #this will map into titleList
    movieTitle = titleList[idList.index(data['id'])]
    movieScores[titleList] = docScore
    print("")

print("Done!")
for entry in movieScores:
    print(entry+":"+str(movieScores[entry]))

#write results to a file
f = open("database.txt", "w")
for entry in movieScores:
    f.write(entry+":"+str(movieScores[entry])+"\n")

