import scipy.io as spio
mat = spio.loadmat(r'movie_metadata.mat', struct_as_record=False)
data = mat['m']
#print(data[0,0].Title)
#ID, title, year, length, language, genre 
idList = (data[0,0].ID).tolist() #list of lists
#list of strings, all prefixed with "u'"
titleList = (data[0,0].Title).tolist()

print idList[0:5]
print titleList[0:5]
