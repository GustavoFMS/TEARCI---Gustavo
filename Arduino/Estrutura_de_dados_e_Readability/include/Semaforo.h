#pragma once

class Semaforo
{
  public:

    Semaforo(const int pin_green, const int pin_red, const int pin_yellow); // constructor

    const int pin_red;
    const int pin_yellow;
    const int pin_green;

    void ligar_Verde();

    void ligar_amarelo();

    void ligar_vermelho();
};