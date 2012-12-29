# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Lisa McKenna

#2.1
print "*******************************"
print "Exercise 2.1"
print "I cannot figure what is going on here. Perhaps the leading 0 means it is 'in octal' which I found on google. Still confused though."
# I think the issue is that the leading 0 means the # is in 'octal notation' which I have a hazy grasp on.

#2.2
print "*******************************"
print "Exercise 2.2"
5
x = 5
x + 1
#no output when running 'python chapter2_exersises.py' because there are no print statements
print 5
print x
print x + 1
print "*******************************"

#2.3
print "Exercise 2.3"
width = 17
height = 12.0
delimiter = '.'

print width/2 
print "width/2 results in an integer"
print width / 2.0
print "width/2.0 results in a floating-point number"
print height/3
print "height/3 results in a floating-point number"
print 1 + 2 * 5
print "answer is 11 because of rule of precedence. multiplication comes first."
print delimiter * 5
print "the result is a string."
print "*******************************"

#2.4
print "Exercise 2.4"
# question 1
print (4.0 / 3.0) * 3.14 * (5**3)
# question 2
print (24.95 * .60 * 60.0) + (.75 * 59.0) + 3
# question 3
print "Question 3 was a challenge! With guidance from Will, here's how I came up with breakfast time of 7:30:06"
#took your advice
hour = 6
minute = 52
seconds = 0

new_minutes = minute + (7*3) + (8*2)
new_seconds = seconds + (12*3) + (15*2)
#figure out if the new minutes or new seconds are over 60
if new_minutes > 60:
	hour = hour + 1
	new_minutes = new_minutes - 60
#print new_seconds
if new_seconds > 60:
	new_minutes = new_minutes + 1
	new_seconds = new_seconds - 60

print hour
print new_minutes
print new_seconds
print "*******************************"



