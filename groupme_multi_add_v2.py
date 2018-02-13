import requests
import csv
import json
import sys

# FUNCTIONS TO SET UP ENVIRONMENT FOR YANGZI'S SCRIPT
def checkValidToken():
	return

def getListOfGroupNames(api_response):
	list_of_group_names = []
	json_groups = api_response["response"]
	for group in json_groups:
		list_of_group_names.append(group["name"])
	return list_of_group_names

def outputFormattedList(list_output):
	return "".join(["   " + str(name) + "\n" for name in list_output])

def getGroupID(api_response, group_name):
	json_groups = api_response["response"]
	for group in json_groups:
		if group["name"] == group_name:
			return group["group_id"]
	return ValueError("That group does not exist.")

# YANGZI'S FUNCTIONS
def formatNumbers(number):
    import re
    rep = {"(": "", ")": "", " ": ""}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    formattedNum = pattern.sub(lambda m: rep[re.escape(m.group(0))], number)
    return formattedNum

def csvToJson(name_of_csv, lines_to_skip):
    with open(name_of_csv, 'rt') as csvfile:
        members = csv.reader(csvfile)
        for _ in range(int(lines_to_skip)):
            members.next()
        members_data = []
        for member in members:
            if member[0] == "":
                break
            print(members)
            number = formatNumbers(member[0])
            new_groupme_member = {"nickname": member[0], "phone_number": number}
            members_data.append(new_groupme_member)
        wrapper = {"members": members_data}
        json_members = json.dumps(wrapper)
        return json_members

def add_members(api_url, group_id, access_token, name_of_csv, lines_to_skip):
    json_members = csvToJson(name_of_csv, lines_to_skip)
    requests.post(api_url + "/groups/" + group_id + "/members/add" +
                  "?token=" + access_token, data=json_members)


# RUNS EVERYTHING
def main():

    # get user_token info from user
	user_token = input("Welcome to the GroupMe-Multi-Add script!\n" +
	"Please refer to the written documentation for in depth instructions.\n" +
	"To begin with, please enter your User token: ")

	# send request to GroupMe's API to get back a list of names of all groups the user is in.
	api_url = "https://api.groupme.com/v3"
	query = api_url + "/groups?omit='memberships'&token=%s" % user_token
	r1 = requests.get(query).json()
	list_of_group_names = getListOfGroupNames(r1)
	formatted_list_of_group_names = outputFormattedList(list_of_group_names)
	
	# choose what group you are targeting
	group_name = input("Choose the group name from the following list you are targeting:\n" + 
	 	formatted_list_of_group_names +
	 	"Target: ")
	group_id = getGroupID(r1, group_name)

	name_of_csv = input("Name of your csv file: ")
	lines_to_skip = input("Number of lines before the first member of your roster: ")

	add_members(api_url, group_id, user_token, name_of_csv, lines_to_skip)

if __name__ == "__main__":
    main()

