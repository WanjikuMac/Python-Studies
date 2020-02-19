my_name = 'Wan Ji Ku'
my_age = 20
my_height = 5
my_weight = 53
my_eyes = 'Brown'
my_teeth = 'white'
my_hair = 'Black'

def convert(my_weight):
    return (my_weight * 1)/ 0.45359237
    

print(f"Let's talk about {my_name}.")
print("He's {} inches tall.".format(my_height))
print("He's {} kgs heavy.".format(my_weight))
print("Actually that's not too heavy")
print("He's got {0} eyes and {1} hair.".format(my_hair, my_eyes))
print("His teeth are usually {} depending on the food he takes".format(my_teeth))
total = my_age + my_height + my_weight
print("If I add {}, {}, and {} I get {}".format(my_age, my_height, my_weight, total))