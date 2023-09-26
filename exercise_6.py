# import math

# seconds = int(input('Enter the number of seconds: '))
# days = math.floor(seconds / (24 * 60 * 60))
# hours = math.floor((seconds % (24 * 60 * 60)) / (60 * 60))
# minutes = math.floor(((seconds % (24 * 60 * 60)) % ( 60 * 60)) / (60))
# seconds = ((seconds % (24 * 60 * 60)) % ( 60 * 60)) % 60

# print(f"d:h:m:s -> {days}:{hours}:{minutes}:{seconds}")

time = int(input('Enter the number of seconds: '))
days = time // (24 * 60 * 60)
hours = time % (24 * 60 * 60) // (60 * 60)
minutes = time % (24 * 60 * 60) % (60 * 60) // 60
seconds = time % (24 * 60 * 60) % (60 * 60) % 60

print(f"d:h:m:s -> {days}:{hours}:{minutes}:{seconds}")