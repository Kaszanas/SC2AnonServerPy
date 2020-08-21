import sc2reader
from PACAnalyzer.pacanalyzer import PACAnalyzer
import pickle



infile_0 = open('./DEMOS/Output/11506437_1566325283_230842.pickle','rb')
messages_0 = pickle.load(infile_0)
print(messages_0)

for event in messages_0.events:
    print(event)