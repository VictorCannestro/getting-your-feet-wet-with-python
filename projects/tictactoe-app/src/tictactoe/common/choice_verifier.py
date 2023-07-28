def decide_from(available_decisions: tuple) -> str:
    yes, no = available_decisions
    player_input = input(f"Would you like to play again? Enter [{yes}|{no}] ")
    while player_input not in available_decisions:
        print(f"Please enter either [{yes}|{no}]")
        player_input = input(f"Would you like to play again? Enter [{yes}|{no}] ")    
    return player_input



if __name__ == "__main__": 
    print("Working inside ChoiceVerifier")