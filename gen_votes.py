#!/usr/bin/env python3.4
f = open("all_votes.csv","r")
max_vote_id = 0
politicians = {}
names = {}
first_names = {}
affiliation = {}
f_affiliation = open("affiliation.txt","r")
for line in f_affiliation:
    elements = line.split()

    name = ""
    i = 0

    for word in elements[:-1]:
        if word != "SC-ALA":
            name += word

    if len(elements) > 2:
        party = elements[-1]
    else:
        party = ""

    affiliation[name.casefold()] = party


for line in f.readlines()[1:]:
    elements = line.split(",")
    elements = [e.replace('"','') for e in elements]

    first_name = elements[1]
    name = elements[2]
    politician_id = int(elements[0])
    vote_id = int(elements[3])
    ramo = elements[4]

    if ramo != "C": continue

    if "Favorevole" in elements[6]:
        vote = 1
    elif "Contrario" in elements[6]:
        vote = 2
    else:
        vote = 9

    if politician_id not in politicians:
        politicians[politician_id] = {}

    if politician_id not in names:
        names[politician_id] = name
        first_names[politician_id] = first_name

    if vote != 9:
        politicians[politician_id][vote_id] = vote

    if vote_id > max_vote_id: max_vote_id = vote_id

f_out = open("camera.csv","w")

first_line = "Last Name,First Name,ID,Occupation,Party,Date Entered,Date Exited,Note,CONSTITUENCY,Type of Information,Religion,"
for i in range(max_vote_id):
    first_line+=str(i)+","
first_line = first_line[:-1]

print(first_line,file=f_out)

for politician_id in politicians:
    votes = politicians[politician_id]
    all_lower = (names[politician_id] + first_names[politician_id]).replace(" ","").casefold()
    try:
        party = affiliation[all_lower]
    except KeyError:
        party = "None"
    output = "%s,%s,%s,Politician,%s,in,out,note,const,aff,rel," % (names[politician_id], first_names[politician_id], str(politician_id),party)



    for i in range(max_vote_id):
        if i in votes:
            output += str(votes[i])+","
        else:
            output += "9,"
    print(output[:-1],file=f_out)
