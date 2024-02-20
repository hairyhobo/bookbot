def main():
  with open("books/frankenstein.txt") as f:
    file_content = f.read()
    word_count = Word_Count(file_content)
    #print(len(word_count))
    letter_count = count_letters(file_content)
    #print(letter_count)
    print(f"--- Begin report of {f.name} ---")
    print(f"{word_count} words found in the document")
    for i in range(len(letter_count)):
      print(f"The '{letter_count[i]['Letter']}' character was found {letter_count[i]['Count']} times")
    print("--- End report ---")

def Word_Count(text : str):
  return text.split()

def count_letters(text : str):
  lower_case_text = text.lower()
  letter_count = {}
  for i in range(len(lower_case_text)):
    if lower_case_text[i].isalpha():
      
      if lower_case_text[i] in letter_count:
        letter_count[lower_case_text[i]] += 1
      else:
        letter_count[lower_case_text[i]] = 1

  letter_count_list = []
  for key in letter_count.keys():
    letter_count_list.append({"Letter": key,"Count":letter_count[key]})
  #print(letter_count_list)
  letter_count_list.sort(reverse=True,key=lambda x: x['Count'])
  return letter_count_list






main()