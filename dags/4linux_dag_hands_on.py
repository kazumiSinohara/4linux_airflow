#Para completar esta dag vamos reproduzir as modificações realizadas durante a etapa de modelagem
#e implementar no pipeline do airflow através de uma dag

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime
import pandas as pd
import nltk
import spacy
import re
from unicodedata import normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import load
import numpy as np

dag = DAG(
    dag_id = '4linux_dag',
    start_date = datetime(2020,4,17),
    schedule_interval = '*/5 * * * *')


def remover_acentos(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()


def remover_acentos_pontuacoes(df):
    df['text_pt'] = df.text_pt.apply(lambda texto: remover_acentos(texto))
    df['text_pt'] = df.text_pt.apply(lambda texto: re.sub(u'[^a-z]', ' ', texto))
    df['text_pt'] = df.text_pt.apply(lambda texto: re.sub(u'\s+', ' ', texto))
    return df


def remove_stop_words(df,stopwords):
    df['text_pt_w_sw'] = df.text_pt.apply(lambda texto: ' '.join(p for p in texto.split() if p not in stopwords))
    return df


def remove_stopwords():
    #Ler o dataset de validação
    #Retirar as stopwords do idioma português utilizando nltk e spacy
    #Remover os acentos das reviews e das stopwords
    #Salvar o dataframe resultante com o nome 'imdb-reviews-pt-br_stopwords.csv'

    df = pd.read_csv("imdb-reviews-pt-br_validation.csv", encoding='utf-8', index_col=0)
    
    #TODO: implementar a remoção das stopwords, como fizemos no notebook
    return None


def predict_sentiment():
    #Ler o dataset de validação com os stopwords removidos
    #Carregar o modelo vectorizer (método load do joblib)
    #Vetorizar as reviews com TF-IDF (método transform do vectorizer)
    #Carregar o modelo de regressão logística (clf)
    #Realizar a análise de sentimento no vetor TF-IDF (método predict de clf)
    #Salvar o dataset resultante com o nome: 'imdb-reviews-pt-br_answer.csv'
    
    df = pd.read_csv("imdb-reviews-pt-br_stopwords.csv", encoding='utf-8', index_col=0)
    
    #TODO: implementar a transformação das reviews em vetores TF-IDF
    #TODO: implementar a classificaçao dos vetores a partir do modelo de regressão logistíca treinado
    return None


remove_stopwords = PythonOperator(
    task_id = 'remove_stopwords',
    python_callable = remove_stopwords,
    dag = dag)

predict_sentiment = PythonOperator(
    task_id = 'predict_sentiment',
    python_callable = predict_sentiment,
    dag = dag)

#Define a ordem das tasks dentro da DAG
remove_stopwords >> predict_sentiment
