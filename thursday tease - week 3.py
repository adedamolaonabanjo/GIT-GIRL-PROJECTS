Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
>>> student_id = [1,2,3,4,5,6,7,8,9,10]
>>> exam_dataframe = pd.DataFrame(exam_data, index = student_id)
>>> exam_dataframe
         name  score  attempts qualify
1   Anastasia   12.5         1     yes
2        Dima    9.0         3      no
3   Katherine   16.5         2     yes
4       James    NaN         3      no
5       Emily    9.0         2      no
6     Michael   20.0         3     yes
7     Matthew   14.5         1     yes
8       Laura    NaN         1      no
9       Kevin    8.0         2      no
10      Jonas   19.0         1     yes
>>> 
