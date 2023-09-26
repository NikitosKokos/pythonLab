days = int(input('Enter the number of days: '))
hours = int(input('Enter the amount of hours: '))
minutes = int(input('Enter the number of minutes: '))
seconds = int(input('Enter the number of seconds: '))
total_seconds = seconds + minutes * 60 + hours * 60 * 60 + days * 24 * 60 * 60
print('The total number of seconds: ' + str(total_seconds))