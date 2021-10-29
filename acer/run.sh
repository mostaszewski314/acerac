# Pendulum
python3 acer/run.py --algo acer --env_name Pendulum-v0 --gamma 0.95 --lam 0.9 --b 3 --c0 0.3 --c 10 --actor_lr 0.001 --critic_lr 0.002 --actor_layers 20 --critic_layers 50 --memory_size 1000000 --num_parallel_envs 10  --actor_beta_penalty 0.1 --batches_per_env 10 --max_time_steps 2000000

# Ant Acer
python3 acer/run.py --algo acerac --env_name -v0 --gamma 0.99 --lam 0.9 --b 2 --c0 0.1 --c 10 --actor_lr 0.00003 --critic_lr 0.00006 --actor_layers 256 256  --critic_layers 256 256 --memory_size 1000000 --num_parallel_envs 10 --actor_beta_penalty 0.001 --batches_per_env 10 --num_evaluation_runs 5  --std 0.4  --max_time_steps 3000000 --tau 4 --alpha 0.5

# Half-Cheetah AcerAC from github
python3 acer/run.py --algo acerac --env_name HalfCheetahBulletEnv-v0 --gamma 0.99 --lam 0.9 --b 2 --c0 0.1 --c 10 --actor_lr 0.00003 --critic_lr 0.00006 --actor_layers 256 256  --critic_layers 256 256 --memory_size 1000000 --num_parallel_envs 10 --actor_beta_penalty 0.001 --batches_per_env 10 --num_evaluation_runs 5  --std 0.4  --max_time_steps 3000000 --tau 4 --alpha 0.5

# Ant ACER
python3 acer/run.py --algo acer --env_name AntBulletEnv-v0 --gamma 0.99 --lam 0.9 --b 2 --c 10 --actor_lr 1e-5 --critic_lr 1e-5 --actor_layers_mean 256 256 --actor_layers_std 64 64  --critic_layers 256 256 --memory_size 1000000 --num_parallel_envs 10 --actor_beta_penalty 0.001 --batches_per_env 10 --num_evaluation_runs 5 --max_time_steps 3000000

# Every 30000 timesteps evaluation -- average over 5 runs
# 5 random seeds
# gamma = 0.99
# std = 0.3
# lam = 0.9
# b = 2
# memory size = 1e6
# minibatch = 256
# target update interval = 1
# gradient steps = 1
# learning start = 1e3
# actor_lr 1e-5
# critic_lr 1e-5 
# actor_layers 256 256
# critic_layers 256 256
# batches_per_env = 10
# num_parallel_envs = 10

# c0?
# c?
# actor_beta_penalty ?
# tau ?
# alpha ?