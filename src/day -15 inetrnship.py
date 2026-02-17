#topic 1
favorable = 1
total_outcomes = 6
probability = favorable / total_outcomes

print("probability of rolling a 4 on a fair die =",probability)
print("-" * 50)


#independent events example
#topic 2
p_rain = 0.3
p_traffic = 0.2

p_both = p_rain* p_traffic
print("Probability of Rain =", p_rain)

print("Probability of Traffic =", p_traffic)
print("Probability of both Rain AND Traffic =", p_both)

print("-" * 50)

#conditional probability
p_A_and_B = 0.1
p_B = 0.4
p_A_given_B = p_A_and_B / p_B
print(p_A_given_B)

# Bayes' theorem example
p_disease = 0.01
p_positive_given_disease = 0.9
p_positive = 0.05

p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive
print(p_disease_given_positive)

#Task 1
import random

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Experimental Probability of sum = 7:", experimental_probability)

#Task 2
# Independent events
P_heads = 1/2
P_six = 1/6
P_both = P_heads * P_six
print("Probability of Heads AND rolling a 6:", P_both)
# Dependent events (without replacement)
P_first_red = 5/10
P_second_red_given_first = 4/9
P_both_red = P_first_red * P_second_red_given_first
print("Probability both marbles are Red:", P_both_red)
# Simple conditional probability example
count_san = 100
count_san_francisco = 70
P_francisco_given_san = count_san_francisco / count_san
print("P(Francisco | San) =", P_francisco_given_san)

#Task 3
# Given probabilities
P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

# Step 1: Total probability of "Free"
P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)

# Step 2: Bayes' Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)