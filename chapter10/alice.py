def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

try:
    FileNotFoundError
except NameError:
    #py2
    FileNotFoundError = IOError
    
filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
