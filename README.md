### Tensorflow Board + Word2Vec 

This is a full example the tensorflow board with Word2Vec as seen in the google AI experiments Video

--------------

#### Introduction

Word2Vec is one of the most common used NLP machine learning tools to cluster words based on co-occurance (skipgram model). 
Due to the programmatic nature of Word2Vec, the resulting word vectors are high dimensional (>200 dimensions). To make those word vectors human interpretable common dimensionality reduction techniques are PCA or T-SNE.  

With the Google Tensorflow Board users have the advantage to see the stepwise learning process of the algorithm and to study the word vector graphics in a D3.js based interactive interface.

In this repo the advanced word2vec.py example from tensorflow was taken and connected to the tensorflow board by writing a pipeline with all neccessary steps by training on the sample text file and opening the tensor board.  

#### Build pre-requisites

    Tensorflow 1.0
    g++ compiler (latest)
    python 2.7

#### Installation Steps: 

 - git clone https://github.com/tensorflow/models
 - Follow the word2vec steps according to the manual (https://github.com/tensorflow/models/tree/master/tutorials/embedding): g++ compiling and downloading the example text (execute those steps in the /tutorials/embedding folder)
 - copy the pipeline.py and word2vec.py from this repo into the /tutorials/embedding folder
 - Run python pipeline.py --epochs_to_train 3 --train_data text8 --eval_data questions-words.txt --save_path /tmp/log
  
#### Result: 

The standart interface (with T-SNE)

![alt tag](https://firebasestorage.googleapis.com/v0/b/rscriptmarket-66f49.appspot.com/o/statics%2Fgithub%2Ftensorboard1.png?alt=media&token=04a51b8a-b670-464d-b1d6-759361e52df9)

The focused interface (with PCA)

![alt tag](https://firebasestorage.googleapis.com/v0/b/rscriptmarket-66f49.appspot.com/o/statics%2Fgithub%2Ftensorboard2.png?alt=media&token=75caa3da-b1e2-4c71-802b-ea04a4501d4c)


#### Next Steps:

 - add document2vec algorithms
 - improve speed & efficiency of the word2vec.py file

  