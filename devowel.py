state_names = ["Alabama", "California", "Oklahoma", "Florida"]
vowels = list("aeiou")
output = []

texas = "Texas"
print(texas)
tezas = texas.replace('x', 'z')
print(texas)
print(tezas)
texas = tezas
print(texas)

print(state_names)
state_names.remove("Alabama")  # actually mutates (changes) the list
print(state_names)

for state in state_names:
    state_lower = state.lower()  # new list with states in lower case
    for vowel in vowels:
        # if vowel in state_names:
            # print(True)
            try:
                # print(state_lower, type(state_lower), state, type(state), vowel)
                state_lower = state_lower.replace(vowel, '')
                print(state_lower)
            except Exception as error:
                print("!!! Caught exception:", error)
                break
    output.append("".join(state_lower).capitalize())

print(output)
