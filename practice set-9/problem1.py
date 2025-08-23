f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("the word twinkle present in content")
else:
    print("the word twinkle is not present in content")
f.close()