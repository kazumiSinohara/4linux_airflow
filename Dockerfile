# DESCRIPTION: Airflow container with data science library

FROM puckel/docker-airflow:1.10.9
RUN pip install --user scikit-learn
RUN pip install --user spacy
RUN pip install --user nltk
RUN python -m spacy download pt --user


EXPOSE 8080
