# democracy

## how to use

1. setup a google form with a multiple-choice grid question for votes for each election, where the rows are rankings (integers [1, N]), and columns are candidate names. from the three dot menu, enable "limit to one response per column". you can add other fields to the form but they will be ignored. make sure that each question name for the ballot has a unique word in it -- not shared by any other questions -- which will serve as the ballot name. eg. you can append each question with `(ballot 1)`, `(ballot 2)`, and so on. do not use `[]` square brackets in question names as they are used by google forms to distinguish choices.

2. after collecting votes, export the data from the form as a CSV.

3. do this (one-time setup):

```
git clone https://github.com/tendstofortytwo/democracy
cd democracy
python3 -m venv venv
source venv/bin/activate
pip3 -r requirements.txt
```

4. do this every time you want to run an election, using the CSV generated as above:

```
cd democracy
source venv/bin/activate
python3 crunch_numbers.py your_file.csv "name of election" 2    # assuming you want to elect two people
```

## license

MIT license; see LICENSE.md.
