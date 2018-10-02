""" 
Leah Emerson June 14 2018 last update October 2 2018
SIMPLE SCIPT TO MAKE SIMPLE SONGS FROM GPX FILES
****************************************************

Given one or more gpx files, extract gpx information:
from http://www.madpickles.org/rokjoo/2010/08/11/gpx-elevation-profile-plotting-with-the-google-chart-api/
for Python 3. (gpxstats.py and gpxlib.py)

Pysynth library used for song-creation:  https://mdoege.github.io/PySynth/

FUNCTIONS:
  keynote_to_keyname 
          allows reference to PySynth key notes by number rather than name. 

  statsToNotes 
        takes in the statistics of the gpx file, and based on on the distances as length of notes
        and elevation changes as pitch of note.

   createSong
        creates song, for each note generated in statsToNotes by mixing multiple types of music files together
"""
import pysynth_p
import pysynth_b
import pysynth_s
import mixfiles
import demosongs
import gpxstats
from mkfreq import getfreq
import sys

def keynote_to_keyname(song):
  pitchhz, keynum = getfreq()
  o = []
  for a, b in song:
    for x in keynum.keys():
      if keynum[x] == a - 1:
        k = x
    o.append((k, b))
  return o

def statsToNotes(points):
  highNotes=[]
  lowNotes = []
  elevationChanges = points['elevationChanges']
  distances = points['distances']
  
  #create a  note for each elevation change and length of note based on distance
  for i in range(len(points['elevationChanges'])):
    #takes elevation number and creates a value 44-88 for upper half of scale. creates length of note (2,4,8,16,32,64) based on distance
    if (elevationChanges[i] >= 0 ):
      noteHigh = (elevationChanges[i]*5 - ((elevationChanges[i]*5) %3))/3 
      lengthHigh = ((distances[i]/4) - ((distances[i]/4) %4)) 
      
      if(noteHigh <=44):
        noteHigh = noteHigh +44
      else:
        noteHigh = 88
     
      if (lengthHigh>32):
        lengthHigh = 64
      elif (lengthHigh==24):
        lengthHigh = 32
      elif(lengthHigh == 12 or lengthHigh==20):
        lengthHigh=16
      if (lengthHigh ==0):
        lengthHigh=2

      upperNote = (noteHigh,lengthHigh)
      print(upperNote)
      highNotes.append(upperNote)

    #takes elevation number when less than 0 and gives value 1-44 for lower half of scale
    else:
      posElevation = abs(elevationChanges[i])
      noteLow = int((posElevation - (posElevation %3))/3)
      lengthLow = ((distances[i]/4) - ((distances[i]/4) %4)) 
    
      if (noteLow <= 44):
        noteLow = 44 - noteLow
      else:
        noteLow = 0

      if (lengthLow>32):
        lengthLow = 64
      elif (lengthLow==24):
        lengthLow = 32
      elif(lengthLow == 12 or lengthLow==20):
        lengthLow=16
      elif (lengthLow ==0):
        lengthLow=2
      
      LowerNote = (noteLow,lengthLow)
      lowNotes.append(LowerNote)
  return highNotes, lowNotes

def createSong(highNotes, lowNotes, number):
  number = str(number)
  #piano-like sound for elevation changes that are greater than 0
  piano = tuple(highNotes)
  piano = keynote_to_keyname(piano)
  pianoName = "piano" + number + ".wav"
  pysynth_b.make_wav(piano, fn = pianoName)
  
  #percussion for elevation changes are less than 0
  low = tuple(lowNotes)
  low = keynote_to_keyname(low)
  percuussionName = "percussion" + number +".wav"
  pysynth_p.make_wav(low, fn=percuussionName)

  #string for more full sound, based on elevation changes less than 0
  stringName = "string" + number  + ".wav"
  pysynth_s.make_wav(low, fn =stringName)

  #mix files created (can only mix two at a time)
  firstMix = "mix" + number + ".wav"
  finalMix = "FINAL" + number + ".wav"
  mixfiles.mix_files(pianoName, percuussionName, firstMix)
  mixfiles.mix_files(stringName, firstMix, finalMix)

def main(argv=None):
  gpx = gpxstats.main()
  for i in range (len(gpx)):
    high, low = statsToNotes(gpx[i])
    createSong(high,low, i)

if __name__ == '__main__':
  sys.exit(main())

  