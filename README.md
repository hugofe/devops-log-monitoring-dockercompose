**DevOps - Poc - Monitoramento e Log**

**Este repositório visa o de ferramentas de monitoramento e log para uma aplicação web.**

Neste contém os seguintes serviços como containers:
 - Applicação Web(Pyhon - Flask)
 - DB MySQL
 - Web Server(Nginx)
 - Graylog 
 - MongoDB
 - ElasticSearch
 - Monitoramento Prometheus
 - Grafana

Para utilização de todos os serviços foram criados três(3) arquivos .yml seguindo a estrutura de arquivo docker-composer

1. docker-compose.app.yml, contém serviços para subir a aplicação WEB e suas dependências:
    - Aplicação WEB
    - Mysql
    - Nginx

2. docker-compose.graylog.yml, contém serviços para subir o graylog e suas dependências:
    - MongoDB
    - ElasticSearch
    - Graylog

Arquitetura Graylog

.. image:: https://docs.graylog.org/en/3.2/_images/architec_small_setup.png

3. docker-compose.monitoring.yml, contém serviços para subir o prometheus e suas dependências:
    - Prometheus
    - Grafana

A aplicação WEB é um formulario que foi desenvolvida em Python utilizando do framework Flask, contendo os seguintes campos:
Nome
E-mail
Comentátio
Botão Enviar


Execução
--------

Para reproduzir este ambiente é necessário apenas a utilização do comando.

**Linux**

.. code-block:: shell
docker-compose -f docker-compose.app.yml \
               -f docker-compose.graylog.yml \
               -f docker-compose.monitoring.yml up


Futuras melhorias:
------------------

Migrar serviços para cluster Kubernetes.

Mysql
Utilizar Percona em cluster com Proxysql para escalabidade e alta disponibilidade.

MongoDB
Utilizar Percona Server para MongoDB para escalabidade e alta disponibilidade.

Prometheus
Adicionar segurança com algum tipo de autenticação e ssl, basic auth e ssl com nginx por exemplo.
Adicionar cAdvisor para analise de uso e performance dos container.

Grafana
Adicionar segurança ssl.

Graylog
Melhorar as metricas e centralização de logs de acordo com o contexto necessário.

ElasticSearch
Adicionar segurança ssl e autenticação de usuario.

