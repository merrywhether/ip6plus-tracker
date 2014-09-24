# iPhone 6+ CLI tracking Tool

This is a Python-based command line tool to allow you track the inventory of iPhone 6+s at your local Apple Store. I can only guarantee that it will run on a Mac (due to the nature of some of the sound events), and it is based entirely on standard-library functionality to ensure the easiest setup for non-developers.

This tool was developed for the MacRumors community, as posted [here](http://forums.macrumors.com/showthread.php?p=19868260#post19868260).

--------

It tracks phones by model number, and it features 2 main modes:
* a loud song alert so that you don't have to be at your computer to know that inventory levels have changed
* a quiet beep alert when you are at your computer so that you can be a little more discrete

You can mix these modes as well, if there's one you're really hoping for but are also curious about other closely-spec'ed models.

It also supports restarting your last search (which is automatically saved).

--------

To start the program (for those uncomfortable with command line):
* navigate in Finder to the folder containing the python files
* open Terminal.app (in /Applications/Utilities or searchable with Spotlight)
* drag the 'run.py' file into the terminal window (this should auto-input the path to the file)
* hit enter and follow the on-screen prompts

Other notes:
* I've made this entirely with vanilla python 2.7, which is built-in to OS X Mountain Lion and OS X Mavericks, so you won't need to download any additional software.
* The program enters an infinite loop searching for inventory on a regular basis. In order to quit the program at any time, press ctrl-c.
* To restart, you can press the up arrow (this will show you the previously entered command) in the same terminal window it was previously using and then press enter again.

--------

If you want to track iPhone 6 models, they are listed in the models.py folder in the ip6plus_tracker folder but are currently commented out. If you'd like to enable them, just delete the hashes in front of any you'd like to track.