
# Positional Inverted Index with MapReduce

This repository contains a MapReduce implementation of a positional inverted index for the "20Newsgroups" dataset. The positional inverted index allows efficient retrieval of documents containing specific terms and supports operations like AND and OR on query terms.

## Problem Statement

The problem was to design a positional inverted index using a MapReduce program for the "20Newsgroups" dataset. The index should be constructed after applying various preprocessing techniques such as stop word removal, normalization, and lemmatization.

The program should implement two functions: `f_or` for computing the 'OR' operation on postings and `f_and` for computing the 'AND' operation on postings. These functions allow running different queries, including nested queries of 'OR' and 'AND' on the postings of terms at runtime.

## Dataset

The "20Newsgroups" dataset consists of several directories, and all directories are used to create the index of documents present in each directory.

## File Structure

- `mapper.py`: Contains the mapper function for preprocessing input data and emitting intermediate key-value pairs.
- `reducer.py`: Contains the reducer function for building the positional inverted index.
- `README.md`: Provides an overview of the project, its objectives, and instructions for running the code.

## Usage

To run the program, follow these steps:

1. **Download and Extract Dataset**: Download and extract the "20Newsgroups" dataset from [here](http://qwone.com/~jason/20Newsgroups/20news-19997.tar.gz).

2. **Install Dependencies**: Ensure that Python 3 and required libraries (NLTK) are installed. NLTK can be installed using pip:
   
   ```bash
    $ pip install nltk


    $ python -m nltk.downloader stopwords wordnet omw punkt

3. **Run MapReduce Job**: Run the MapReduce job using Hadoop or a similar framework. Make sure to provide the paths to the input and output directories, as well as the mapper and reducer scripts.Example usage:
  ```bash
  $ hadoop jar <path_to_hadoop_jar> -input <input_directory> -output <output_directory> -mapper mapper.py -reducer reducer.py
