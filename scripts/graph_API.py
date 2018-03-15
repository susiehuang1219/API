# A script to return and update meta data for facebook users using Graph API
"""
Created: Feb 2015
@author: shuang

"""
import json
import httplib
import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

app_id = 'xxxxx' # hide my application id
app_secret = 'xxxxxxxxxxxxxxxxx'

id_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

conn = httplib.HTTPSConnection('graph.facebook.com')

for user_id in id_file:
    user_id = user_id.rstrip()
    if user_id != '':
        conn.request('GET', '/' + user_id + '?access_token='+app_id+'|'+app_secret)
        http_reply = conn.getresponse()
        json_object = json.load(http_reply)
        print user_id
        # Type = 0 : User
        # Type = 1 : Non-User
        type = 0
        category = 'People'
        if 'first_name' in json_object.keys():
            type = 1
        elif 'category' in json_object.keys():
            type = 3
            category = json_object['category']
        try:
            urlname = json_object['name']  
        except KeyError:
            type = -1
            category = 'error'
        output_line = '%s\t%d\t%s\n' % (user_id, type, category)
        output_file.write(output_line)

conn.close()
id_file.close()
output_file.close()