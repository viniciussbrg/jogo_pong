# PONGISIM #

Trabalho de ARQUITETURA DE COMPUTADORES onde se deve recriar um jogo de Pong no Logisim ou Logisim Evolution.

A versão utilizada para o desenvolvimento foi o Logisim Evolution

<img width="1497" height="838" alt="WhatsApp Image 2026-06-03 at 17 01 36" src="https://github.com/user-attachments/assets/37fa298d-2449-4d85-bedc-decf8c6a628d" />

## Instalação ##

1. Abaixe o arquivo zip do repositorio ( **<> Code** ) e extrai o arquivo para a sua pasta desejada. 
2. Instale o [_Logisim Evolution_](https://github.com/logisim-evolution/logisim-evolution) na sua maquina
3. Rode o programa e vai em `Arquivo > Abrir` e carregue o arquivo **_pongtron_5001.circ_**

## Como Iniciar ##
1. Va para `Simular` e habilite o pulso `Pulso Habilitado` e em `Simular > Frequência de Pulso` configure o pulso por volta de **32 - 16 Hz**

2. Configure o tamanho da sua _"raquete"_ em **PlayerAPaddleSize** e **PlayerBPaddleSize** 
</br>
<img width="591" height="67" alt="Captura de tela 2026-05-26 100158" src="https://github.com/user-attachments/assets/1d92557d-19e8-4ed7-82ea-2f18ff9a2454" />
</br></br>
3. Set qual player sera o bot ou não em **Player[X]IsComputer** e sua dificuldade em **Player[X]ComputerLevel** 
</br>
<img width="628" height="146" alt="image" src="https://github.com/user-attachments/assets/8fcbda67-eacc-44be-a4d3-f40d6f1af5c5" />
</br></br>
4. Agora aperte no interruptor para iniciar 
</br>
<img width="205" height="158" alt="image" src="https://github.com/user-attachments/assets/fa747e28-eec9-489d-a2a6-8dd6d81d4612" />
</br></br>
5. Use isso para controlar a paleta desejada 
</br>
<img width="208" height="145" alt="image" src="https://github.com/user-attachments/assets/ac225250-b16a-4e65-9e14-8570a5b4a595" />
</br></br>
6. Olhe para o led e se divirta (área marcada e sua pontuação)
</br>
<img width="45%" height="45%" alt="image" src="https://github.com/user-attachments/assets/4e4fba5c-6a87-4f38-ba70-dff5bf37fb81" />

## Módulos do sistema ##

* **ToDigit** : Conversor de Números para Digitos
<img width="30%" height="30%" alt="image" src="https://github.com/user-attachments/assets/f31ec4cc-8aab-441e-9faa-5b6f72da18d6" />
<img width="36%" height="36%" alt="image" src="https://github.com/user-attachments/assets/0d50d9bc-853d-408a-8451-1629d7ce6c57" />

* **BCDConverter** : BCD converte um número para sua representação em Binary-Coded Decimal e retorna cada dígito individualmente
<img width="336" height="225" alt="image" src="https://github.com/user-attachments/assets/980b3adf-c4ce-45b4-9b70-530549195543" />
<img width="30%" height="30%" alt="image" src="https://github.com/user-attachments/assets/ebe65ee8-6862-47b1-a742-fd807fc3fe05" />

* **PaddleHandler** : Modulo para calcular as propriedades da raquete
<img width="37%" height="37%" alt="image" src="https://github.com/user-attachments/assets/871f8bca-4ae8-4b3f-9833-a2b21317f1a3" />
<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/ee2c969d-8a57-424d-90ab-2ff397f75efb" />

* **BallHandler** : Modulo para calcular a posição da bola
<img width="36%" height="36%" alt="image" src="https://github.com/user-attachments/assets/68548c57-64a3-4692-b7f1-c62087499f4f" />
<img width="36%" height="36%" alt="image" src="https://github.com/user-attachments/assets/078649fd-7cf8-4337-a519-af969539ab0d" />

* **ComputerEnemyMovementHandler** : Driver da IA do computador
<img width="33%" height="33%" alt="image" src="https://github.com/user-attachments/assets/7881134c-e11f-4482-bc47-067dd40c5730" />
<img width="60%" height="60%" alt="image" src="https://github.com/user-attachments/assets/d42901d7-df95-498f-93f6-53775715dec7" />

* **DisplayDriver** : Driver responsável para o output da maquina para o display 
<img width=13% height=13% alt="image" src="https://github.com/user-attachments/assets/ce810589-0bf3-4fda-b618-32414b79a740" />
<img width="53%" height="53%" alt="image" src="https://github.com/user-attachments/assets/2cffa0b4-60f5-455b-90c8-65fb310accd6" />

* **PaddleDisplayHandler** : Modulo para mostrar a raquete no display
<img width="33%" height="33%" alt="image" src="https://github.com/user-attachments/assets/f984a92f-a7ae-42b2-8062-33def7d33f7d" />
<img width="43%" height="43%" alt="image" src="https://github.com/user-attachments/assets/9379f542-5249-4f85-8e00-b3557d5d2802" />

* **BallDisplayHandler** : Modulo para mostrar a bola no display
<img width="13%" height="13%" alt="image" src="https://github.com/user-attachments/assets/5b39f77d-4819-42dc-89b8-ea9f1adb0dbc" />
<img width="64%" height="64%" alt="image" src="https://github.com/user-attachments/assets/7f073c3e-388b-476b-a6fb-f82656c5fd93" />

* **ScoreDisplayHandler** : Modulo para mostrar a pontuação no display
<img width="20%" height="20%" alt="image" src="https://github.com/user-attachments/assets/3cb77b7a-38a7-4d8a-bdca-add5ee66fd09" />
<img width="66%" height="66%" alt="image" src="https://github.com/user-attachments/assets/04cb40eb-5545-4c66-b080-985686b46e85" />

* **CharacterROM** : Contém a fonte usada para os texto no pong
<img width="30%" height="30%" alt="image" src="https://github.com/user-attachments/assets/ba5502ca-06ff-4fe4-9559-fe588ef257ee" />
<img width="30%" height="30%" alt="image" src="https://github.com/user-attachments/assets/ca58799f-07fa-4754-88ae-11888efd7ea0" />

* **CharacterDisplayHandler** : Modulo para mostrar o player no display
<img width="25%" height="25%" alt="image" src="https://github.com/user-attachments/assets/42aa5070-5542-4a77-898b-88b040ad29d0" />
<img width="65%" height="65%" alt="image" src="https://github.com/user-attachments/assets/d5e11498-ae45-4fb4-9f46-5d1a8fba625b" />

* **PlayerHandler** : Driver que maneja o controle do jogador
<img width="27%" height="27%" alt="image" src="https://github.com/user-attachments/assets/ed0eed3b-a952-42d9-a66e-61e6651e3729" />
<img width="60%" height="60%" alt="image" src="https://github.com/user-attachments/assets/3e08112a-cf69-45bf-a305-04aebfb0c792" />

* **BallCollisionHandler** : Modulo da Colisão da bola
<img width="34%" height="34%" alt="image" src="https://github.com/user-attachments/assets/d5634389-89c4-43ba-9701-910669169e8e" />
<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/1675060e-8248-4293-96d1-781335eee49c" />

* **ScoreHandler** : Usado para Salvar e Calcular a Pontuação
<img width="416" height="176" alt="image" src="https://github.com/user-attachments/assets/7f8b4bad-c7a7-4c25-a5c0-4bf007c20714" />
<img width="35%" height="35%" alt="image" src="https://github.com/user-attachments/assets/97209e1f-b747-4b69-8034-e52c2238ddab" />

* **BallStartDirectionHandler** : Modulo para posição de inicio da bola
<img width="34%" height="34%" alt="image" src="https://github.com/user-attachments/assets/7c64486e-1e44-4cc7-95c1-6a73b6f4624b" />
<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/8da3ca3c-dc02-48be-9065-4092d708aca3" />

* **PauseScreenHandler** : Usado para pausar o jogo
<img width="24%" height="24%" alt="image" src="https://github.com/user-attachments/assets/ea85c1eb-beec-4aeb-a3f7-11d79e34471b" />
<img width="34%" height="34%" alt="image" src="https://github.com/user-attachments/assets/705d1d8f-1734-4c8f-9631-4d774342cc14" />

* **ToggleableCharacterHandler** : Toggle de personagem ou computador
<img width="32%" height="32%" alt="image" src="https://github.com/user-attachments/assets/fba1e0f9-fc4f-4948-95dd-2d22f764a32f" />
<img width="67%" height="67%" alt="image" src="https://github.com/user-attachments/assets/1e785a6f-97a6-4c4a-bfe9-0008ab626816" />

