
# Task 1: Hello
print(" ")
print("-----------------------Task 1: -------------------------------------------------") 
def hello():
    return "Hello!"
print(hello()) 

# Task 2: Greet
print(" ")
print("-----------------------Task 2: -------------------------------------------------") 
def greet(name):
    return f"Hello, {name}!" 
print(greet("James"))

# Task 3: Calculator
print(" ")
print("-----------------------Task 3: -------------------------------------------------") 
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                if b == 0:
                    return "You can't divide by 0!"
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                if b == 0:
                    return "You can't divide by 0!"
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation!"
    except Exception as e:
        return f"You can't multiply those values!"

# Example for debugging 
print("Addition: ",calc(5, 3, "add"))                     # output: 8
print(calc(5, 0, "divide"))                               # output: You can't divide by 0!
print("Multiply: ",calc("five", "three", "multiply"))     # output: You can't multiply those values!
print("Mul:", calc(5,"three","multiply"))

# Task 4: Data Type Conversion
print(" ")
print("-----------------------Task 4: -------------------------------------------------") 
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return "Invalid data type requested!"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

# Example for debugging 
print(data_type_conversion("42", "int"))            # output: 42
print(data_type_conversion("3.14", "float"))        # output: 3.14
print(data_type_conversion(100, "str"))             # output: "100"
print(data_type_conversion("nonsense", "float"))    # output: You can't convert nonsense into a float.

# Task 5: Grading System Using *args
print(" ")
print("-----------------------Task 5: -------------------------------------------------") 
def grade(*args):
    try:
        avg = sum(args) / len(args)
        match avg:
            case avg if avg >= 90:
                return "A"
            case avg if avg >= 80:
                return "B"
            case avg if avg >= 70:
                return "C"
            case avg if avg >= 60:
                return "D"
            case _:
                return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

# Example for debugging 
print(grade(95, 85, 92))    # output: A
print(grade(75, 80, 70))    # output: C
print(grade(50, 55, 58))    # output: F
print(grade(90, 70, 84))    # output: B
print(grade())              # output: Invalid data was provided. (No grades provided)
print(grade(90, "A", 85))   # output: Invalid data was provided.

# Task 6: Repeat a String Using a For Loop and Range
print(" ")
print("-----------------------Task 6: -------------------------------------------------") 
def repeat(string, count):
    result = ""  
    for _ in range(count): 
        result += string 
    return result

# Example for debugging 
print(repeat("Hello", 3))   # output: "HelloHelloHello"
print(repeat("A", 5))       # output: "AAAAA"
print(repeat("Test", 0))    # output: ""

# Task 7: Student Scores Using **kwargs
print(" ")
print("-----------------------Task 7: -------------------------------------------------") 
def student_scores(mode, **kwargs):
    if not kwargs:
        return "No Student data Provided."
    
    match mode:
        case 'best':
            return max(kwargs, key=kwargs.get)
        case 'mean':
            return sum(kwargs.values())/ len(kwargs)
        case _:
            return "invalid Mode!!"
        
# Example for debugging 
print(student_scores("best", Alice=85, Bob=92, Charlie=78))  # output: "Bob"
print(student_scores("mean", Alice=85, Bob=92, Charlie=78))  # output: 85.0
print(student_scores("best"))                                # output: "No student data provided."
print(student_scores("top", Alice=85, Bob=92))               # output: "Invalid mode!"       

# Task 8: Titleize a String
print(" ")
print("-----------------------Task 8: -------------------------------------------------") 
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}  
    words = text.split()  # Split the text into words
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower() 
    return " ".join(words) 

# Example for debugging 
print(titleize("the quick brown fox jumps over the lazy dog"))  
# output: "The Quick Brown Fox Jumps Over the Lazy Dog"

print(titleize("a journey in the world of python"))  
# output: "A Journey in the World of Python"

print(titleize("this is a test"))  
# output: "This is a Test"

# Task 9: Hangman (String Masking)
print(" ")
print("-----------------------Task 9: -------------------------------------------------") 
def hangman(secret, guess):
    masked_word = ""  
    for letter in secret:
        if letter in guess:  
            masked_word += letter
        else:
            masked_word += "_"  
    return masked_word

# Example for debugging
print(hangman("alphabet", "ab"))    # output: "a___ab__"
print(hangman("hangman", "hng"))    # output: "h_ng_an"
print(hangman("python", ""))        # output: "______"
print(hangman("testing", "tes"))    # output: "tes____"


# Task 10: Pig Latin Translator
print(" ")
print("-----------------------Task 10: ------------------------------------------------") 
def pig_latin(text):
    vowels = {"a", "e", "i", "o", "u"}
    words = text.split()  
    pig_latin_words = []  

    for word in words:
        if word[0] in vowels: 
            pig_latin_words.append(word + "ay")
        elif word[:2] == "qu": 
            pig_latin_words.append(word[2:] + "quay")
        else:  
            for i, letter in enumerate(word):
                if letter in vowels: 
                    pig_latin_words.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(pig_latin_words) 

# Example for debugging
print(pig_latin("apple banana quiet string"))  
# output: "appleay ananabay ietquay ingstray"
print(pig_latin("hello world"))  
# output: "ellohay orldway"
print(pig_latin("this is a test"))  
# output: "isthay isay aay esttay"
