import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os



logdir = 'logs/256_net_small_lrs'
multiconfig = {}

for e, fname in enumerate(os.listdir(logdir)):
    if os.path.isdir(f"{logdir}/{fname}"):
        config = json.load(open(f'{logdir}/{fname}/parameters.json', 'r'))
        for key, val in config.items():
            if e == 0:
                multiconfig[key] = [str(val)]
            elif not str(val) in multiconfig[key]:
                multiconfig[key].append(str(val))

params_to_track = [key for key, val in multiconfig.items() if len(val) > 1]
print(params_to_track)

fig, axs = plt.subplots(1,1, figsize=(20, 8))
colors = plt.cm.get_cmap('tab20c').colors
axs.set_prop_cycle(color=colors)

for fname in os.listdir(logdir):
    if os.path.isdir(f"{logdir}/{fname}"):
        params = json.load(open(f'{logdir}/{fname}/parameters.json', 'r'))
        df = pd.read_csv(f'{logdir}/{fname}/results.csv', delimiter=',')
        axs.plot(df.iloc[:]['eval_return_mean'].values, label={key: str(val) for key, val in params.items() if key in params_to_track})

axs.legend(loc='center left', bbox_to_anchor=(0.8, 0.3))
plt.grid()
plt.savefig(f"{logdir}/summary_plot.png", dpi=400)
plt.close()
