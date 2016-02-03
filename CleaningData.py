import pandas as pd
dfHeroesInfo = pd.read_csv('data/HeroIDAndMapID 2015-12-30 - 2016-01-29.csv')
dfReplaysChar = pd.read_csv('data/ReplayCharacters 2015-12-30 - 2016-01-29.csv')
dfReplays = pd.read_csv('data/Replays 2015-12-30 - 2016-01-29.csv')

#for testing purposes 
# dfReplays = dfReplays[:100]
# dfReplaysChar = dfReplaysChar[:100]

#Lets make some renaming
dfReplays.rename(columns={'ReplayID': 'replayID', 
                          'GameMode(3=Quick Match 4=Hero League 5=Team League)': 'mode',
                          'MapID':'MapID',
                          'Replay Length':'length','Timestamp (UTC)':"time"}, inplace=True)
dfReplaysChar.rename(columns={'ReplayID': 'replayID', 
                          'Is Auto Select': 'autoselect',
                          'HeroID':'heroID',
                          'Hero Level':'heroLvl','Is Winner':"win",
                             'MMR Before':'mmr'}, inplace=True)
# [replayID,mode,mmr2, team1mmr1 ... team1mmr5, mmr2, team2mmr1 ... team2mmr2, c11 ... c15,c21 ... c25, date, length  
#  month,day,weekday,year,hourday]

#Lets start by regrouping the ID into a dict
d = dict()
for i,v in dfReplays.iterrows():
#     print str(v['replayID'])
#     break
    if not str(v['replayID']) in d: 
        tempDate = pd.to_datetime(v["time"],format='%m/%d/%Y %I:%M:%S %p')
        d[str(v['replayID'])] = {'mmr1':[],'mmr2':[],'mode':v['mode'],
             'replayID':v['replayID'],'c1':[],'c2':[],
             'date': tempDate,
             'lenght':int(v['length'][3:5]),
             'month':tempDate.month,
             'day':tempDate.day,
             'year':tempDate.year,
             'hourday':tempDate.hour,
             'weekday':tempDate.weekday()}

#now lets add the team members
for i,v in dfReplaysChar.iterrows():
    #team1 is always winning
    if v['win']:
        d[str(v['replayID'])]['c1'].append(v['heroID'])
        d[str(v['replayID'])]['mmr1'].append(v['mmr'])
    else:
        d[str(v['replayID'])]['c2'].append(v['heroID'])
        d[str(v['replayID'])]['mmr2'].append(v['mmr'])
dft = pd.DataFrame.from_dict(d,orient='index')

dft.to_csv('data/clean.csv')
