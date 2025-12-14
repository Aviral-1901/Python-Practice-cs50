sentence = input("enter a sentence with emoticons : ")
#emoji vanda paile letter bata baneko emoji jasto lai emoticons vanido raixa
#like :) is happy and :( is sad

sentence = sentence.replace(':(','🙁')
sentence = sentence.replace(':)','🙂')
#using replace method of string i am replacing emoticon in sentence with an actual emoji

print(sentence)
                