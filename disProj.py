import pandas as pd
import numpy as np
import csv
import requests 
import nltk
import matplotlib.pyplot as plt
import plotly.express as px
import networkx as nx
from bs4 import BeautifulSoup
from textblob import TextBlob
from collections import Counter
from nltk.corpus import brown
import random
import plotly.graph_objects as go

def createString(document_Fast, section):
    text = ''
    for tag in document_Fast.select(f'div[class^={section}]'):
        t = tag.get_text(strip = True, separator='\n')
        if t: 
            text = t + text
    return text



def listNouns(text):
    tokenized = nltk.word_tokenize(text)
    is_noun = lambda pos: pos[:2] == 'NN'
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    return nouns 

def listAdjectives(text):
    tokenized = nltk.word_tokenize(text)
    
    is_adj = lambda pos: pos[:2] == 'JJ'
    adjectives = [word for (word, pos) in nltk.pos_tag(tokenized) if is_adj(pos)]
    return adjectives
 
def listVerbs(text):
    tokenized = nltk.word_tokenize(text)
    is_verb = lambda pos: pos[:2] == 'VB'
    verb = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)]
    return verb

Fast_Webpage_1 = requests.get("http://nu.edu.pk/Student/Conduct")
Fast_Webpage_2 = requests.get("http://nu.edu.pk/University/History")
Fast_Webpage_3 = requests.get("http://nu.edu.pk/vision-and-mission")
Fast_Webpage_4 = requests.get("http://nu.edu.pk/Oric")
Fast_Webpage_5 = requests.get("http://nu.edu.pk/QEC")



Air_Webpage_1 = requests.get("https://au.edu.pk/Pages/About/Vision_Mission.aspx")
Air_Webpage_2 = requests.get("https://au.edu.pk/Pages/Faculties/DASSS/Departments/AerospaceSciences/dept_aerospace_about.aspx")
Air_Webpage_3 = requests.get("https://au.edu.pk/Pages/Faculties/IAA/iaa.aspx")
Air_Webpage_4 = requests.get("https://au.edu.pk/Pages/Research/computing.aspx")
Air_Webpage_5 = requests.get("https://au.edu.pk/Pages/ORIC/oric_home.aspx")


Comsat_webpage_1 = requests.get("https://www.lcwu.edu.pk/about/history-excellence.html")
Comsat_webpage_2 = requests.get("https://www.lcwu.edu.pk/lcwu-code-conduct.html")
Comsat_webpage_3 = requests.get("https://www.lcwu.edu.pk/about/vision-mission.html")
Comsat_webpage_4 = requests.get("https://www.lcwu.edu.pk/research/lcwu-research.html")
Comsat_webpage_5 = requests.get("https://www.lcwu.edu.pk/academics/lcwu-faculties/lcwu-fst.html")

html_string_Fast1 = Fast_Webpage_1.text
html_string_Fast2 = Fast_Webpage_2.text
html_string_Fast3 = Fast_Webpage_3.text
html_string_Fast4 = Fast_Webpage_4.text
html_string_Fast5 = Fast_Webpage_5.text

html_string_Air1 = Air_Webpage_1.text
html_string_Air2 = Air_Webpage_2.text
html_string_Air3 = Air_Webpage_3.text
html_string_Air4 = Air_Webpage_4.text
html_string_Air5 = Air_Webpage_5.text

html_string_Comsat1 = Comsat_webpage_1.text
html_string_Comsat2 = Comsat_webpage_2.text
html_string_Comsat3 = Comsat_webpage_3.text
html_string_Comsat4 = Comsat_webpage_4.text
html_string_Comsat5 = Comsat_webpage_5.text

document_Fast1 = BeautifulSoup(html_string_Fast1, "html.parser")
document_Fast2 = BeautifulSoup(html_string_Fast2, "html.parser")
document_Fast3 = BeautifulSoup(html_string_Fast3, "html.parser")
document_Fast4 = BeautifulSoup(html_string_Fast4, "html.parser")
document_Fast5 = BeautifulSoup(html_string_Fast5, "html.parser")

