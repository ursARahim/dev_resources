# Basic Linux Commands

#### Move to the root directory
`/`

#### Move to the home directory
`cd` or `cd ~`

#### Change the directory
`cd directoryname`

#### Go to the previous directory relative to the current directory
`cd ..`

#### Go to the previous directory from where you came
`cd -` 

#### Print the current working directory
`pwd`

#### Clear terminal screen
`clear`

#### List files and directories of current working directory
`ls`

#### List all visible and hidden files and directories with detailed information
`ls -la`

#### Create a directory
`mkdir testdir`

#### Remove a directory (empty or nonempty)
`rm -r testdir`

#### Create a file
`touch filename.txt`

#### Create a file with some text
`echo "test string" > file1.txt`

#### Append some text with existing file
`echo "test string 2" >> file1.txt`

#### Remove a file
`rm filename`

#### To show contents inside a file
`cat filename.txt`

#### Rename a directory or file
`mv prevname newname`

#### Move a directory or file in a new location
`mv prevlocation newlocation`

#### Copy a directory or file in a new location
`cp prevlocation newlocation`

#### Create directory like parent child
```
mkdir -p dir1/dir2/dir3

NB: It will create directory like dir2 under dir1 and dir3 under dir2
```

#### Determine the file type
```
file filname

NB: It will tell whether the file is file or directory
```

#### Save one file's contents in another file
```
cat file1.txt > file2.txt

NB: It will save contents of file1 into file2
```

#### Append one file's contents in another file
```
cat file1.txt >> file2.txt

NB: It will append contents of file1 into file2
```

#### View the contents of a file
```
1. cat filename.txt
2. more filename.txt
3. less filename.txt

NB: less is quite better

4. head filename.txt // shows first 10 lines
5. tail filename.txt // shows last 10 lines
```

#### Search text in a file
```
1. grep -i hello file.txt

explanation: grep (global regular expression) is by default case sensitive. Here -i means insensitive. It will search 'hello' in file.txt

2. grep -ir hello .

It will recursively search 'hello' in all files of current directory
