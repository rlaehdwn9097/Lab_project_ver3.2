# DQN main
# coded by St.Watermelon

from dqn_learn import DQNagent
import config as cf
def main():
    max_episode_num = 30
    agent = DQNagent()
    agent.train(max_episode_num)
    agent.plot_result()
    agent.plot_cache_hit_result()
    agent.plot_redundancy_result()

if __name__=="__main__":
    main()
    