#1 update values in a dictionary and list
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
x[1][0] = 15
#2
students[0]['last_name'] = "Bryant"
#3
sports_directory['soccer'][0] = "Andres"
#4
z[0]['y'] = 30

print(x)
print(students[0])
print(sports_directory['soccer'])
print(z)

#2 Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for student in some_list:
        print (f"first_name - {student['first_name']}, last_name - {student['last_name']}")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 

#3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for students in some_list:
        print(students[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4 Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(key)} {key.upper()}")
        for value in some_dict[key]:
            print(value)
        print("-------------")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

