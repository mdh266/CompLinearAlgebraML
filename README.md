# Numerical Linear Algebra In Machine Learning
-----------------------------

In this blogpost we'll go over applications of numerical linear algebra in machine learning starting out with regression and getting to modern recommender systems! Numerical linear algebra (and numerical analysis more generally) was one of thoses courses that I learned, thought was boring and never wanted to study again. Only with maturity that comes with age (and a PhD) was I able to understand and appreciate the true power of numerical linear alebra.  Infact *understanding (distribued) linear algebra is probably one of the most important and useful tools I have ever learned.* It is the backbone by which many machine learning algorithms work.  Specifically I go over how numerical linear algebra is used for, 

1. Linear Regression with the Cholesky Decomposition 
2. Linear Regression with the Singular Value Decomposition (SVD)
3. Ridge Regression with the SVD
4. Alternating Least Squares for Recommendation Systems

Using only Pandas, Numpy and SciPy. 


## Dependencies
-------------------------
[Pandas 0.25.3](https://pandas.pydata.org/)

[NumPy 1.17.3](https://numpy.org/)

[SciPy 1.3.1](https://www.scipy.org/)

[Seaborn 0.9.0](http://seaborn.pydata.org/)


Install depenceies by creating conda environment with:

    conda create env -f environment.yml
    
See how to do this all on Google Cloud [here](https://github.com/mdh266/JupyterOnGCP)
    
