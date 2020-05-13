from scipy.stats import poisson

#média 2 acidentes por dia
#prob de acontecerem 3 acidentes por dia

prob3 = poisson.pmf(3, 2)

#prob de acontecerem 3 ou menos

prob3menos = poisson.cdf(3, 2)

#prob de acontecerem mais de 3

prob3mais = poisson.sf(3, 2)


