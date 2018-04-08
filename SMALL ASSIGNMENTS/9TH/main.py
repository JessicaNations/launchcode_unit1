def analyze_text(text):
    text_str = 0
    count = 0
    big_count = 0

    for i in range(len(text)):
            if text[i].isalpha():
                text_str += 1       
    for c in text:
        if c == 'e':
            count += 1
        if c == 'E':
            big_count += 1   
        result = count + big_count
        count_str = float(result*100/text_str)      
    big_answer = "The text contains " + str(text_str) + " alphabetic characters, of which " + str(result) + " (" + str(count_str) + "%) are 'e'."
    
    return big_answer

def main():

    text1 = "Eeeee"
    answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
    print(analyze_text(text1), answer1)

    text2 = "Blueberries are tasteee!"
    answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
    print(analyze_text(text2), answer2)

    text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
    answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
    print(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
    text4 = "Eeeee"
    answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
    print(analyze_text(text4), answer4)

    text5 = "Blueberries are tasteee!"
    answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
    print(analyze_text(text5), answer5)

    text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
    answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
    print(analyze_text(text6), answer6)

if __name__ == "__main__":
    main()