document_Air1 = BeautifulSoup(html_string_Air1, "html.parser")
document_Air2 = BeautifulSoup(html_string_Air2,"html.parser")
document_Air3 = BeautifulSoup(html_string_Air3, "html.parser")
document_Air4 = BeautifulSoup(html_string_Air4, "html.parser")
document_Air5 = BeautifulSoup(html_string_Air5, "html.parser")

document_Comsat1 = BeautifulSoup(html_string_Comsat1, "html.parser")
document_Comsat2 = BeautifulSoup(html_string_Comsat2,"html.parser")
document_Comsat3 = BeautifulSoup(html_string_Comsat3, "html.parser")
document_Comsat4 = BeautifulSoup(html_string_Comsat4, "html.parser")
document_Comsat5 = BeautifulSoup(html_string_Comsat5, "html.parser")



Fast_text = '' 
Air_text = ''
Lcwu_text = '' 

Fast_text += createString(document_Fast1, "section")
Fast_text += createString(document_Fast2, "col-md-12")
Fast_text += createString(document_Fast3, "col-md-12")
Fast_text += createString(document_Fast4, "col-md-12")
Fast_text += createString(document_Fast5, "container")

Air_text += createString(document_Air1, "panel-body")
Air_text += createString(document_Air2, "panel-body")
Air_text += createString(document_Air3, "panel-body")
Air_text += createString(document_Air4, "col-md-9")
Air_text += createString(document_Air5, "col-md-12")

Lcwu_text += createString(document_Comsat1, "content-wrap")
Lcwu_text += createString(document_Comsat2, "content-wrap")
Lcwu_text += createString(document_Comsat3, "content-wrap")
Lcwu_text += createString(document_Comsat4, "content-wrap")
Lcwu_text += createString(document_Comsat5, "content-wrap")


Fast_nouns = listNouns(Fast_text)
Fast_verbs = listVerbs(Fast_text)
Fast_adjectives = listAdjectives(Fast_text)

Air_nouns = listNouns(Air_text)
Air_verbs = listVerbs(Air_text)
Air_adjectives = listAdjectives(Air_text)

Lcwu_nouns = listNouns(Lcwu_text)
lcwu_verbs = listVerbs(Lcwu_text)
lcwu_adjectives = listAdjectives(Lcwu_text)




dict0 = {'Nouns' : Fast_nouns, 'Verbs': Fast_verbs, 'Adjectives': Fast_adjectives}
df = pd.DataFrame.from_dict(dict0, orient='index')
df = df.transpose()
df.to_csv('Fast_University.csv')

dict1 = {'Nouns' : Air_nouns, 'Verbs': Air_verbs, 'Adjectives': Air_adjectives}
df1 = pd.DataFrame.from_dict(dict1, orient='index')
df1 = df1.transpose()
df1.to_csv('Air_University.csv')

dict2 = {'Nouns' : Air_nouns, 'Verbs': Air_verbs, 'Adjectives': Air_adjectives}
df2 = pd.DataFrame.from_dict(dict2, orient='index')
df2 = df2.transpose()
df2.to_csv('Lcwu_University.csv')

FastDataFrame = pd.read_csv("Fast_University.csv")
AirDataFrame = pd.read_csv("Air_University.csv")
LcwuDataFrame = pd.read_csv("Lcwu_University.csv")

px.histogram(FastDataFrame, x="Nouns")

px.histogram(AirDataFrame, x="Nouns")
px.histogram(LcwuDataFrame, x="Nouns")



data = {'Nouns':len(Fast_nouns), 'Verbs':len(Fast_verbs), 'Adjectives':len(Fast_adjectives)}

Names = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10,5))

plt.bar(Names, values, color = 'maroon', width = 0.4)
plt.xlabel("Fast University")
plt.ylabel("Count")
plt.show()

data = {'Nouns':len(Air_nouns), 'Verbs':len(Air_verbs), 'Adjectives':len(Air_adjectives)}

Names = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10,5))

plt.bar(Names, values, color = 'blue', width = 0.4)
plt.xlabel("Air Unviersity")
plt.ylabel("Count")
plt.show()


data = {'Nouns':len(Lcwu_nouns), 'Verbs':len(lcwu_verbs), 'Adjectives':len(lcwu_adjectives)}

Names = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10,5))

plt.bar(Names, values, color = 'brown', width = 0.4)
plt.xlabel("LCWU University Lahore")
plt.ylabel("Count")
plt.show()


