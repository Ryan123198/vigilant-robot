adj_1 = input("Please input an adjective ")
nat = input("Please input a nationality ")
name = input("Please input a name of a person ")
noun_1 = input("Please input a noun ")
adj_2 = input("Another adjective ")
noun_2 = input("Another noun ")
adj_3 = input("An adjective again ")
adj_4 = input("And an adjective again ")
noun_3 = input("Please input a plural noun ")
noun_4 = input("Then another noun ")
num_1 = input("Please input a number ")
shape = input("And any shape ")
food_1 = input("Please input a food ")
food_2 = input("Another food ")
num_2 = input("Finally, please input a number ")

MadLibs = """

Pizza was invented by a {} {}
chef named {}. To make pizza, you need
to take a lump of {}, and make a thin, round
{} {}. Then you cover it with
{} sauce, {} cheese, and fresh
chopped {}. Next you have to bake it in a very
hot {}. When it is done, cut it into {}
{}/s. Some kids like {} pizza the
best. but my favorite is the {} pizza. If I could, I
would eat pizza {} times a day!"""

print(MadLibs.format(adj_1, nat, name, noun_1, adj_2, noun_2, adj_3, adj_4, noun_3, noun_4, num_1, shape,  food_1,
                     food_2, num_2))