# probable-file-system
Python Script to copy the largest file(s) from a folder with optional sub-folders into a destination folder.  

You can choose the largest file based on file type (.txt, .mp3, .doc, etc). 

If this directory/folder structure below resembles what you have, this script helps you in copying and transferring the largest file based on size from each of the sub-directories.

This is also an easy way to copy songs from Osu because the game stores its mp3 files in the same structure below.

![file structure](https://github.com/ReStartQ/probable-system/blob/main/Structure.png)

## Osu Song Copy Tutorial
<br/>
To do this with Osu, find the Songs folder path and input it as the initial directory.

Ex: C:\Users\MyUserName\AppData\Local\osu!\Songs

<br/>
Then set the destination path

Ex: C:\Users\MyUserName\OneDrive\Desktop\New Folder

<br>
When it prompts for whether this is for osu, reply with y or yes. 

Note: Choosing no will let you input a file type but will go with a different naming standard compared to the osu standard. 

<br>
The original naming standard will keep the original file name and increment the file's name if there is a naming conflict in the destination folder.

The osu naming standard will rename the files to the name of the subdirectory and will default the file type to mp3.







## Simple run
To run this program just double click the main.py file.
## Running in terminal 
Another option to run the script is to do it in the terminal/cmd prompt, enter the following command:

python3 main.py


