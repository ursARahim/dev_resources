# Managing users and groups

#### See the list of users
`cat /etc/passwd`

#### Create a user
`useradd username`

#### Delete a user
`userdel username`

#### Modify a user
```
usermod

NB: Use the usermod command. like to change user name use: usermod -l oldusername newusername
```

#### To see all the groups of current user
`groups`

#### To see all the groups of a specific user
`groups username`

#### To crate a group
```
groupadd devs
NB: These are the secondary groups. Primary groups are by default attached to every user. 
A primary group will also be created by the username also.
```

#### To modify a group 
```
groupmod

NB: Add a user to a specific group
groupmod -G devs username
```

#### To delete a group
`groupdel`


