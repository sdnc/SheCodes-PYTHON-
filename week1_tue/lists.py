sara_wishlist = ["shoes", "bag", "projector", "plane tickets", "jewelry"]

# indexing 

print("length: ", len(sara_wishlist))

print("index 0: ", sara_wishlist[0])
print("index -1: ", sara_wishlist[-1])
print("index 1 (inclusive) to 4 (exclusive): ", sara_wishlist[1:4])

print("*Add 'crypto' to index place 1*")
sara_wishlist[1] = 'crypto'
print("Entire wishlist: ", sara_wishlist)

sara_wishlist.append("yoga mat")
print("Entire wishlist after append: ", sara_wishlist)

sara_wishlist.extend(["books", "ipad", "couch"])
print("Entire wishlist after extend: ", sara_wishlist)

sara_wishlist.insert(1, "peanut butter")
print("Entire wishlist after insert: ", sara_wishlist)

sara_wishlist.pop()
sara_wishlist.pop(2)
print("Entire wishlist after pop: ", sara_wishlist)

sara_wishlist.remove("projector")
print("Entire wishlist after remove': ", sara_wishlist)

# sublists 

chilli_wishlist = [
['igloo'], # bed
['donut toy','tennis ball', 'crocodile toy'],# toys
['chicken', 'peanut butter'], # treats
['cardboard box', 'kong', 'dig mat'] # activity based toys
]

print(chilli_wishlist[2])
print(chilli_wishlist[2][1])
