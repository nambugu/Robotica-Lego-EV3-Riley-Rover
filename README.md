RileyRover - Robô com Garra e Sensor Ultrassônico

# 🤖 RileyRover - Veículo Autônomo com Garra e Sensor Ultrassônico

## 📖 Sobre o Projeto
Este projeto consiste no desenvolvimento e programação de um robô móvel baseado no design RileyRover, utilizando o kit LEGO Mindstorms EV3 e a biblioteca Pybricks (MicroPython). O objetivo principal é a navegação autônoma para detecção, aproximação, captura segura de objetos e retorno à base.

## ⚙️ Hardware e Configuração
O robô foi construído com as seguintes especificações:
* **Unidade de Processamento:** LEGO EV3 Intelligent Brick (rodando ev3dev).
* **Atuadores de Tração:** 2 Motores Grandes (Motor Esquerdo: **Porta A** | Motor Direito: **Porta B**).
* **Atuador da Garra:** 1 Motor Médio acoplado ao mecanismo de engrenagens (**Porta C**).
* **Sensor de Percepção:** Sensor Ultrassônico montado na parte frontal (**Porta S4**).
* **Base:** RileyRover Base Design com Back Castor (roda boba) para estabilidade.

## 🚀 Funcionalidades
* **Navegação Autônoma:** O robô avança pelo ambiente utilizando odometria calculada pelo diâmetro das rodas e distância do eixo.
* **Detecção de Objetos:** Utiliza o sensor ultrassônico para identificar o alvo (ex: uma lata) a exatos 6 centímetros de distância.
* **Captura Inteligente (Gripper):** Ao detectar o objeto, o robô para e aciona a garra com precisão de tempo para segurar o item sem danificar as engrenagens.
* **Transporte e Retorno:** Após a captura, o robô gira 210 graus no próprio eixo, retorna para a base, deposita o objeto e finaliza a missão com uma comemoração audiovisual (dança e fanfarra).

## 🛠️ Como Executar
1. Certifique-se de que o EV3 está com o cartão SD do `ev3dev` e conectado ao PC via USB ou Wi-Fi.
2. Abra o projeto no **VS Code** com a extensão do Pybricks instalada.
3. Conecte-se ao robô, abra o arquivo `main.py` e execute o código (F5).

## 👥 Colaboradores (Faculdade Impacta)

* Gustavo Nambu - RA 2300232
* Enzo Ferigatto - RA 2301239
* Pedro Neri - RA 2301683
