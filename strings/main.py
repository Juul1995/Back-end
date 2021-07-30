# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54 

scorers = player_0 +" "+ str(goal_0) + ', ' + player_1 +" "+ str(goal_1) # no need for the space in front of /n 
report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute"

player = 'Wim Kieft'
first_name = player[:player.find(" ")]
last_name = player[player.rfind(" ") + 1:]
last_name_len = len(player[player.find(" ") + 1:])
name_short = first_name[0] + '. ' + last_name

chant_name = first_name +'!'
print (chant_name)
chant = chant_name + " " +  chant_name + " " +  chant_name #get rid of the space after Wim! 

good_chant = chant[-1] != " "

print(scorers)
print(report)
print(chant)
print(good_chant)



