from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.decode('utf-8').split()
    for word in line_words:
        story_words.append(word)
story.close


# from urllib.request import urlopen
# bytes = urlopen('http://sixty-north.com/c/t.txt')
# print("\n1st bytes\n")
# print(bytes)
# print(type(bytes))
# story_words = []
# for foo in bytes:
#     line_words = foo.decode('utf-8').split()
#     for thunder in line_words:
#         story_words.append(thunder)
# bytes.close
# print("\n2ndbytes\n")
# print(bytes)
# print(type(bytes))
# print("\nfoo\n")
# print(foo)
# print(type(foo))


#     # print("\nword\n")
#     # print(word)
#     # print(type(word))
