
cprint('Day 2: 30 Days of python programming')
first_name = 'Quentin'
last_name = 'MARRET'
full_name = first_name + ' ' + last_name
country = 'France'
city = 'Paris'
age = 26
year = 1999

type(first_name) # str
type(last_name) # str
type(full_name) # str   
type(country) # str
type(city) # str
type(age) # int
type(year) # int


print('longueur de prénom : ', len(first_name))
len(first_name) > len(last_name) # False
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
radius = float(input('Entrez le rayon du cercle : '))
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

print('Area of circle: ', area_of_circle)
print('Circumference of circle: ', circum_of_circle)


first_name = input('quel est ton prénom ?')
last_name = input('quel est ton nom ?')
full_name = first_name + ' ' + last_name
