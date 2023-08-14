import gym
import time
import numpy as np

# Initialize the Taxi-v3 environment.
env = gym.make('Taxi-v3')               

def qlearn(gamma=0.95):
    """
    Train a Q-learning agent on the Taxi-v3 environment.
    
    Parameters:
    - gamma: Discount factor for future rewards.
    
    Returns:
    - Q: The learned Q-table.
    """
    # Initialize the Q-table with zeros.
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    num_episodes = 1000         # Number of episodes for trainin
    
    # Training loop
    for i in range(num_episodes):
        done = False
        tuple_state = env.reset()
        state = tuple_state[0]

        # Episode loop
        while not done:
            # Add noise to the Q-values to encourage exploration.
            value_noise = np.random.randn(env.action_space.n)*(1./(i+1))

            # Choose action based on Q-values and noise
            action = np.argmax(Q[state] + value_noise)

            # Take the chosen action in the environment.
            next_state, reward, done, _, info = env.step(action)

            # Update the Q-value based on the received reward and the highest Q-value of next state
            Q[state,action] = reward + gamma * np.max(Q[next_state])
            state = next_state

    return Q

Q = qlearn()

# Creating a new environment instance to visualize the agent's performance using the learned Q-values
env_human = gym.make('Taxi-v3', render_mode = 'human')

print("\nVisualizing the learned Q-values in action:")

tuple_state = env_human.reset()
state = tuple_state[0]
done = False

while not done:
    action = np.argmax(Q[state])
    next_state, _, done, _, _ = env_human.step(action)
    env_human.render()
    state = next_state
    time.sleep(0.5)



