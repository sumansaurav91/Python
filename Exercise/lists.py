# Working with lists
friends = ["Suman", "Saurav", "Sandy", "Soni", "Moni"]
friends[1] = "Singh"
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

# Working with list function
lucky_numbers = [4, 8, 15, 18, 36, 46]
friends = ["Suman", "Saurav", "Sandy", "Soni", "Moni"]
# friends.extend(lucky_numbers)
friends.append("Cradle")
friends.insert(2, "Kelly")
# friends.pop()
print(friends.index("Kelly"))
print(friends)
print(friends.count("Suman"))
friends.sort()
print(friends)
print(friends.reverse())