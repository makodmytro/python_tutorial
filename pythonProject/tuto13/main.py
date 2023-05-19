age = int(input('input your age!'))

if age >= 18:
    print('You are an adult.')
else:
    print('You are not an adult.')

# example of elif instruction

marks = int(input('input your marks'))

if marks >= 90:
    print('Grade A')
elif marks >= 70:
    print('Grade B')
elif marks >= 50:
    print('Grade C')
else:
    print('You are failed!')