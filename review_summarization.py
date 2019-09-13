#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for Text Summarization

Author : Arijit Ghosh Chowdhury

*****************************************************************************
Input Parameters:
    reviews: A list of strings containing the reviews

Returns:
    summary: A list of strings containing the summaries.
*****************************************************************************
"""


# ***************************************************************************
import numpy as np
from talon.signature.bruteforce import extract_signature
from langdetect import detect
from nltk.tokenize import sent_tokenize
import skipthoughts
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
# ***************************************************************************


def preprocess(reviews):
    """
    Performs preprocessing operations such as:
        1. Removing signature lines (only English reviews are supported)
        2. Removing new line characters.
    """
    n_reviews = len(reviews)
    for i in range(n_reviews):
        review = reviews[i]
        review, _ = extract_signature(review)
        lines = review.split('\n')
        for j in reversed(range(len(lines))):
            lines[j] = lines[j].strip()
            if lines[j] == '':
                lines.pop(j)
        reviews[i] = ' '.join(lines)
        
        
def split_sentences(reviews):
    """
    Splits the reviews into individual sentences
    """
    n_reviews = len(reviews)
    for i in range(n_reviews):
        review = reviews[i]
        sentences = sent_tokenize(review)
        for j in reversed(range(len(sentences))):
            sent = sentences[j]
            sentences[j] = sent.strip()
            if sent == '':
                sentences.pop(j)
        reviews[i] = sentences
        
        
def skipthought_encode(reviews):
    """
    Obtains sentence embeddings for each sentence in the reviews
    """
    enc_reviws = [None]*len(reviews)
    cum_sum_sentences = [0]
    sent_count = 0
    for review in reviews:
        sent_count += len(review)
        cum_sum_sentences.append(sent_count)

    all_sentences = [sent for review in reviews for sent in email]
    print('Loading pre-trained models...')
    model = skipthoughts.load_model()
    encoder = skipthoughts.Encoder(model)
    print('Encoding sentences...')
    enc_sentences = encoder.encode(all_sentences, verbose=False)

    for i in range(len(reviews)):
        begin = cum_sum_sentences[i]
        end = cum_sum_sentences[i+1]
        enc_reviews[i] = enc_sentences[begin:end]
    return enc_reviews
        
    
def summarize(reviews):
    """
    Performs summarization of reviews
    """
    n_reviews = len(reviews)
    summary = [None]*n_reviews
    print('Preprecesing...')
    preprocess(reviews)
    print('Splitting into sentences...')
    split_sentences(reviews)
    print('Starting to encode...')
    enc_reviews = skipthought_encode(reviews)
    print('Encoding Finished')
    for i in range(n_reviews):
        enc_review = enc_reviews[i]
        n_clusters = int(np.ceil(len(enc_review)**0.5))
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans = kmeans.fit(enc_review)
        avg = []
        closest = []
        for j in range(n_clusters):
            idx = np.where(kmeans.labels_ == j)[0]
            avg.append(np.mean(idx))
        closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_,\
                                                   enc_review)
        ordering = sorted(range(n_clusters), key=lambda k: avg[k])
        summary[i] = ' '.join([reviews[i][closest[idx]] for idx in ordering])
    print('Clustering Finished')
    return summary
      