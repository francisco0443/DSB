# C2B Group 4

Projeto desenvolvido em grupo no âmbito da unidade curricular Data Science for Business, para a Care to Beauty.

Este repositório reúne o código usado para resolver dois problemas de negócio: fidelização de clientes e otimização de stock. O trabalho combina preparação de dados, análise exploratória, segmentação, recomendação e previsão de vendas.

## Fidelização de clientes

O primeiro objetivo foi identificar perfis comportamentais de clientes para apoiar uma estratégia de loyalty mais personalizada.

Para isso, foi feita limpeza e preparação de dados transacionais, construção de métricas como RFM e outros indicadores comportamentais, e segmentação com K-Means.

A solução final identificou quatro personas principais:

- Deal Hunters
- Dormant
- Core Actives
- High-Value Explorers

Estas personas permitem orientar estratégias distintas de retenção, comunicação e recomendação.

## Sistema híbrido de recomendação

A partir da segmentação, foi desenvolvido um sistema híbrido de recomendação baseado em learning to rank com LightGBM.

O modelo combina várias fontes de sinal:

- popularidade global
- co-ocorrência de produtos
- similaridade por conteúdo
- popularidade por persona

Os resultados mostraram desempenho superior aos baselines simples nas métricas de ranking e recomendação, com melhor capacidade para priorizar os produtos mais relevantes para cada cliente.

## Previsão de vendas e stock

O segundo problema explorou previsão de vendas com LSTM para apoiar decisões de reposição e planeamento de inventário.

Foi usada uma análise ABC/XYZ para definir o universo de SKUs mais relevantes, seguida de engenharia de features temporais, comerciais e históricas.

Apesar de a abordagem ter sido metodologicamente sólida, os resultados não superaram de forma consistente métodos de previsão mais simples, o que indica espaço para melhoria futura na arquitetura e nas features.

## Estrutura do repositório

- `Fidelização/` - notebooks ligados a segmentação, recomendação e preparação de dados.
- `SalesForecast/` - notebooks de análise e previsão de vendas.
- `Stuff/` - scripts e notebooks auxiliares para exportação, limpeza e exploração.


