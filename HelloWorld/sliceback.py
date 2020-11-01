letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

#when using negative step, the start vlue has to be greater than the stop value

backwards = letters[25::-1]
print(backwards)
backwards = letters[::-1]
print(backwards)

backwards = letters[-10:-13:-1] # or [16:13:-1]
print(backwards)

backwards = letters[-22::-1]    #or [4::-1]
print(backwards)

backwards = letters[-1:-9:-1]   #or [:-9:-1]
print(backwards)


#Python Slice Idioms
#[::-1] is reverse
#[-4:] last 4 characters
#[:1] first 1 character
#[0] will give 1st chracter but error if empty string etc, thus the above is more userful





