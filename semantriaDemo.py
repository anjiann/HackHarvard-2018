import semantria, time, uuid, os

# API Key/Secret
# Set the environment vars before calling this program
# or edit this file and put your key and secret here.
consumerKey = os.getenv('SEMANTRIA_KEY')
consumerSecret = os.getenv('SEMANTRIA_SECRET')

# Initializes new session with the serializer object and the keys.
session = semantria.Session(consumerKey, consumerSecret)

subscription = session.getSubscription()

#some sample text - only one document
initialTexts = [ "Poovalli Induchoodan  is sentenced for six years prison life for murdering his classmate. Induchoodan, the only son of Justice Maranchery Karunakara Menon  was framed in the case by Manapally Madhavan Nambiar  and his crony DYSP Sankaranarayanan  to take revenge on idealist judge Menon who had earlier given jail sentence to Manapally in a corruption case. Induchoodan, who had achieved top rank in Indian Civil Service loses the post and Manapally Sudheeran ([[Saikumar  enters the list of civil service trainees. We learn in flashback that it was Ramakrishnan  the son of Moopil Nair , who had actually killed his classmate. Six years passes by and Manapally Madhavan Nambiar, now a former state minister, is dead and Induchoodan, who is all rage at the gross injustice meted out to him - thus destroying his promising life, is released from prison. Induchoodan thwarts Manapally Pavithran  from performing the funeral rituals of Nambiar at Bharathapuzha. Many confrontations between Induchoodan and Manapally's henchmen follow. Induchoodan also falls in love with Anuradha ([[Aishwarya , the strong-willed and independent-minded daughter of Mooppil Nair. Justice Menon and his wife returns back to Kerala to stay with Induchoodan. There is an appearance of a girl named Indulekha ([[Kanaka , who claims to be the daughter of Justice Menon. Menon flatly refuses the claim and banishes her. Forced by circumstances and at the instigation and help of Manapally Pavithran, she reluctantly come out open with the claim. Induchoodan at first thrashes the protesters. But upon knowing the truth from Chandrabhanu his uncle, he accepts the task of her protection in the capacity as elder brother. Induchoodan decides to marry off Indulekha to his good friend Jayakrishnan . Induchoodan has a confrontation with his father and prods him to accept mistake and acknowledge the parentage of Indulekha. Menon ultimately regrets and goes on to confess to his daughter." ]

documents = []
for text in initialTexts:
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

#we have our results array, print them for viewing
# Print sample of analysis results. (There's lots more in there!)
for data in results:
    # Print document sentiment score
    print("Document {0} / Sentiment score: {1}".format(
        data['id'], data['sentiment_score']))

    # Print document themes
    if "themes" in data:
        print("Document themes:")
        for theme in data["themes"]:
            print("\t {0} (sentiment: {1})".format(
                theme['title'].encode('ascii', 'replace'), theme['sentiment_score']))

    # Print document entities
    if "entities" in data:
        print("Entities:")
        for entity in data["entities"]:
            print("\t {0}: {1} (sentiment: {2})".format(
                entity['title'].encode('ascii', 'replace'), entity['entity_type'],
                entity['sentiment_score']
            ))

    print("")

print("Done!")