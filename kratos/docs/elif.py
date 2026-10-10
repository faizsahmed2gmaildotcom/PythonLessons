# if <statement> - Runs code if <statement> is True
# elif <statement> - Runs code if <statement> is True, and all previous if/elif were False
# else - Runs code if all previous if/elif were False

height = 130

if height <= 60:
    print("baby")
if height <= 120:
    print("child")
if height <= 150:
    print("teen")
if height > 150:
    print("adult")

if height <= 60:
    print("baby")
elif height <= 120:
    print("child")
elif height <= 150:
    print("teen")
else:
    print("adult")
