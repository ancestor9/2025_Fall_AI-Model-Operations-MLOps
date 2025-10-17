# file = open('dog_breeds.txt')
# print(file.read())
# file.close()

# reader = open('dog_breeds.txt')
# # try:
# #     # Further file processing goes here
# for i in range(3):
#     print(reader.readline())
    
# # finally:
# #     reader.close()

with open('dog_breeds.txt') as reader:
    for i in range(3):
        print(reader.readline())
    # Further file processing goes here
    
file = open('dog_breeds.txt', 'wb')
print(type(file))
#<class '_io.TextIOWrapper'>