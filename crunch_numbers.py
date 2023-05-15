import pyrankvote
from pyrankvote import Candidate, Ballot
import csv
import sys

def main():
	if len(sys.argv) != 2:
		print(f"Usage: {sys.argv[0]} votes_file", file=sys.stderr)
		sys.exit(1)

	candidates = {}
	ballots = []
	
	with open(sys.argv[1]) as votes_file:
		reader = csv.DictReader(votes_file)
		for row in reader:
			ballot = []
			for field in row:
				idx = field.find("[")
				if idx > 0:
					candidate = row[field]
					rank = int(field[idx+1:-1])
					if candidate not in candidates:
						candidates[candidate] = Candidate(candidate)
					ballot.append({ "candidate": candidates[candidate], "rank": rank })
			ballots.append(list(map(lambda v: v["candidate"], sorted(ballot, key=lambda v: v["rank"]))))
		for c in candidates:
			print(f"candidate detected: {c}")
		print(f"found {len(ballots)} ballots")

		for b in ballots:
			for c in b:
				print(f"{c}: {type(c)}")

		prepared_ballots = list(map(lambda b: Ballot(ranked_candidates=b), ballots))

		election_result = pyrankvote.instant_runoff_voting(candidates, prepared_ballots)

		print(election_result)

if __name__ == "__main__":
	main()

