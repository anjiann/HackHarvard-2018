# class idTextPair(tuple):
#     def __new__(self, ID, text):
#         return tuple.__new__(idTextPair, (ID, text))
#     def getID(self, idTextPair):
#         return idTextPair.ID
#     #def getText():
#      #   return idTextPair.text
synopses = {}

def read(line):
    split = line.split('\t')
    synopses[split[0]] = split[1]

filename = "/Users/anthonycui/Documents/Coding/HackHarvard-2018/MovieSummaries/plot_summaries.txt"
with open(filename, "r") as fp:
    for line in fp:
        read(line)
