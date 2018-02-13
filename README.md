# GroupMe-Multi-add

I’m updating GroupMe-Multi-Add (originally written by Y.H.) to accommodate for changes within GroupMe’s public facing UI, as well as make it more intuitive to use for less tech-oriented people.

## Changes Made

1. GroupMe’s UI now makes it impossible to find the group_id of a chat without using the API. Consequently, I auto-grab the correct GroupMe group_id using the name of the group and calls to the API instead.
2. Got rid of global variables and implemented a terminal prompting system, which lessens the likelihood of human error.
3. The script is now written in Python 3.

## Purpose

GroupMe-Multi-add bulk adds a list of members from a .csv file to a GroupMe group.

## Installation
1. Install Homebrew if you haven’t already. Run the following command in the terminal:
'/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'
2. Install wget: 'brew install wget'
3. Download the Miniconda installer. Miniconda is a lightweight python environment, which automatically includes python 3: 'wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh'
4. Run the Miniconda installer: 'bash Miniconda3-latest-MacOSX-x86_64.sh'
5. Delete the Miniconda installer: 'rm ~/Miniconda3-latest-MacOSX-x86_64.sh'
6. Edit PATH variable and store it: 'echo export PATH='~/miniconda3/bin:$PATH' >> ~/.profile'
7. Activate the changes: 'source ~/.profile'
8. Install python environment: 'conda install anaconda'
9. Update python packages: 'conda update --all'
10. In your terminal, run 'git clone https://github.com/Pyrinox/GroupMe-Multi-Add-v2.0.git' in the directory you would like to keep the script in.


## Usage

To use this script, you will need to do the following:

1. Create a csv file that contains a single column of phone numbers. Save it in the same directory that the python file is in. 

2. Get an access token by creating a [GroupMe account](https://web.groupme.com/signup). If you already have an account, directly sign into the [developer's portal](https://dev.groupme.com/session/new). Once you're logged in, you should be able to see the "Access Token" button located at the top right of the navigation menu (to the left of your account name). Copy the token.

3. Finally, in your terminal, cd to the directory containing your .csv file and python script. Then type `python groupme_multi_add_v2.py` and press Enter. Follow all the prompts.

4. Congratulations, you've just added your entire roster to your GroupMe group.


## API Reference

[GroupMe API](https://dev.groupme.com/docs/v3)
