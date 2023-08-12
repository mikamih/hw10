names = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}

print("List of students:")
for student in names['students']:
    print("- " + student['firstName'] + " " + student['lastName'])

print("\nList of teachers:")
for teacher in names['teachers']:
    print("- " + teacher['firstName'] + " " + teacher['lastName'])