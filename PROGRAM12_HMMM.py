# Q12. Hidden Markov Model - Viterbi Algorithm

# Hidden states
states = ["Sunny", "Rainy"]

# Observation sequence
observations = ["Walk", "Shop", "Clean"]

# Initial probabilities
# Probability of starting with Sunny or Rainy
initial = {
    "Sunny": 0.6,
    "Rainy": 0.4
}

# Transition probabilities
# Probability of moving from one state to another
transition = {
    "Sunny": {
        "Sunny": 0.7,
        "Rainy": 0.3
    },
    "Rainy": {
        "Sunny": 0.4,
        "Rainy": 0.6
    }
}

# Emission probabilities
# Probability of observing an activity from a state
emission = {
    "Sunny": {
        "Walk": 0.6,
        "Shop": 0.3,
        "Clean": 0.1
    },
    "Rainy": {
        "Walk": 0.1,
        "Shop": 0.4,
        "Clean": 0.5
    }
}

# This list stores probability values at each time step
viterbi = []

# This list stores previous best states
path = []

# -------------------------------
# Step 1: First observation
# -------------------------------

first_obs = observations[0]

first_probs = {}

for state in states:
    # probability = initial probability * emission probability
    first_probs[state] = initial[state] * emission[state][first_obs]

viterbi.append(first_probs)

print("For observation:", first_obs)
print(first_probs)
print()

# -------------------------------
# Step 2: Remaining observations
# -------------------------------

for i in range(1, len(observations)):

    current_obs = observations[i]

    current_probs = {}
    current_path = {}

    for current_state in states:

        best_prob = 0
        best_previous_state = ""

        for previous_state in states:

            # Formula:
            # previous probability * transition probability * emission probability
            prob = (
                viterbi[i - 1][previous_state]
                * transition[previous_state][current_state]
                * emission[current_state][current_obs]
            )

            # Choose maximum probability
            if prob > best_prob:
                best_prob = prob
                best_previous_state = previous_state

        # Store best probability for current state
        current_probs[current_state] = best_prob

        # Store from which previous state we came
        current_path[current_state] = best_previous_state

    viterbi.append(current_probs)
    path.append(current_path)

    print("For observation:", current_obs)
    print(current_probs)
    print("Previous best states:", current_path)
    print()

# -------------------------------
# Step 3: Find final best state
# -------------------------------

last_probs = viterbi[-1]

if last_probs["Sunny"] > last_probs["Rainy"]:
    last_state = "Sunny"
else:
    last_state = "Rainy"

# -------------------------------
# Step 4: Backtracking
# -------------------------------

best_sequence = [last_state]

# Go backwards and find previous best states
for i in range(len(path) - 1, -1, -1):
    previous_state = path[i][best_sequence[0]]
    best_sequence.insert(0, previous_state)

# -------------------------------
# Final output
# -------------------------------

print("Observation sequence:", observations)
print("Most likely hidden state sequence:", best_sequence)