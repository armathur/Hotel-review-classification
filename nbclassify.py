
import math
import sys
import string

test_text = {}
consolidated_class_prob = {}

train_label = {}
train_text = {}

with open("nbmodel.txt","r") as file:
    for line in file:
        (key, positive_words_prob, negative_words_prob, truthful_words_prob, deceptive_words_prob) = line.split()
        consolidated_class_prob[key] = positive_words_prob, negative_words_prob, truthful_words_prob, deceptive_words_prob




prior_prob_positive, prior_prob_negative, prior_prob_truthful, prior_prob_deceptive  = consolidated_class_prob["my_var_prior_probs"]

#
# print prior_prob_positive
# print prior_prob_negative
# print prior_prob_truthful
# print prior_prob_deceptive

#test case
#zvwkh674t2sxSGHHkXgm I would definitely recommend this hotel to anyone wanting accommodation in Chicago. Ideal position, lovely quiet rooms, good facilities, complimentary breakfast well received and the Manager's evening drinks reception excellent; we always tipped the staff who were serving our drinks. The in-house Amalfitini cocktail was very good. The staff were very friendly and helpful. If I ever return to Chicago I would certainly stay there again. Theres nothing bad I can say about this hotel.


#string = "zvwkh674t2sxSGHHkXgm I would definitely recommend this hotel to anyone wanting accommodation in Chicago. Ideal position, lovely quiet rooms, good facilities, complimentary breakfast well received and the Manager's evening drinks reception excellent; we always tipped the staff who were serving our drinks. The in-house Amalfitini cocktail was very good. The staff were very friendly and helpful. If I ever return to Chicago I would certainly stay there again. Theres nothing bad I can say about this hotel. "

file_test = sys.argv[1]

with open(file_test,"r") as file_reviews_test:
    for line in file_reviews_test:
       (key, review) = line[:20], line[21:]
       test_text[key] = review


for key in test_text:
    test_case = test_text[key].split()
    test_case = [token.lower() for token in test_case]
   # test_case = [token.translate(None, string.punctuation) for token in test_case]


    prob_positive = math.log10(float(prior_prob_positive))
    for itr in range(1,len(test_case)):
        if(consolidated_class_prob.has_key(test_case[itr])):
            prob_positive +=  math.log10(float(consolidated_class_prob[test_case[itr]][0]))

    #print prob_positive

    prob_negative = math.log10(float(prior_prob_negative))

    for itr in range(1,len(test_case)):
        if(consolidated_class_prob.has_key(test_case[itr])):
            prob_negative +=  math.log10(float(consolidated_class_prob[test_case[itr]][1]))

    #print prob_negative

    prob_truthful = math.log10(float(prior_prob_truthful))

    for itr in range(1,len(test_case)):
        if(consolidated_class_prob.has_key(test_case[itr])):
            prob_truthful +=  math.log10(float(consolidated_class_prob[test_case[itr]][2]))

    #print prob_truthful



    prob_deceptive = math.log10(float(prior_prob_deceptive))

    for itr in range(1,len(test_case)):
        if(consolidated_class_prob.has_key(test_case[itr])):
            prob_deceptive +=  math.log10(float(consolidated_class_prob[test_case[itr]][3]))

    #print prob_deceptive


    if (prob_truthful > prob_deceptive):
        decision = key + " truthful"

    else:
        decision = key + " deceptive"


    if(prob_positive > prob_negative):
        decision += " positive"
    else:
        decision += " negative"

    with open("hw2-data-corpus/nboutput.txt","a") as file_decision:
     file_decision.write(decision + "\n")
