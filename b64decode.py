from base64 import b64decode

# with open('hefei.txt', 'r', encoding='utf-8') as f:
#     txt = f.readlines()
#     for c in txt:
#         print(c)
code = ['Q39fJw==','asOpw6EV','w6dqw7HCjA==','GBvCrsO9','AU3CjcOJ','G8KVw4XCow==']

for c in code:
    string = b64decode(c).decode('utf8')
    print(string)