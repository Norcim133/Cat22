import urllib2

response = urllib2.urlopen('http://www.cnn.com')
html = response.read()

sad = 0

list_of_words = html.split(' ')
for word in list_of_words:
    if word == "is":
        sad += 1
print sad