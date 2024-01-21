def containsDuplicate(self, nums: list[int]) -> bool:
    dicty = {}      # Dictionary to store values
    for i in nums:
        if i not in dicty:
            dicty[i] = 1
        else:
            return False    # if the number is present in dictionary then return False
    return True     # After checking through the whole list, return True