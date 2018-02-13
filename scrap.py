import requests
import csv
import json
import sys


# get user_token info from user
user_token = input("Welcome to the GroupMe-Multi-Add script!\n\
Please refer to the written documentation for in depth instructions.\n\
To begin with, please enter your User token: ")

# send request to GroupMe's API to get back a list of names of all groups the user is in.
base = "https://api.groupme.com/v3"
query = base + "/groups?omit='memberships'&token=%s" % user_token
r1 = requests.get(query).json()


def checkValidToken():
	return

def getListOfGroupNames(api_response):
	list_of_group_names = []
	json_groups = api_response["response"]
	for group in json_groups:
		list_of_group_names.append(group["name"])
	return list_of_group_names

def outputFormattedList(list_output):
	return "".join(["   " + str(name) + "\n" for name in list_of_group_names])



list_of_group_names = getListOfGroupNames(r1)
# formatted_list_of_group_names = '\n '.join(list_of_group_names)
formatted_list_of_group_names = outputFormattedList(list_of_group_names)
# choose what group you are targeting
group_name = input("Choose the group name from the following list you are targeting:\n"\
 	+ formatted_list_of_group_names +
 	"Target: ")

def getGroupID(api_response, group_name):
	json_groups = api_response["response"]
	for group in json_groups:
		if group["name"] == group_name:
			return group["group_id"]
	return ValueError("That group does not exist.")

group_id = getGroupID(r1, group_name)

print(group_id)

