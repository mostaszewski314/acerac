import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os
import sys

# logdir = 'logs/ANT_final_3_seed/'

def plot_single_runs(logdir):
    multiconfig = {}
    e = 0
    for fname in os.listdir(logdir):
        if os.path.isdir(f"{logdir}/{fname}"):
            config = json.load(open(f'{logdir}/{fname}/parameters.json', 'r'))
            for key, val in config.items():
                if e == 0:
                    multiconfig[key] = [str(val)]
                elif not str(val) in multiconfig[key]:
                    multiconfig[key].append(str(val))
            e += 1

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

def plot_averaged_runs(logdir):
    fig, axs = plt.subplots(1, 1, figsize=(20, 8))
    results = []

    for fname in os.listdir(logdir):
        if os.path.isdir(f"{logdir}/{fname}"):
            # axs.plot(df.iloc[:]['eval_return_mean'].values)
            df = pd.read_csv(f'{logdir}/{fname}/results.csv', delimiter=',')
            results.append(df.iloc[:]['eval_return_mean'].values)
    results = np.array(results)
    mean, std = np.mean(results, axis=0), np.std(results, axis=0)
    print(mean.shape, std.shape)

    axs.plot(np.arange(len(mean)), mean)
    axs.fill_between(np.arange(len(mean)), mean - std, mean + std, alpha=0.3)
    plt.grid()
    plt.savefig(f"{logdir}/average_plot.png", dpi=400)
    plt.close()

if __name__ == "__main__":
    args = sys.argv[1:]
    logdir = args[0]
    print(args)
    if int(args[1]) == 1:
        plot_averaged_runs(logdir)
    else:
        plot_single_runs(logdir)
    
