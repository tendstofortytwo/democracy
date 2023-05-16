import pyrankvote
from pyrankvote import Candidate, Ballot
import csv
import sys

def main():
	if len(sys.argv) != 4:
		print(f"Usage: {sys.argv[0]} votes_file election_name no_of_seats", file=sys.stderr)
		sys.exit(1)

	candidates = {}
	ballots = []
	seat_count = int(sys.argv[3])
	
	with open(sys.argv[1]) as votes_file:
		reader = csv.DictReader(votes_file)
		for row in reader:
			ballot = []
			for field in row:
				idx = field.find("[")
				if idx > 0:
					electionName = field[:idx].lower()
					if sys.argv[2].lower() not in electionName:
						continue
					candidate = row[field]
					if candidate == "":
						continue
					rank = int(field[idx+1:-1])
					if candidate not in candidates:
						candidates[candidate] = Candidate(candidate)
					ballot.append({ "candidate": candidates[candidate], "rank": rank })
			ballots.append(list(map(lambda v: v["candidate"], sorted(ballot, key=lambda v: v["rank"]))))

	candidates = candidates.values()
	ballots = list(map(lambda b: Ballot(ranked_candidates=b), ballots))

	print(f"found {len(ballots)} ballots and {len(candidates)} candidates")

	election_result = pyrankvote.single_transferable_vote(candidates, ballots, number_of_seats=seat_count)

	print(election_result)

if __name__ == "__main__":
	main()

