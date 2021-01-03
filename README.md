# Music-Player
A Short GUI based Music Player

## Installing dependencies with pip
for Windows :- ```pip install -r requirements.txt```

for MacOS :- ```pip3 install -r requirements.txt```

## Running the program
1.choose your version PySimpleGUI or Tkinter
2. Run the ```Music_Player.py``` file.
3. A Prompt will ask for the file path or click the browse file button to browse the file (some non-copyrighted music is included in the `example music` folder)
4. Click OK.
5. the audio player will come and then you can :-
                                                Play
                                                pause
                                                unpause
                                                reset
                                                change volume (pysimplegui version only)
                                                change theme (pysimplegui version only)
5.After you are done click 'Exit Player' and the player will close               

## How to it all works!!
see the Pygame library is used to develop games (if you are reading you must know that) and it is pretty obvious that it games have music 𝄞. And because they have music there must be some way to play it 🥁. So, Pygame has the mixer class that can be accessed by 

```python
from pygame import mixer
```
now the mixer class has the functions for Playing music, Pausing Music, Unpausing music and resetting the music. 

hope you like it
