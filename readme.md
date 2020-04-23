Projeto final:

Nesse projeto iremos realizar uma análise de sentimento em um
dataset com reviews de filmes em português.

Este projeto será divido em duas partes, a primeira será a etapa
de análise e modelamento, que será realizado no Jupyter. 
A segunda será a etapa onde implementaremos os processos de limpeza 
e classificação, desenvolvidos na primeira etapa,
nos dados de validação utilizando uma DAG do airflow.

Instruções para a segunda etapa:

Vamos instalar o airflow a partir de uma imagem de Docker.

O primeiro passo é montar um container com o airflow e com as
bibliotecas adicionais que iremos utilizar. A forma mais simples de 
realizar este passo é estar com o terminal na mesma pasta onde
se encontra o Dockerfile deste projeto e executar o seguinte comando:

$ sudo docker build --tag docker-airflow-4linux:1.1 .

Uma vez que a imagem foi montada basta iniciar o container com o
seguinte comando:

$ docker run -d -p 8080:8080 -v $(pwd)/dags:/usr/local/airflow/dags docker-airflow-4linux:1.1

Depois que o notebook for realizado e os modelos treinados e salvos, vamo completar a DAG
e introduzi-la no airflow. Para isso basta entrar no terminal do container o o seguinte comando:

$ docker exec -it <container id> bash

depois navegar até /usr/local/airflow/dags e executar este comando:

$ python 4linux_dag.py

Para executar a DAG imediatamente, basta utilizar este comando:

$ airflow backfill -s -1 4linux_dag

**Caso seja necessário deletar a DAG
$ airflow delete_dag 4linux_dag -y






