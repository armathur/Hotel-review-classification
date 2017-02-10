import sys

# loading the label and review data into two dictionaries with common keys

train_label = {}
train_text = {}
test_text ={}

positive_words = {}
negative_words = {}
truthful_words = {}
deceptive_words = {}

positive_words_prob = {}
negative_words_prob = {}
truthful_words_prob = {}
deceptive_words_prob = {}

consolidated_class_prob = {}

sum_of_positive_class = 0
sum_of_negative_class = 0
sum_of_truthful_class = 0
sum_of_deceptive_class = 0

positive_reviews = 0
negative_reviews = 0
truthful_reviews = 0
deceptive_reviews = 0



file_train_labels =  sys.argv[1]
file_train_text=  sys.argv[2]

with open(file_train_labels , "r") as file_labels:
    for line in file_labels:
       (key, label1, label2) = line.split()
       train_label[key] = label1, label2


# Splitting the file with first 20 char being the key and remaining chars being the review

with open(file_train_text,"r") as file_reviews:
    for line in file_reviews:
       (key, review) = line[:20], line[21:]
       train_text[key] = review


total_records = len(train_label)

for key in train_text:
    tokenList =  train_text[key].split()
    if(train_label[key][1] == "positive"):
        for i in range(0 ,len(tokenList)):
            if(positive_words.has_key(tokenList[i])):
                positive_words[tokenList[i]] +=1
            else:
                positive_words[tokenList[i]] = 1
                negative_words[tokenList[i]] = 0


    if(train_label[key][1] == "negative"):
        for i in range(0 ,len(tokenList)):
            if(negative_words.has_key(tokenList[i])):
                negative_words[tokenList[i]] +=1
            else:
                negative_words[tokenList[i]] = 1
                positive_words[tokenList[i]] = 0

    if(train_label[key][0] == "truthful"):
        for i in range(0 , len(tokenList)):
            if(truthful_words.has_key(tokenList[i])):
                truthful_words[tokenList[i]] += 1
            else:
                truthful_words[tokenList[i]] = 1
                deceptive_words[tokenList[i]] = 0

    if(train_label[key][0] == "deceptive"):
        for i in range(0 , len(tokenList)):
            if(deceptive_words.has_key(tokenList[i])):
                deceptive_words[tokenList[i]] +=1
            else:
                deceptive_words[tokenList[i]] = 1
                truthful_words[tokenList[i]] = 0



for key in positive_words:
    positive_words[key] += 1
    negative_words[key] += 1
    deceptive_words[key]+= 1
    truthful_words[key] += 1


# print positive_words
# print negative_words
# print truthful_words
# print deceptive_words

for key in positive_words:
    sum_of_positive_class += positive_words[key]
    sum_of_negative_class += negative_words[key]
    sum_of_deceptive_class += deceptive_words[key]
    sum_of_truthful_class += truthful_words[key]

# print sum_of_truthful_class
# print sum_of_positive_class
# print sum_of_negative_class
# print sum_of_deceptive_class


for key in train_label:
    if(train_label[key][0] =="truthful"):
        truthful_reviews +=1
    if (train_label[key][0] == "deceptive"):
        deceptive_reviews +=1
    if (train_label[key][1] == "positive"):
        positive_reviews +=1
    if (train_label[key][1] == "negative"):
        negative_reviews +=1

prior_prob_positive = positive_reviews/float(total_records)
prior_prob_negative = negative_reviews/float(total_records)
prior_prob_truthful = truthful_reviews/float(total_records)
prior_prob_deceptive = deceptive_reviews/float(total_records)


for key in positive_words:
    positive_words_prob[key] = positive_words[key]/float(sum_of_positive_class)
    negative_words_prob[key] = negative_words[key]/float(sum_of_negative_class)
    truthful_words_prob[key] = truthful_words[key] /float(sum_of_truthful_class)
    deceptive_words_prob[key] = deceptive_words[key]/float(sum_of_deceptive_class)


for key in positive_words_prob:
    consolidated_class_prob[key] = positive_words_prob[key], negative_words_prob[key], truthful_words_prob[key], deceptive_words_prob[key]

consolidated_class_prob["my_var_prior_probs"] = prior_prob_positive, prior_prob_negative, prior_prob_truthful, prior_prob_deceptive

for key in consolidated_class_prob:
    with open("nbmodel.txt","a") as file_model:
        file_model.write(key + " " +str(consolidated_class_prob[key][0]) + " "+ str(consolidated_class_prob[key][1]) + " " + str(consolidated_class_prob[key][2]) + " "+ str(consolidated_class_prob[key][3]) + "\n")



#classifier

#prior probability calculation


#
# # print prior_prob_positive
# # print prior_prob_negative
# # print prior_prob_truthful
# # print prior_prob_deceptive
#
# #test case
# #zvwkh674t2sxSGHHkXgm I would definitely recommend this hotel to anyone wanting accommodation in Chicago. Ideal position, lovely quiet rooms, good facilities, complimentary breakfast well received and the Manager's evening drinks reception excellent; we always tipped the staff who were serving our drinks. The in-house Amalfitini cocktail was very good. The staff were very friendly and helpful. If I ever return to Chicago I would certainly stay there again. Theres nothing bad I can say about this hotel.
#
#
# #string = "zvwkh674t2sxSGHHkXgm I would definitely recommend this hotel to anyone wanting accommodation in Chicago. Ideal position, lovely quiet rooms, good facilities, complimentary breakfast well received and the Manager's evening drinks reception excellent; we always tipped the staff who were serving our drinks. The in-house Amalfitini cocktail was very good. The staff were very friendly and helpful. If I ever return to Chicago I would certainly stay there again. Theres nothing bad I can say about this hotel. "
#
#
# with open("hw2-data-corpus/test-text.txt","r") as file_reviews_test:
#     for line in file_reviews_test:
#        (key, review) = line[:20], line[21:]
#        test_text[key] = review
#
#
# for key in test_text:
#     test_case = test_text[key].split()
#
#     prob_positive = math.log10(prior_prob_positive)
#     for itr in range(1,len(test_case)):
#         if(positive_words_prob.has_key(test_case[itr])):
#             prob_positive +=  math.log10(positive_words_prob[test_case[itr]])
#
#     #print prob_positive
#
#     prob_negative = math.log10(prior_prob_negative)
#
#     for itr in range(1,len(test_case)):
#         if(negative_words_prob.has_key(test_case[itr])):
#             prob_negative +=  math.log10(negative_words_prob[test_case[itr]])
#
#     #print prob_negative
#
#     prob_truthful = math.log10(prior_prob_truthful)
#
#     for itr in range(1,len(test_case)):
#         if(truthful_words_prob.has_key(test_case[itr])):
#             prob_truthful +=  math.log10(truthful_words_prob[test_case[itr]])
#
#     #print prob_truthful
#
#
#
#     prob_deceptive = math.log10(prior_prob_deceptive)
#
#     for itr in range(1,len(test_case)):
#         if(deceptive_words_prob.has_key(test_case[itr])):
#             prob_deceptive +=  math.log10(deceptive_words_prob[test_case[itr]])
#
#     #print prob_deceptive
#
#
#     if (prob_truthful > prob_deceptive):
#         decision = key + " truthful"
#
#     else:
#         decision = key + " deceptive"
#
#
#     if(prob_positive > prob_negative):
#         decision += " positive"
#     else:
#         decision += " negative"
#
#     with open("hw2-data-corpus/decision_file.txt","a") as file_decision:
#      file_decision.write(decision + "\n")
