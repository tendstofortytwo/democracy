# democracy

## how to use

1. setup a google form with a single multiple-choice grid question for votes, where the rows are rankings (integers [1, N]), and columns are candidate names. from the three dot menu, enable "limit to one response per column". you can add other fields to the form but they will be ignored. do not add other multiple-choice grid questions or any fields with `[]` brackets in the name.

2. after collecting votes, export the data from the form as a CSV.

3. do this (one-time setup):

```
git clone https://github.com/tendstofortytwo/democracy
cd democracy
python3 -m venv venv
pip3 -r requirements.txt
```

4. do this every time you want to run an election, using the CSV generated as above:

```
cd democracy
python3 crunch_numbers.py your_file.csv
```

## license

MIT license; see LICENSE.md.
