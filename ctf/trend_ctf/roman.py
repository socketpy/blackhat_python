
operation = ['*','+','(',')','-','/']
roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
def iterate(received):
    new_string = ""
    n = 0
    i = 0
    while i < len(received):
        char = received[i]
        roman_temp = ""
        if char in roman:
            roman_temp = char
            i += 1
            while received[i] != ' ':
                roman_temp += received[i]
                i += 1
            n = roman_to_int(roman_temp)
            new_string += str(n)
            print "Roman: ", str(n)
            continue;
        elif str.isalpha(char):
            alpha_temp = char
            i+=1
            while i < len(received) and received[i] not in operation :
                if received[i] == ',':
                    i+=1
                    continue
                elif received[i] == '=':
                    break
                alpha_temp += received[i]
                i += 1
            n = text2int(alpha_temp)
            new_string += str(n)
            print "Alphabet: ", str(n)
            continue;

        elif char in operation:
            new_string += char
        elif char == ',' or char == '=' :
            i += 1
            continue;
        else:
            new_string += char
        i += 1

    return new_string

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def roman_to_int(input):
   if type(input) != type(""):
      raise TypeError, "expected string, got %s" % type(input)
   input = input.upper()
   nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
   ints = [1000, 500, 100, 50,  10,  5,   1]
   places = []
   for c in input:
      if not c in nums:
         raise ValueError, "input is not a valid roman numeral: %s" % input
   for i in range(len(input)):
      c = input[i]
      value = ints[nums.index(c)]
      # If the next place holds a larger number, this value is negative.
      try:
         nextvalue = ints[nums.index(input[i +1])]
         if nextvalue > value:
            value *= -1
      except IndexError:
         # there is no next place.
         pass
      places.append(value)
   sum = 0
   for n in places: sum += n
   # Easiest test for validity...
   return sum

a = raw_input()
print iterate(a)
