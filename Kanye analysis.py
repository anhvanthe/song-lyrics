common_words =['and', 'a', 'an', 'the', 'that', 'this', '', 'of',
               'in', 'for', 'at', 'it', 'to', 'the,', 'is' ]

def open_file(file_name):
    data = open(file_name, 'r')
    string_data = data.read()
    new_data = string_data.split('\n')
    words = []
    for i in new_data:
        words += i.lower().split(' ')
    return words 

def remove_common_words(words):
    running = True 
    while running:
        for i in words:
            if i in common_words:
                words.remove(i)
        if any(x in common_words for x in words):
            pass
        else:
            running = False
    return words

def words_count(words):  
    my_dict = {'x':0}
    for x in words:
        if x in my_dict:
            my_dict[x] += 1
        else:
            my_dict[x] =1
    return my_dict 
  
def most_common_words(my_dict):
    values = my_dict.values()
    best = max(values)
    words = []
    for i in my_dict:
        if my_dict[i] == best:
            words.append(i)
    return (words, best)

def words_often(my_dict, min_times):
    result = []
    done = False
    while not done:
        temp = most_common_words(my_dict)
        if temp[1] >= min_times:
            result.append(temp)
            for i in temp[0]:
                del(my_dict[i])
        else:
            done = True
    return result 

def export_csv(final_data, file_name):   
    import csv
    with open(file_name, "w", newline = '' ) as f:
        myWriter = csv.writer(f)
        myWriter.writerow(['words', 'count'])
        for i in final_data:
            myWriter.writerow([i])
            

list_data = open_file("Kanye West College Dropout Full.txt")
cleaned_data = remove_common_words(list_data)
final_data = words_often(words_count(cleaned_data), 1)           
export_csv(final_data, "kanye college dropout.csv")
        
            
            

