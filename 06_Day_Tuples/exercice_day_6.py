empty_tuple = ()

tuple_sisters = ("Justine", "Tiphaine")
print(tuple_sisters)

tuple_brothers = ("Pierre", "Edouard")
print(tuple_brothers)

tuple_family = tuple_sisters + tuple_brothers
print(tuple_family)

print(len(tuple_family))

tuple_family_members = list(tuple_family)
tuple_family_members.append("Maman")
tuple_family_members.append("Papa")


tuple_family2 = tuple(tuple_family_members)
print(tuple_family2)


print('____exercice 2____')

justine, tiphaine, *cousins = tuple_family2

fruits_tuple = ("banane", "pomme", "poire", "fraise", "kiwi")
vegetables_tuple = ("carotte", "poivron", "tomate", "salade", "concombre")
animals_tuple = ("chien", "chat", "lapin", "hamster", "poisson")

food_stuff_tp = fruits_tuple + vegetables_tuple + animals_tuple
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle_index = len(food_stuff_lt) // 2
print(food_stuff_tp[middle_index])

print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print(nordic_countries.__contains__('Estonia'))
print(nordic_countries.__contains__('Iceland'))

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)