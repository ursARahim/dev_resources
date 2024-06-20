# VIM Tutorials
## VIM Modes
You should be aware of the most important concept in Vim before moving on: **modes** in Vim.

Everything in Vim is considered a mode. You can achieve whatever you want if you understand modes in Vim. There are many modes in Vim. But, we'll be looking at the 4 most important modes.

They are: 
1. **Command Mode**: This is the default mode (also called Normal mode) in Vim. Whenever Vim starts, you'll be in this mode. You can switch to any mode from this mode Basically, to switch from one mode to another, you have to come to Command Mode first and then navigate to the other mode. The commands that you run without any prefix (colon) indicate that you're running the command in command mode.

2. **Command-Line Mode**: You can use this mode to play around with some commands. But the commands in this mode are prefixed with a colon (:). You can switch to this mode by pressing : (colon) in command mode.

3. **Insert Mode**: This mode is used to edit the contents of the file. You can switch to insert mode by pressing `i` from command mode. You can use the `Esc` key to switch back to command mode.

4. **Visual Mode**: You use this mode to visually select some text and run commands over that section of code. You can switch to this mode by pressing `v` from the command mode.

## Useful Basic Commands

### Open default VIM window (buffer)
`vim` 

Run this from terminal to open the default VIM window

### Create a new file from VIM
`:edit testfile.txt` 

This will open testfile.txt in edit mode or create a new text file with name testfile.txt

### Open a file
`vim filename.txt` 

Type **vim filename.txt** to open a file using VIM

### Insert mode
`i` 

Press **i** to enter in insert mode to write any text file.

### Save file
`:w` 

Type **:w** to save file

### Quit file
`:q` 

Type **:q** to quit file

### Quit file without save
`:q!` 

Type **:q!** to quit file without save. If you write something but don't want to save it then Type this.

### Save and Quit at one time
`:wq` 

Type **:wq** to save and quit at one time

## Cut, Copy, and Paste

### Copy
To copy any text insert into **visual** mode by typing `v`
select text by moving cursor, then to copy press `y`

### Cut
To cut a text type `d`

### Paste
To paste type `p`


## Undo and Redo

### Undo
To undo type `u`

### Redo 
To redo type `CTRL+R`

## Navigate or move cursor around a file
- **h** = move cursor left
- **l** = move cursor right
- **k** = move cursor up
- **j** = move cursor down

## Delete character, word, line
- **x** = delete the character that holds the cursor
- **dw** = dw stands for delete word. It will delete the word that the cursor holds
- **dd** = by typing double dd it will delete the whole line

## Beginning and end of a Line or the File
- **0** = Move beginning of the line
- **$** = Move end of the line
- **gg** = Move beginning of the file
- **G** = Move end of the file