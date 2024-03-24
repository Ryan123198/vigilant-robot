x = "I have %s friends named %s, %s and %s."
friend_1 = "Joey"
friend_2 = "Chandler"
friend_3 = "Ross"
friend_4 = "Bob"
friend_5 = "Gu\nther"
num1 = 3
num2 = 4
y = ", %s and"

print(friend_1 + "\n" + friend_2 + "\n" + friend_3 + "\n" + friend_4)
print(num1 * (friend_1 + "\b"))
print(x % (num1, friend_1, friend_2, friend_3))
print(x.replace(" and", y) % (num2, friend_1, friend_2, friend_3, friend_4))
print(x.replace("%s", "%r") % (num1, friend_1, friend_2, friend_5))
