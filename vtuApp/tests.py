# Python3 code to demonstrate
# convert dictionary string to dictionary
# using json.loads()
import json
import ast

# initializing string 
# test_string = '{"result":1,"msg":"Plans retrieved","plancount":11,"data":({"id":"79","text":"500MB - [30 Days Plan] - 100.00 "},{"id":"80","text":"1.00GB - [30 Days Plan] - 200.00 "},{"id":"81","text":"2.00GB - [30 Days Plan] - 400.00 "},{"id":"82","text":"3.00GB - [30 Days Plan] - 600.00 "},{"id":"83","text":"5.00GB - [30 Days Plan] - 1,000.00 "},{"id":"84","text":"10.00GB - [30 Days Plan] - 2,000.00 "},{"id":"85","text":"15.00GB - [30 Days Plan] - 3,000.00 "},{"id":"86","text":"20.00GB - [30 Days Plan] - 4,000.00 "},{"id":"87","text":"40.00GB - [30 Days Plan] - 8,000.00 "},{"id":"89","text":"75.00GB - [30 Days Plan] - 15,000.00 "},{"id":"90","text":"100.00GB - [30 Days Plan] - 20,000.00 "}]}'

test_string = '{"result":1,"msg":"Plans retrieved","plancount":11,"data":({"id":"79","text":"500MB - [30 Days Plan] - 100.00 "},{"id":"80","text":"1.00GB - [30 Days Plan] - 200.00 "},{"id":"81","text":"2.00GB - [30 Days Plan] - 400.00 "},{"id":"82","text":"3.00GB - [30 Days Plan] - 600.00 "},{"id":"83","text":"5.00GB - [30 Days Plan] - 1,000.00 "},{"id":"84","text":"10.00GB - [30 Days Plan] - 2,000.00 "},{"id":"85","text":"15.00GB - [30 Days Plan] - 3,000.00 "},{"id":"86","text":"20.00GB - [30 Days Plan] - 4,000.00 "},{"id":"87","text":"40.00GB - [30 Days Plan] - 8,000.00 "},{"id":"89","text":"75.00GB - [30 Days Plan] - 15,000.00 "},{"id":"90","text":"100.00GB - [30 Days Plan] - 20,000.00 "})}'
# printing original string 
print("The original string : " + str(test_string))

success_data_top_up = {'reset': True,
                       'result': 1,
                       'url': 'https://honourworld.ng/products/data-top-up',
                       'msg': 'Data top-up request has been received and will be processed shortly! '}


invalid_number = {'msg': 'This is not an MTN number'}

insufficient_bla = {'msg': 'You do not have sufficient credit in your wallet. Please top-up wallet first'}

if 'You do not have sufficient credit in your wallet. Please top-up wallet first' in insufficient_bla['msg']:
    print(True)




print(list(invalid_number.keys()).index('msg'))
# using json.loads()
# convert dictionary string to dictionary
res = ast.literal_eval(test_string)

# print result
print("The converted dictionary : " + str(res))