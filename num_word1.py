def number_to_words(num):
    num_dict = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",
                "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
    hundred_dict = {"1": "One hundred", "2": "Two hundred", "3": "Three hundred",
                    "4": "Four hundred", "5": "Five hundred", "6": "Six hundred",
                    "7": "Seven hundred", "8": "Eight hundred", "9": "Nine hundred"}
    tens_dict = {"2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty",
                 "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}
    ones_case = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen",
                 "14": "Fourteen", "15": "Fifteen", "16": "Sixteen",
                 "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}

    length = len(num)
    string = ""
    
    # Handle hundreds place
    if length == 3 and num[0] in hundred_dict:
        string += hundred_dict[num[0]]
        if num[1] != "0" or num[2] != "0":  # Add "and" if tens or units are non-zero
            string += " and "
        length -= 1
        num = num[1:]

    # Handle tens place
    if length == 2:
        if num[0] == "1":  # Handle special case for numbers 10-19
            string += ones_case[num[0] + num[1]]
            return string
        elif num[0] in tens_dict:
            string += tens_dict[num[0]]
            if num[1] != "0":
                string += " "
        length -= 1
        num = num[1:]
    
    # Handle units place
    if length == 1 and num[0] in num_dict:
        string += num_dict[num[0]]
    
    return string

# Get input from user
num = input("Enter a number up to 999: ")
print(number_to_words(num))
