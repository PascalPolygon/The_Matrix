
  # The Matrix: Navigating VR with Machine Learning-Decoded EEG’s 
  
  -----
  <p align="center">
  Mawaba Pascal Dao<br> 
  Pdao2015@my.fit.edu <br>
  Spring 2020   
  </p>
  
  As industries and entire societies are increasingly reliant on the symbiosis of human-machine interactions for their success, it is important to identify methods for optimizing those interactions, notably by increasing the bandwidth at which those interactions happen. The current ways of interacting with machines include using devices such as buttons, pointers, keyboards etc. Such tools are cumbersome and provide extremely low rates of data transfer from the human to the machine. For example, you can only use 2 thumbs to type on a smartphone keyboard. The goal of this project will be to design and train a machine learning algorithm on human EEG brain signals. The EEG signals will represent basic inputs such as: move left or move right. The trained algorithm will be able to take in those inputs and accordingly manipulate an object in a virtual environment.  The development of such a Brain Machine Interface will have valuable applications in medicine, space and defense, robotics and entertainment amongst many other fields. The proposed algorithm is a Support Vector Machine (SVM) that feeds into a Neural Network (NN) [4]. This architecture is chosen because based on the current literature it provides the best classification performance for this type of application [1]. The training and testing EEG data will be obtained from the PhysioNet EEG dataset which consists of over 1500 one-to-two minutes long EEG records, logged from 109 healthy people [2]. The data will be EEG signal values over 64 channels sampled at 160 Hz. 


In completing this project, the following tasks need to completed 

1- Filtering EEG signals 

This pre-processing step will be required to filter out the unwanted signal. The specific                 filtering to be applied is yet to be decided 

2- Artifact Removal 

This is a second pre-processing step to reduce the amount of useless data created by artifacts in EEG signals [3]. Eye and muscle movement are examples of physiological artifacts that will mask the EEG signal. 

3- Feature Extraction 

A possible method for this step is using Discrete Wavelet Transforms [4] 

4- Designing ML 

Implementing the SVM and NN 

5- Training ML 

The training will be done on a dedicated subset of the PhysioNet data  

6- Testing ML 

The held-out subset will be used for testing. 

7- Connectivity to a custom virtual environment in Unity

With this project I hope to establish the groundwork for the development of a truly immersive AI-powered VR experience. A subject I plan to work on for my master's thesis. Given that the data is labeled and obtained from a reputable source, the success of this project can be measured as the training accuracy of the machine learning algorithm. 

---
<p align="center">
 References 
  </p>
  
[1] G. Pfurtscheller, C. Neuper, D. Flotzinger, and M. Pregenzer, "EEGbased discrimination between imagination of right and left hand movement," Electroencephalography and Clinical Neurophysiology, vol. 103, pp. 642-651, 1997. 

[2] A. L. Goldberger, L. A. N. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark, J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley, "PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals," Circulation, vol. 101, pp. e215-e220, June 13, 2000 2000. 

[3] G. Bartels, S. Li-Chen, and L. Bao-Liang, "Automatic artifact removal from EEG - a mixed approach based on double blind source separation and support vector machine," in 2010 Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), 2010, pp. 5383-5386. 

[4] Alomari, Mohammad & Abubaker, Ayman & Turani, Aiman & Baniyounes, Ali & Manasreh, Adnan. (2014). EEG Mouse:A Machine Learning-Based Brain Computer Interface. International Journal of Advanced Computer Science and Applications. 5. 193-198. 10.14569/IJACSA.2014.050428.
