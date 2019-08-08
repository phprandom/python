print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 30  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "a"
end4 = "i"
end5 = "n"
end6 = "s"
end7 = "m"
end8 = "o"
end9 = "k"
end10 = "e"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5,
print end6 + end7 + end8 + end9 + end10 + end11 + end12


while True:
    for i in ["/","- ","|","\\","|"]:
        print "%s\r" % i,
