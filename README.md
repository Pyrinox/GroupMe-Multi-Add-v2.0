# GroupMe-Multi-add

I'm updating GroupMe-Multi-add (originally written by Yangzi) to accommodate for changes within GroupMe's public facing UI, and make it more intuitve to use.

GroupMe-Multi-add bulk adds a list of members from a .csv file to a GroupMe group.

## Installation

* In your terminal, run `git clone https://github.com/yangzihe/GroupMe-Multi-add.git` in the directory you would like to keep this script in.

* Install the Python Requests Library from [here](http://docs.python-requests.org/en/master/user/install/#install).

## Usage

To use this script, you will need to do the following:

1. Create a csv file that contains a single column of phone numbers. Save it in the same directory that the python file is in. 

2. Access Token. To get an access token, create a [GroupMe account](https://web.groupme.com/signup). If you already have an account, directly sign into the [developer's portal](https://dev.groupme.com/session/new). Once you're logged in, you should be able to see the "Access Token" button located at the top right of the navigation menu (to the left of your account name). Copy the token.

3. Finally, in your terminal, cd to the directory containing your .csv file and python script. Then type `python groupme_multi_add.py` and press Enter. Follow all the prompts.

4. Congratulations, you've just added your entire roster to your GroupMe group.


## API Reference

[GroupMe API](https://dev.groupme.com/docs/v3)
