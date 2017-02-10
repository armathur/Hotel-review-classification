classified_label ={}
test_label = {}
total_positive = 0
true_positive = 0
true_negative = 0
false_negative = 0
false_positive = 0


with open("hw2-data-corpus/nboutput.txt", "r") as file_decision:
    for line in file_decision:
        (key, label1, label2) = line.split()
        classified_label[key] = label1, label2


# print classified_label



with open("hw2-data-corpus/test-labels.txt", "r") as file_labels:
    for line in file_labels:
       (key, label1, label2) = line.split()
       test_label[key] = label1, label2



for key in classified_label:
    if classified_label[key][1] == "positive":
        if classified_label[key][1] == test_label[key][1]:
            true_positive += 1
        else:
            false_positive += 1

precision =  true_positive/float(false_positive+true_positive)

print precision

for key in classified_label:
    if classified_label[key][1] == "negative":
        if classified_label[key][1] != test_label[key][1]:
            false_negative += 1
        else:
            true_negative += 1


recall = true_positive/ float(true_positive + false_negative)

print recall

f_one_score = 2*(precision*recall) / float(precision+recall)

print f_one_score

