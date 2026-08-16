list = ['thirty', 'days', 'of', 'python']

phrase1 = ' '.join(list)
print(phrase1)

phrase2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(phrase2)

company = 'Coding For All'
print(company)

print(len(company))

upper_case = company.upper()
print(upper_case)

lower_case = company.lower()
print(lower_case)

phrase2_format1 = phrase2.capitalize()
print(phrase2_format1)

phrase2_format2 = phrase2.title()
print(phrase2_format2)

phrase2_format3 = phrase2.swapcase()
print(phrase2_format3)

phrase2_sliced = phrase2[6:]
print(phrase2_sliced)

print("contains ? : ", company.find("Coding") != -1)
print("contains (with in) ? : ", "Coding" in company)

print(company.replace("Coding", "Python"))

phrase3 = 'Python For Everyone'
print(phrase3.replace("Everyone", "All"))

print(company.split())


GAFAM = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', ')
print(GAFAM)

print(company[0])
print("caractère 10 : ", company[10])

company_index = company.index("C")
print("index of C : ", company_index)

company_index2 = company.index("F")
print("index of F : ", company_index2)

company_index3 = company.rfind("l")
print("last index of l : ", company_index3)

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind("because"))

print(sentence.rindex("because"))

sentence2 = 'You cannot end a sentence with because because because is a conjunction'
start = sentence2.find("because")
print("start index of last 'because' : ", start)
end = sentence2.rfind("because")
print("end index of last 'because' : ", end)

sliced_sentence = sentence2[start:end + len("because")]
print("sliced sentence : ", sliced_sentence)

print('   Coding For All      '.strip())