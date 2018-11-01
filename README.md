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



## Exercise2

### Compare
1. Exponatial Mechnism
2. Report One-sided  Noisy Arg-max algorithm
3. Randomized Response 
4. Laplace Mechanism

### Test
```
python exercise2/excecise_2.py
```

### Result 
N = `1000`, Epsilon = `0.5`, BETA = `0.1` with Exponatial Mechanism

#### 1. Probibility
<img width="641" alt="screen shot 2018-11-01 at 3 45 45 am" src="https://user-images.githubusercontent.com/6240395/47839773-540a8100-dd8a-11e8-8db2-c132261334db.png">

#### 2. Private Loss Histogram
<img width="646" alt="screen shot 2018-11-01 at 3 45 52 am" src="https://user-images.githubusercontent.com/6240395/47839790-64226080-dd8a-11e8-8f94-bde971d19570.png">
 

#### 3. Accuracy 
<img width="643" alt="screen shot 2018-11-01 at 3 46 01 am" src="https://user-images.githubusercontent.com/6240395/47839803-700e2280-dd8a-11e8-83b9-2bcddf5f6522.png">
