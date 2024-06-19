# VIM Tutorials
## VIM Modes
You should be aware of the most important concept in Vim before moving on: **modes** in Vim.

Everything in Vim is considered a mode. You can achieve whatever you want if you understand modes in Vim. There are many modes in Vim. But, we'll be looking at the 4 most important modes.

They are: 
1. **Command Mode**: This is the default mode (also called Normal mode) in Vim. Whenever Vim starts, you'll be in this mode. You can switch to any mode from this mode Basically, to switch from one mode to another, you have to come to Command Mode first and then navigate to the other mode. The commands that you run without any prefix (colon) indicate that you're running the command in command mode.

2. **Command-Line Mode**: You can use this mode to play around with some commands. But the commands in this mode are prefixed with a colon (:). You can switch to this mode by pressing : (colon) in command mode.

3. **Insert Mode**: This mode is used to edit the contents of the file. You can switch to insert mode by pressing `i` from command mode. You can use the `Esc` key to switch back to command mode.

4. **Visual Mode**: You use this mode to visually select some text and run commands over that section of code. You can switch to this mode by pressing `v` from the command mode.

## Useful Commands

### Open default VIM window (buffer)
`vim` 

Run this from terminal to open the default VIM window

### Create a new file from VIM
`:edit testfile.txt` 

This will open testfile.txt in edit mode or create a new text file with name testfile.txt

### Open a file
`vim filename.txt` 

Write **vim filename.txt** to open a file using VIM

### Insert text
`i` 

Press **i** to enter in insert mode to write any text file.

### Save file
`:w` 

Write **:w** to save file

### Quit file
`:q` 

Write **:q** to quit file

### Quit file without save
`:q!` 

Write **:q!** to quit file without save. If you write something but don't want to save it then write this.

### Save and Quit at one time
`:wq` 

Write **:wq** to save and quit at one time