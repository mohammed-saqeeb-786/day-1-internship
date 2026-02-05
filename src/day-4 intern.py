#task 1
 
#Goal: Practice dictionary creation, updating, and safe data retrieval using .get().
## Scenario: You are building a simple digital rolodex to store contact information.
#* Instructions:
    
    
#* Create a dictionary named contacts with at least three people. Each Key should be a name (String) and the Value should be their phone number (String or Int).

contacts={"saqeeb":"9353951993",
          "asif":"1234567890",
          "mutaheer":"8989898989"}

#adding

contacts["saif"]="5656565647"

#updating

contacts["saqeeb"]="4545456372"

#safe access

print(contacts.get("anushka","puri zindagi me nahi hai"))

#iteratitng

for a, b in contacts.items():
    print(f" contact {a} | phone: {b}")
    
    #task 2
     
   # create a row log (matlab ek waste type ka row banao)
#this is my raw log 
row_log=["ID01" ,"ID02", "ID01", "ID05", "ID02", "ID08","ID01"]

#creatingg a set named unique
unique_user=set(row_log)

#display the id(
print("this is the unique set of IDS",(unique_user))

#membership test
print("is ID05 present?","ID05" in row_log)

#the original list 
print("the length of the list is",len(row_log))
print("the length of the set is",len(unique_user))

#duplicates
duplicates = len(row_log) - len(unique_user)

#displaying
print(f"{duplicates} duplicates are removed")



#task3
#creating two sets
friend_a={"python","cooking","hiking", "movies"}
friend_b={"hiking", "gaming", "photography", "python"}

shared_interests =friend_a&friend_b
all_interest =friend_a|friend_b
unique_to_a =friend_a-friend_b

#displaying intersection
print("intersection of friend a and friend b are",shared_interests)

#displaying union 
print("union of friend a and friend b are ", all_interest)

#displaying difference
print("union of friend a and friend b are ",unique_to_a)

   
