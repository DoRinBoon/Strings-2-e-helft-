# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
last_name = player[player.find(' '):]
print (first_name) 
 
last_name_len = len(last_name)
print (last_name_len)

name_short = (player[0] + '.' + last_name)
print (name_short)

yell = first_name + '! '
chant = yell *4
chant = chant.rstrip(chant[-1])
print (chant)

good_chant = (chant[-1] != ' ')
print (good_chant)
