# import inflect

# def number_to_words(num):
#     p = inflect.engine()
#     words = p.number_to_words(num)
#     return words

# number = int(input("Enter a number: "))
# print(f"The number in words is: {number_to_words(number)}")



# Without library
def number_to_words(num):
    under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    above_100 = {100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}

    if num < 20:
        return under_20[num]

    if num < 100:
        return tens[num // 10 - 2] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])

    # find the appropriate pivot - 'Million', 'Thousand' or 'Hundred'
    pivot = max([key for key in above_100.keys() if key <= num])

    return number_to_words(num // pivot) + ' ' + above_100[pivot] + ('' if num % pivot == 0 else ' ' + number_to_words(num % pivot))

number = int(input("Enter a number: "))
print(f"The number in words is: {number_to_words(number)}")
