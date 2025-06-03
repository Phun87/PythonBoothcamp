# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkOrange")
# timmy.forward(100)
#
#
#
# my_screen = Screen()
# my_screen.canvheight = 300
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander",]) #Adds column
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Quilladin", "Grass"])#Adds row
table.add_row(["Kakuna", "Bug · Poison"])
table.align = "l" #align the contents to left
# print(table)
my_string = table.get_string()
print(my_string)