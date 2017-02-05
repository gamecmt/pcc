from name_funciton import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = raw_input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = raw_input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
