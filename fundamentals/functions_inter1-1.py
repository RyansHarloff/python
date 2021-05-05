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

#chnage value
x[1][0] = 15

#change Jordan
students[0]= {'first_name': 'Michael' , 'last_name': 'Bryant'}

#change messi
sports_directory.update({'soccer' : ['Andres', 'Ronaldo', 'Rooney']})

#change z
z[0] = {'x': 10, 'y':30}

