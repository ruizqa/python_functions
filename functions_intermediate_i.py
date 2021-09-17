
#Update values in dictionaries and lists

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

x[1][0]=15
print(x)
students[0]["last_name"] = "Bryant"
print(students)
sports_directory["soccer"][0]="Andres"
print(sports_directory)
z[0]["y"] =30
print(z)


#Iterate through a list of dictionaries

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(dict_list):
    output=""
    for d in dict_list:
        i=0
        for k,v in d.items():
            output += f"{k} - {v}"
            if i<len(d)-1:
                output+=", "
            i+=1
        output += "\n"
    print(output)

iterateDictionary(students)

#Get values from list of dictionaries

def iterateDictionary2(key_name, some_list):
    i=0
    for d in some_list:
        print(some_list[i][key_name])
        i+=1

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#Iterate through a dictionary with list values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for k in some_dict:
        print("-"*10)
        print(len(some_dict[k]),k.upper())
        for i in some_dict[k]:
            print(i)
        

printInfo(dojo)


