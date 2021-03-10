# Machine-Learning-Algorithms

---------- K-Means Algorithm------------- 

After evaluation of the implemented algorithm:

classification_report's overall shape after many trials is:   

              precision    recall  f1-score   support
           0       0.95      0.97      0.96       334
           1       1.00      1.00      1.00       333
           2       0.97      0.95      0.96       333

    accuracy                           0.97      1000
    macro avg      0.97      0.97      0.97      1000
    weighted avg   0.97      0.97      0.97      1000

Performance of K-Means on Some Difficult DataSet(N=1000, K=3)

![Figure_1](https://user-images.githubusercontent.com/43790905/109571743-2d48ea80-7afd-11eb-88a1-243ac76357e7.png)

![difficult](https://user-images.githubusercontent.com/43790905/109571910-65e8c400-7afd-11eb-9b55-c0f6aa434393.png)



------------ NAIVE BAYES CLASSIFICATION(Gaussian Naive Bayes) -------------------

Time Complexity O(N*k) where N = sample size k =#features

In my implementation I used Gaussian Distrubution Function as the likelihood function


Any #Samples,#features,#classes can be selected


Easy Prediciton Cases


![resim](https://user-images.githubusercontent.com/43790905/110560626-5bf73e80-8157-11eb-85a9-226e6df08b0e.png)


Predicted data: [0.59701462 0.17565587], probability matrix: [2.0740195124616857e-20, 1.3434938976936702e-09, 5.38207044913125e-11, 0.002467214513519645], Class prediction: 3 (yellow)

Some Example Outputs (Difficult Datasets)


![Screenshot_1](https://user-images.githubusercontent.com/43790905/110560486-23effb80-8157-11eb-9ace-90633f17cb08.jpg)

Prediction => Predicted data: [0.66155157 0.12965543], probability matrix: [4.2641016633004194e-15, 6.583880853799688e-16, 1.6702414085001405e-11, 1.134583396026431e-35], Class prediction: 2 (green)


![resim](https://user-images.githubusercontent.com/43790905/110560699-7d582a80-8157-11eb-82c2-9c33a88286fe.png)


Predicted data: [0.64899913 0.80238836], probability matrix: [4.170053097274955e-19, 3.426164633100442e-15, 1.2343720339194956e-23, 5.1688366455939134e-11], Class prediction: 3 (yellow)

![resim](https://user-images.githubusercontent.com/43790905/110560762-97920880-8157-11eb-9b15-f51a933ca875.png)


Predicted data: [0.19029299 0.99193991], probability matrix: [1.730899822525541e-09, 0.0018788863789938246, 0.0024679061237033433, 2.0486430866068992e-22], Class prediction: 2 (green)


