 ## Installation
 ``` 
 pip install ahp_calculator
```
## Usage
``` 
from ahp_calculator import ahp_calculator 

AC=ahp_calculator()
AC.open_calculator()
```

## INTRODUCTION

The Analytic Hierarchy Process (AHP) is a method for organizing and evaluating complicated decisions, using Maths and Psychology. In 1970s, Thomas L. Saaty developed AHP which is a theory of measurement. AHP has been widely used, particularly in large-scale situations with several criteria and when the evaluation of alternatives is mostly subjective. It has quantifying capability which distinguishes the AHP from other decision making techniques.

AHP is one of the extensively used Multi Criteria Decision Making (MCDM) tool for processing multiple important objectives and weighting the criteria. The AHP allows to assign a priority among various alternatives and integrating multidimensional measures into a single scale of priorities.

## METHOD

The pair-wise comparison is used to compare the importance of criteria. It can be carried out with nine-point scale value which includes values 9, 8, 7, 6...., 1/7, 1/8, 1/9, which indicates 9 as extreme preference, 7 as very strong preference, 5 as strong preference and so on down to 1 which represents no preference. Thus, the pair-wise comparison aids to simplify the criteria by evaluating the independent contribution of each criterion with each other. The square matrix is organized for pairwise comparisons of various criteria. The principal eigenvalue and their corresponding eigenvector was developed among the relative importance within the criteria from the comparison matrix. The weights for each element can be generated from the normalized eigenvector. The subjective judgment from AHP were checked via consistency index. The consistency index (CI) is calculated as:
<br>
&emsp; CI = ( λmax - n ) / ( n - 1 )<br>
 &emsp; Where CI = Consitency Index<br>
 &emsp; λmax = maximum eigenvector of the matrix <br>
 &emsp; n = order of the matrix <br>
 After comparing CI with random index, Consistency Ratio (CR) can be derived from their ratio. The consistency ratio should be ≤ 0.1 (Saaty, 1990). The pairwise comparison is assumed to be inconsistent if the CR exceeds the threshold, the process has to be reviewed in such case.
 <br><br>

 
 ![image](https://github.com/Geospasolutions/AHP_Calculator/blob/master/assests/Matrix.PNG)
<br> <br>
![image](https://github.com/Geospasolutions/AHP_Calculator/blob/master/assests/Animation.gif)
