# PONGISIM #

Trabalho de ARQUITETURA DE COMPUTADORES onde se deve recriar um jogo de Pong no Logisim ou Logisim Evolution.

A versão utilizada para o desenvolvimento foi o Logisim Evolution

## Instalação ##

1. Abaixe o arquivo zip do repositorio ( **<> Code** ) e extrai o arquivo para a sua pasta desejada. 
2. Instale o [_Logisim Evolution_](https://github.com/logisim-evolution/logisim-evolution) na sua maquina
3. Rode o programa e vai em `Arquivo > Abrir` e carregue o arquivo **_pongtron_5001.circ_**

## Como Iniciar ##
1. Va para `Simular` e habilite o pulso `Pulso Habilitado` e em `Simular > Frequência de Pulso` configure o pulso por volta de **32 - 16 Hz**

2. Configure o tamanho da sua _"raquete"_ em **PlayerAPaddleSize** e **PlayerBPaddleSize** 
<img width="591" height="67" alt="Captura de tela 2026-05-26 100158" src="https://github.com/user-attachments/assets/1d92557d-19e8-4ed7-82ea-2f18ff9a2454" />
</br></br>
3. Set qual player sera o bot ou não em **Player[X]IsComputer** e sua dificuldade em **Player[X]ComputerLevel** 
<img width="628" height="146" alt="image" src="https://github.com/user-attachments/assets/8fcbda67-eacc-44be-a4d3-f40d6f1af5c5" />
</br></br>
4. Agora aperte no interruptor para iniciar 
<img width="205" height="158" alt="image" src="https://github.com/user-attachments/assets/fa747e28-eec9-489d-a2a6-8dd6d81d4612" />
</br></br>
5. Use isso para controlar a paleta desejada 
<img width="208" height="145" alt="image" src="https://github.com/user-attachments/assets/ac225250-b16a-4e65-9e14-8570a5b4a595" />
</br></br>
6. Olhe para o led e se divirta (área marcada e sua pontuação)
<img width="745" height="509" alt="image" src="https://github.com/user-attachments/assets/4e4fba5c-6a87-4f38-ba70-dff5bf37fb81" />

## Módulos do sistema ##

* **ToDigit** :

* **BCDConverter** :

* **PaddleHandler** :

* **BallHandler** :

* **ComputerEnemyMovementHandler** :

* **DisplayDriver** : Driver responsável para o output da maquina para o display 
<img width="170" height="416" alt="image" src="https://github.com/user-attachments/assets/ce810589-0bf3-4fda-b618-32414b79a740" />

* **PaddleDisplayHandler** :

* **BallDisplayHandler** :

* **ScoreDisplayHandler** :

* **CharacterROM** :

* **CharacterDisplayHandler** :

* **PlayerHandler** : Driver que maneja o controle do jogador
<img width="168" height="340" alt="image" src="https://github.com/user-attachments/assets/fa25467c-f7d0-4d3a-b570-13901433910f" />

* **BallCollisionHandler** :

* **ScoreHandler** :

* **BallStartDirectionHandler** :

* **PauseScreenHandler** :

* **ToggleableCharacterHandler** :
