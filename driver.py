
# ---------------------------------------------------------------- #
def displayEligibleCandidates(candidatesToDisplay: dict) -> None:
    """
    This method displays a complete list of all eligible candidates and their IDs
    :param candidatesToDisplay: dictionary containing candidate IDs and names.
    :return: None
    """
    for keys, values in candidatesToDisplay.items():
        separator = 40 - (11 + len(values))
        print(f"|  {keys}  >>  {values}{' ' * separator}|")

def voteForCandidate(candidateVotingFor: str, votes: dict[str, int]) -> None:
    """
    This method allows the user to vote for a candidate and updates the vote count
    :param candidateVotingFor: ID of the candidate the user wishes to vote for
    :param votes: dictionary containing candidate IDs and their corresponding votes
    :return: None
    """
    if candidateVotingFor in allCandidates.keys():
        votes.update({candidateVotingFor: votes[candidateVotingFor] + 1})  # update the vote count for the candidate
        print(f"Your ballot has been successfully casted for: {allCandidates[candidateVotingFor]} bearing Candidate ID: {candidateVotingFor}")

def listOfEligibleCandidates(candidatesToAdd: str, allCandidates: dict[str, str], votes: dict[str, int]) -> None:
    """
    This method adds new candidates to the voting system
    :param candidatesToAdd: string containing new candidates' information
    :param allCandidates: dictionary containing all candidates and their IDs
    :param votes: dictionary containing candidate IDs and their corresponding votes
    :return: None
    """
    for x in candidatesToAdd.split(';'):
        ids_names = x.split(',')
        allCandidates.update({ids_names[0].strip(): ids_names[1].upper().strip()})  # add the candidates to the dictionary
        votes.update({ids_names[0].strip(): 0})  # set all votes for each candidate to zero

def displayElectoralResults(votes: dict[str, int], allCandidates: dict[str, str]) -> None:
    """
    This method displays a complete ordered-list list of the electoral results
    :param votes: dictionary containing candidate IDs and their corresponding votes
    :param allCandidates: dictionary containing all candidates and their IDs
    :return: None
    """
    sorted_candidates: dict[str, int] = dict(sorted(votes.items(), key=lambda item: item[1], reverse=True))
    position: int = 0; same_value: int = -1

    for key, value in sorted_candidates.items():
        separator1: int = 8 - len(str(position))
        separator2: int = 13 - len(str(value))
        separator3: int = 2 - len(str(key))
        separator4: int = 30 - len(str(allCandidates[key]))

        if not value == same_value:
            position += 1
        print(f"| {' ' * separator1}{position} | {' ' * separator2}{value} | {' ' * separator3}{key} | {allCandidates[key]}{' ' * separator4} |")
        same_value = value
# ---------------------------------------------------------------- #

if __name__ == '__main__':

    # variables
    allCandidates: dict[str, str] = {}
    votes: dict[str, int] = {}

    # welcome message
    print("Welcome to the Simple Electronic Voting System (SEVS):")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # prompts the user to enter a string collection of electoral candidates
    candidates: str = input("\nPlease enter a String collection electoral candidates below:\n")
    listOfEligibleCandidates(candidates, allCandidates, votes)

    while True:
        # displays several codes with its respective description
        print("********************************")
        print("| Code >> Description          |")
        print("********************************")
        print("|  1   >> Display candidates   |")
        print("|  2   >> Vote a candidate     |")
        print("|  3   >> Add new candidate(s) |")
        print("|  4   >> Display results      |")
        print("|  0   >> End SEVS             |")
        print("********************************")
        prompt = input("\nEnter a code, from the aforementioned, that corresponds to your task: ")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "1":
            print("*****************************************")
            print("| ID >> Candidate's Name                |")
            print("*****************************************")
            displayEligibleCandidates(allCandidates)
            print("*****************************************")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "2":
            candidateVotingFor = input("\nPlease enter the ID of the candidate you wish to vote for: ")
            voteForCandidate(candidateVotingFor, votes)

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "3":
            newCandidates: str = input("\nPlease enter a String collection of the NEW electoral candidates below:\n")
            listOfEligibleCandidates(newCandidates, allCandidates, votes)
            print("Successfully added a NEW set of electoral candidates to the Simple Electronic Voting System (SEVS).")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "4":
            print("******************************************************************")
            print("| Position | Votes/BallotS | ID | Candidate's Name               |")
            print("******************************************************************")
            displayElectoralResults(votes, allCandidates)
            print("******************************************************************")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "0":
            break

    # closing message
    print("Thank you for using our Simple Electronic Voting System (SEVS).", end="")
