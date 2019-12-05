import pandas as pd
import matplotlib.pyplot as plt

def plot_results(
    df     : pd.DataFrame,
    *args
) -> None:
    colors = []
    
    if len(args) == 1:
        colors = ['r']
    else:
        colors = ['r','g']
        
    fig = plt.figure(figsize=(26,7))

    x_vars = ["NGI","EI","WI","Site_EUI"]
    
    for x_var, i in zip(x_vars, range(1,5)):
        ax = plt.subplot(1,4,i)
        ax.xaxis.set_major_locator(plt.MaxNLocator(6))
        ax.set_xlabel(x_var,fontsize=15)
        
        df.plot(x=x_var,
                y='GHGI',
                ax=ax,
                kind='scatter',
                color='b',
                fontsize=14,
                label='y_test',
                s=15)
        
        for arg, color in zip(args, colors):
            df.plot(x=x_var,
                    y=arg,
                    ax=ax,
                    kind='scatter',
                    color=color,
                    fontsize=14,
                    label=arg,
                    s = 14,
                    alpha=0.4)
            
        ax.set_ylabel('GHGI',fontsize=15)
        ax.legend(loc=4, fontsize=14)
    
    plt.tight_layout()