# GPS-Jingle

Takes in a .gpx file and creates a jingle based on elevation change. The idea is to be able to create a song based on your run, bike. Warning: the songs are not usually great-sounding, but thats the joy of something unique to each excursion. 

I implemented this idea by expanding on exsisting code:

Extracting elevation change data from a gpx file was adopted from: www.madpickles.org/rokjoo/2010/08/11/gpx-elevation-profile-plotting-with-the-google-chart-api/

Music created using PySynth: https://mdoege.github.io/PySynth/

## To Run:

  Download gpxlib.py and gpxstats.py

  Download PySynth https://mdoege.github.io/PySynth/ 

#### In the terminal run gpxstats.gpx and use your .gpx file : 
(If you use MapMyRun you can export gpx files of your workouts from their website)

    python gpxstats.py -i sample.gpx

   This will create a file called "FINAL.wav" in the folder of gpxstats.gpx

I have found that iTunes plays the file automatically, however, there are .wav to .mp3 converters online for a more convenient format. 

### Issues:
  
  *Pysynth is a very simple synthesizer and can only have one sound at once. In order to achieve more than one sound, .wav files must be combined. Therefore multiple .wav files are created for each song, but FINAL.wav is the sounds combined*
  
  
 Please let me know if you find any issues or have questions.


Enjoy your custom songs! 





