import pyshorteners

s = pyshorteners.Shortener()

link= input("enter the link: ")

s.tinyurl.short(link)

print(link)