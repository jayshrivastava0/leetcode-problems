def letterCombinations(digits: str):
    if not digits:  # If the input is empty, return an empty list
        return []
    dicty = {
        '1': [],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    listy = []  # Initialize an empty list to store the combinations

    # Iterate over each digit in the input
    for ele1 in dicty[digits[0]]:  # Iterate over the characters corresponding to the first digit
        try:
            for ele2 in dicty[digits[1]]:  # Iterate over the characters corresponding to the second digit
                try:
                    for ele3 in dicty[digits[2]]:  # Iterate over the characters corresponding to the third digit
                        try:
                            for ele4 in dicty[digits[3]]:  # Iterate over the characters corresponding to the fourth digit
                                listy.append(ele1 + ele2 + ele3 + ele4)  # Append the combination to the list
                        except:
                            listy.append(ele1 + ele2 + ele3)  # Append the combination to the list (without fourth digit)
                except:
                    listy.append(ele1 + ele2)  # Append the combination to the list (without third and fourth digits)
        except:
            listy.append(ele1)  # Append the combination to the list (without second, third, and fourth digits)

    return listy
