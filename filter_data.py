
def pre_sentence(sentence):
    if ("\"sentence\":" in sentence):
        sentence = sentence.replace("\"sentence\": \"","").strip()
        sentence = sentence[0:len(sentence)-2]
        return sentence
    else:
        sentence = sentence.replace("\"headline\": \"", "").strip()
        sentence = sentence[0:len(sentence) - 2]
        sentence = sentence + " ."
        return sentence

def filter(list_sentence):
    new_list = []
    for i in range(0,len(list_sentence)-1):
        if (list_sentence[i] != list_sentence[i+1]):
            new_list.append(pre_sentence(list_sentence[i]))
    new_list.append(pre_sentence(list_sentence[len(list_sentence)-1]))
    return new_list

def like(word):
    return ''.join(e for e in word if e.isalnum())

def out(s_index, length, root_folder):
    ori_file = open("/home/binhnguyen/PycharmProjects/SpeakerIdentify/" + root_folder + "/" + root_folder + ".ori", "w")
    bin_file = open("/home/binhnguyen/PycharmProjects/SpeakerIdentify/" + root_folder + "/" + root_folder + ".bin", "w")
    com_file = open("/home/binhnguyen/PycharmProjects/SpeakerIdentify/" + root_folder + "/" + root_folder + ".com", "w")
    for i in range(0 , length):
        ori_file.write(list_sentence[s_index+i]+"\n")
        com_file.write(l_com_sent[s_index+i]+"\n")
        index = 0
        ls = list_sentence[s_index + i].split()
        list_result = [0 for ii in range(0, len(ls))]
        for word in l_com_sent[s_index+i].split():
            for idx in range(0 , len(ls)):
                # if like(ls[idx]) == like(word):
                if ls[idx] == like(word):
                    list_result[idx] = 1
                    index = idx + 1
                    break

        for num in list_result:
            bin_file.write(str(num))
        bin_file.write("\n")
    ori_file.close()
    bin_file.close()
    com_file.close()


list_sentence = []
l_com_sent = []
data = open("/home/binhnguyen/Downloads/cd.txt",'r').readlines()

for sentence in data:
    if "\"sentence\":" in sentence:
        list_sentence.append(sentence)

    if "\"headline\":" in sentence:
        l_com_sent.append(sentence)

list_sentence = filter(list_sentence)
l_com_sent = filter(l_com_sent)

out(0,8000,"train")
out(8000,1000,"valid")
out(9000,1000,"test")
# ori -> input
# bin -> out
# com -> cau nen