G = nx.Graph()
for i in range(len(newstr)):
    temp_str = listNouns(newstr[i])
    G.add_nodes_from(temp_str)
    for j in range(len(temp_str) - 1):
        G.add_edge(temp_str[j], temp_str[j + 1])
    
        
    

plt.figure(figsize=(100,100))
pos = nx.spring_layout(G, k = 0.15, iterations = 20)
nx.draw(G, pos,node_size = 1600, font_size = 60, with_labels = True, alpha = 0.5, font_weight = "bold", node_shape= "s", linewidths = 40)
plt.show()
namenode = [node for (node, val) in G.degree()]
stop = ['\0']
AllNounsNexttoquality = []
for i in range(len(namenode)):
    for path in nx.all_simple_paths(G, source = namenode[i], target = "quality", cutoff=3):
        if str(path[0]) != str(stop[0]):
            AllNounsNexttoquality.append(path[0])
            stop.clear()
            for i in path:
                stop.append(i)

print("List of all the nouns that are at a distance of less than 5 from quality:\n")
print(AllNounsNexttoquality)
nx.write_edgelist(G, "text.edgelist.csv")
print("Number of connected Components  = ",nx.number_connected_components(G))
print("Is the graph Connected? = ")
nx.is_connected(G)

newstr = Air_text.split(sep = '.')
G=nx.Graph()

sentNouns = list()
for i in range(len(newstr)):
    temp_str = listNouns(newstr[i])
    G.add_nodes_from(temp_str)
    while (G.number_of_edges() < (G.number_of_nodes()*1)):
        r1 = random.choice(list(G.nodes()))
        r2 = random.choice(list(G.nodes()))
        if r1 != r2 and G.has_edge(r1,r2) == 0:
            G.add_edge(r1, r2)



plt.figure(figsize=(100,100))
pos = nx.spring_layout(G, k = 0.15, iterations = 20)
nx.draw(G, pos,node_size = 1500, font_size = 60, with_labels = True, alpha = 0.5, font_weight = "bold", node_shape= "s", linewidths = 50)
plt.show()
namenode = [node for (node, val) in G.degree()]
stop = ['\0']
AllNounsNexttoquality = []
for i in range(len(namenode)):
    for path in nx.all_simple_paths(G, source = namenode[i], target = "quality", cutoff=3):
        if str(path[0]) != str(stop[0]):
            AllNounsNexttoquality.append(path[0])
            stop.clear()
            for i in path:
                stop.append(i)

print("List of all the nouns that are at a distance of less than 5 from quality:\n")
print(AllNounsNexttoquality)

print("Number of connected Components  = ",nx.number_connected_components(G))
print("Is the graph Connected? = ")
nx.is_connected(G)

newstr = Lcwu_text.split(sep = '.')
G=nx.Graph()

sentNouns = list()
for i in range(len(newstr)):
    temp_str = listNouns(newstr[i])
    G.add_nodes_from(temp_str)
    while (G.number_of_edges() < (G.number_of_nodes()*1)):
        r1 = random.choice(list(G.nodes()))
        r2 = random.choice(list(G.nodes()))
        if r1 != r2 and G.has_edge(r1,r2) == 0:
            G.add_edge(r1, r2)



plt.figure(figsize=(100,100))
pos = nx.spring_layout(G, k = 0.15, iterations = 20)
nx.draw(G, pos,node_size = 1500, font_size = 60, with_labels = True, alpha = 0.5, font_weight = "bold", node_shape= "s", linewidths = 50)
plt.show()
namenode = [node for (node, val) in G.degree()]
stop = ['\0']
AllNounsNexttoquality = []
for i in range(len(namenode)):
    for path in nx.all_simple_paths(G, source = namenode[i], target = "Quality", cutoff=3):
        if str(path[0]) != str(stop[0]):
            AllNounsNexttoquality.append(path[0])
            stop.clear()
            for i in path:
                stop.append(i)

print("List of all the nouns that are at a distance of less than 5 from quality:\n")
print(AllNounsNexttoquality)


print("Is the graph Connected? = ")
print(nx.is_connected(G))
print("Number of connected Components  = ", nx.number_connected_components(G))