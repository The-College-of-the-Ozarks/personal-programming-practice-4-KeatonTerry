# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

mph = input("Input speed in mph: ")
mph = float(mph)

print("Which conversion would you like to use?:")
print("if mph to kph, enter 1")
print("if mph to ms, enter 2")
print("if mph to fts, enter 3")
convert = input("input the number that corresponds to your choice: ")

if convert == "1":
    print("Speed in kph is", mph_to_kph(mph))
elif convert == "2":
    print("Speed in m/s is", mph_to_ms(mph))
elif convert == "3":
    print("Speed in ft/s is", mph_to_fts(mph))
else:
    print("This input is invalid")
