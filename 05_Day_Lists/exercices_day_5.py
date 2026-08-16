list = []

list_5_items = ['item1', 'item2', 'item3', 'item4', 'item5']

print(len(list_5_items))

mixed_data_types = ['Quentin', 26, 1.87, 'couple', '9 chemin de la chapeaude']

it_compagnies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_compagnies)

print("Nombre de companies dans la liste:", len(it_compagnies))

print( "première companie de la liste : ", it_compagnies[0])
print( "dernière companie de la liste : ", it_compagnies[-1])
print( "company du milieu de la liste : ", it_compagnies[len(it_compagnies)//2])

it_compagnies[0] = 'Meta'
print(it_compagnies)

it_compagnies.append('Netflix')
print(it_compagnies)

it_compagnies.insert(len(it_compagnies)//2, 'Spotify')

it_compagnies[0].upper()
print(it_compagnies)

print('#'.join(it_compagnies))

assert 'IBM' in it_compagnies

it_compagnies.sort()
print('list sorted', it_compagnies)

it_compagnies.reverse()

print('list de départ : ', it_compagnies)
sliced_3_first = it_compagnies[0:3]
sliced_3_last = it_compagnies[-3:]

print("sliced : ", sliced_3_first)
print("sliced : ", sliced_3_last)

print('____delete it_compagnies____')

print("list de départ : ", it_compagnies)

del it_compagnies[0]  # Delete the first item
print(it_compagnies)

it_compagnies.pop()
print(it_compagnies)

print("___destroy list___")
it_compagnies.clear()
print(it_compagnies)

del it_compagnies
# print(it_compagnies)  # This will raise an error because the list has been deleted


print("____join list____")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end
print(joined_list)

new_full_stack = joined_list.copy()
print(new_full_stack)

index_redux = new_full_stack.index('Redux')
new_full_stack.insert(index_redux + 1, 'Python')
new_full_stack.insert(index_redux + 2, 'SQL')
print(new_full_stack)

print('____exercice 2_____')

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = ages[0]
max = ages[-1]
print("min : ", min)
print("max : ", max)

if len(ages) % 2 == 0:
    median = (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
else:
    median = ages[len(ages)//2]
print("median : ", median)

average = sum(ages) / len(ages)
print("average : ", average)

range_ages = max - min
print("range : ", range_ages)

comparaison = abs(min - average) < abs(max - average)
print("comparaison : ", comparaison)

from countries import countries

print(countries)
median_country = countries[len(countries) // 2]
print("median country : ", median_country)

contries_1 = countries[:len(countries)//2]
contries_2 = countries[len(countries)//2:]

countries_reduced = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

chine, russie, use, *nordique = countries_reduced
print(nordique)