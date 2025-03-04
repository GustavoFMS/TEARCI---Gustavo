#include "Semaforo.h"

#include <Arduino.h>

Semaforo::Semaforo(const int green, const int red, const int yellow)
:pin_green{green},
pin_red{red},
pin_yellow{yellow} {
  // configurar os pinos como saída
  // semaforo 1 Verde
  pinMode(pin_green, OUTPUT);

  // semaforo 1 Vermelho
  pinMode(pin_red, OUTPUT);

  // semaforo 1 Amarelo
  pinMode(pin_yellow, OUTPUT);
}

void Semaforo::ligar_Verde(){
  // ligar LED verde
  digitalWrite(pin_green, HIGH);

  // desligar LED vermelho
  digitalWrite(pin_red, LOW);

  // desligar LED amarelo
  digitalWrite(pin_yellow, LOW);

}

void Semaforo::ligar_amarelo(){
  // desligar LED verde
  digitalWrite(pin_green, LOW);

  // desligar LED vermelho
  digitalWrite(pin_red, LOW);

  // desligar LED amarelo
  digitalWrite(pin_yellow, HIGH);
}

void Semaforo::ligar_vermelho(){
  // desligar LED verde
  digitalWrite(pin_green, LOW);

  // desligar LED vermelho
  digitalWrite(pin_red, HIGH);

  // desligar LED amarelo
  digitalWrite(pin_yellow, LOW);
}