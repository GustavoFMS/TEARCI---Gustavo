#include <Arduino.h>

#include "Semaforo.h"

enum State {
  S1 = 0,
  S2
};

State state = S1;

Semaforo sem1(11,9,10);

Semaforo sem2(7,6,8);

Semaforo sem3(6,5,4);

void setup() {
}

void loop() {
  // criar máquina de estados
  switch (state) {
    case S1:
      //
      // Ligar Semaforo 1  Verde
      sem1.ligar_Verde();

      // Ligar Semaforo 2 Vermelho
      sem2.ligar_vermelho();

      // Espera
      delay(5000);

      // Ligar Semaforo 1 Amarelo
      sem1.ligar_amarelo();

      // transição de estado
      state = S2;

      break;

    case S2:
    
      // Ligar Semaforo 1 Vermelho
      sem1.ligar_vermelho();

      // Ligar Semaforo 2 Verde
      sem2.ligar_Verde();

      // Espera
      delay(5000);

      // Ligar Semaforo 2 Amarelo
      sem2.ligar_amarelo();

      // transição de estado
      state = S1;

      break;
  
    default:
      break;
  }
}