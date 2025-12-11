def test_trial(cards_list, community_cards_list, total_players, num_simulations):
    # Ensure the 'pied_poker' package is installed before running this script
    import pied_poker as pp
    import numpy as np
    np.random.seed(420)

    # 1. Correctly create your player (p1) from the list of card strings
    p1 = pp.Player('You', pp.Card.of(cards_list[0]), pp.Card.of(cards_list[1]))

    # 2. Correctly create the list of community cards from the list of card strings
    community_cards = [pp.Card.of(card_str) for card_str in community_cards_list]

    # 3. Correctly determine the number of opponents and create them
    num_opponents = total_players - 1
    opponents = {f'p{i}': pp.player(f'Player {i+1}') for i in range(num_opponents)}

    # 4. Initialize the simulator with ALL players
    simulator = pp.PokerRound.PokerRoundSimulator(
        community_cards=community_cards,
        players=[p1, *opponents.values()],
        total_players=total_players # Use the integer argument directly
    )
    
    print("Simulator created successfully.")

    simulation_result = simulator.simulate(n=num_simulations, n_jobs=1)
    return simulation_result