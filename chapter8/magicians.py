# 8-9
magicians = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl']


def show_magicians(lists):
    for name in lists:
        print(name)

show_magicians(magicians)

# 8-10


# def make_great(lists):
#     great_lists = []
#     while lists:
#         name = lists.pop()
#         name = "the Great " + name
#         great_lists.append(name)
#     return great_lists

# show_magicians(make_great(magicians))

# 8-11
def make_great(lists):
    great_lists = lists[:]
    the_great_lists = []
    while great_lists:
        name = great_lists.pop()
        name = "the Great " + name
        the_great_lists.append(name)
    return the_great_lists

show_magicians(make_great(magicians))
print("******")
show_magicians(magicians)
