#include <Arduino.h>
#include <Stepper.h>

// Definição dos pinos do motor e parâmetros
const int passosMotor = 32;
const int reducao = 64;
const int passosPorVolta = passosMotor * reducao;

// Definição dos pinos dos botões
const int botao1 = 2;  // Botão para sentido horário
const int botao2 = 3;  // Botão para sentido anti-horário

// Configuração do motor de passo
//IN1- 8, IN2 - 11, IN3 - 9, IN4 -10
Stepper mpHorarios(passosMotor, 8, 9, 10, 11);
Stepper mpAntiHorarios(passosMotor, 11, 10, 9, 8);

// Estados possíveis para a máquina de estados
enum Estado {
  Parado,
  MOVENDO_HORARIO,
  MOVENDO_ANTI_HORARIO
};

Estado estadoAtual = Parado;  // Começa parado

// Variáveis para evitar múltiplas leituras do botão (debounce)
bool botao1Anterior = HIGH;
bool botao2Anterior = HIGH;

void setup() {
  pinMode(botao1, INPUT_PULLUP);
  pinMode(botao2, INPUT_PULLUP);
  
  mpHorarios.setSpeed(100);
  mpAntiHorarios.setSpeed(100);
}

void loop() {
  // Lê os estados atuais dos botões
  bool leituraBotao1 = digitalRead(botao1);
  bool leituraBotao2 = digitalRead(botao2);

  // Detecta clique no botão 1 (borda de descida)
  if (leituraBotao1 == LOW && botao1Anterior == HIGH) {
    if (estadoAtual != MOVENDO_HORARIO) {
      estadoAtual = MOVENDO_HORARIO;
    } else {
      estadoAtual = Parado;
    }
  }

  // Detecta clique no botão 2 (borda de descida)
  if (leituraBotao2 == LOW && botao2Anterior == HIGH) {
    if (estadoAtual != MOVENDO_ANTI_HORARIO) {
      estadoAtual = MOVENDO_ANTI_HORARIO;
    } else {
      estadoAtual = Parado;
    }
  }

  // Atualiza os estados dos botões
  botao1Anterior = leituraBotao1;
  botao2Anterior = leituraBotao2;

  // Máquina de estados para controle do motor
  switch (estadoAtual) {
    case MOVENDO_HORARIO:
      mpHorarios.step(1);  // Gira no sentido horário continuamente
      break;

    case MOVENDO_ANTI_HORARIO:
      mpAntiHorarios.step(1);  // Gira no sentido anti-horário continuamente
      break;

    case Parado:
      // Motor parado (não faz nada)
      break;
  }
}
