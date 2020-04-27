"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
"""

widget_weigh = 75
gizmo_weigh = 112

widget_qtty = int(input("Give the quantity of widget that you need : \n"))
gizmo_qtty = int(input("Give the quantity of widget that you need : \n"))

print("Total weight of the order :\n{0} grams of widget\n{1} grams of gizmo".format(widget_qtty*widget_weigh,gizmo_qtty*gizmo_weigh))