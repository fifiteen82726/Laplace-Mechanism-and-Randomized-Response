## Exercise1

### Compare Randomized Response and Laplace Mechanism

#### 1. Datasset Source: [Adult dataset](https://archive.ics.uci.edu/ml/datasets/Adult )
#### 2 .Query: Threshold Query: 
To find how many adult whos income are `<= 50k` and education number `> 13`
#### 3. Goal: 
Use graph to show the difference between Laplace Mechanism and Randomized Response. 
In normal case, the `Laplace` result will be better than `Randomized Respose` result.

### Test
```
python exercise1/excecise_1.py
```
### Result 
N = `1000`, Epsilon = `0.5`, BETA = `0.05`. As you can see, the the spots in`Laplace` are closer with each others spot than `Randomized Respose`.

### Test
<img width="641" alt="screen shot 2018-11-01 at 1 54 52 am" src="https://user-images.githubusercontent.com/6240395/47835523-b2c7fe80-dd7a-11e8-81fa-3b19b7c9d3ea.png">
