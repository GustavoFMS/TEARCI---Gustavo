#include <Arduino.h>
#include <WiFi.h>
#include <Stepper.h>

// Definição dos pinos do driver ULN2003 (usando os números GPIO diretamente)
#define IN1 4   // Azul (GPIO 4)
#define IN2 12  // Amarelo (GPIO 12)
#define IN3 13  // Laranja (GPIO 13)
#define IN4 14  // Verde (GPIO 14)

// Número de passos por revolução do motor (ajuste conforme necessário)
const int stepsPerRevolution = 2048;

// Inicializa a biblioteca do motor de passo
Stepper myStepper(stepsPerRevolution, IN4, IN3, IN2, IN1);

// Credenciais de rede Wi-Fi
const char* ssid = "iPhone de Paloma";
const char* password = "palloma321";

// Definir o número da porta do servidor
WiFiServer server(80);

// Variáveis auxiliares
String header;
String motorState = "off";  // Estado do motor (inicialmente desligado)

// Tempo de controle
unsigned long currentTime = millis();
unsigned long previousTime = 0; 
const long timeoutTime = 2000;

bool isMotorRunning = false;  // Flag para verificar se o motor está rodando

// Função para conectar ao Wi-Fi com tentativas
void connectWiFi() {
  Serial.print("Conectando ao Wi-Fi");
  WiFi.begin(ssid, password);
  
  // Espera até conectar ao Wi-Fi
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);  // Aguarda meio segundo
    Serial.print(".");
  }

  // Imprime o IP do ESP32
  Serial.println("");
  Serial.println("Wi-Fi conectado!");
  Serial.print("IP do ESP32: ");
  Serial.println(WiFi.localIP());
}

// Função que gera a página HTML para o controle do motor
String generateHTML() {
  String html = "<!DOCTYPE html><html>";
  html += "<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">";
  html += "<link rel=\"icon\" href=\"data:,\">";
  html += "<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;} ";
  html += ".button { background-color: #4CAF50; border: none; color: white; padding: 16px 40px; font-size: 30px; margin: 2px; cursor: pointer;} ";
  html += ".button2 {background-color: #555555;}</style></head>";
  html += "<body><h1>Controle do Motor de Passo</h1>";
  html += "<p>Estado do Motor: " + motorState + "</p>";

  // Botão para ligar ou desligar o motor
  if (motorState == "off") {
    html += "<p><a href=\"/motor/on\"><button class=\"button\">Ligar Motor</button></a></p>";
  } else {
    html += "<p><a href=\"/motor/off\"><button class=\"button button2\">Desligar Motor</button></a></p>";
  }

  html += "</body></html>";
  return html;
}

// Função que faz o motor girar de forma contínua
void runMotorContinuously() {
  if (motorState == "on" && !isMotorRunning) {
    isMotorRunning = true;
    Serial.println("Motor está girando...");
  }
  if (motorState == "on" && isMotorRunning) {
    myStepper.step(1);  // Giro contínuo, um passo por vez
    delay(10);  // Delay para evitar que o motor gire muito rápido
  }
  if (motorState == "off") {
    isMotorRunning = false;
    Serial.println("Motor parou.");
  }
}

void setup() {
  Serial.begin(115200);

  // Atraso inicial para garantir que o ESP32 tenha tempo de estabilizar
  delay(1000);  // Aguarda 1 segundo para estabilizar

  // Conecta ao Wi-Fi
  connectWiFi();

  // Inicia o servidor
  server.begin();

  // Configura o motor de passo
  myStepper.setSpeed(5);  // Define a velocidade do motor (5 RPM)
}

void loop() {
  WiFiClient client = server.available();   // Escuta por clientes

  if (client) {                             // Se um novo cliente se conectar,
    currentTime = millis();
    previousTime = currentTime;
    Serial.println("Novo Cliente.");

    String currentLine = "";                // Variável para armazenar os dados recebidos
    while (client.connected() && currentTime - previousTime <= timeoutTime) {
      currentTime = millis();
      if (client.available()) {             // Se há dados para ler do cliente
        char c = client.read();             // Lê o byte
        Serial.write(c);                    // Exibe no serial monitor
        header += c;
        if (c == '\n') {                    // Se encontrou uma nova linha
          if (currentLine.length() == 0) {  // Fim do cabeçalho da requisição HTTP
            // Resposta HTTP
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();

            // Controle do motor de passo
            if (header.indexOf("GET /motor/on") >= 0) {
              motorState = "on";  // Motor começa a girar
              Serial.println("Motor Ligado");
            } else if (header.indexOf("GET /motor/off") >= 0) {
              motorState = "off";  // Motor para de girar
              Serial.println("Motor Desligado");
            }

            // Envia o HTML para o cliente
            client.print(generateHTML());

            client.println();
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }
    header = "";  // Limpa a variável de cabeçalho
    client.stop();
    Serial.println("Cliente desconectado.");
  }

  // Roda o motor continuamente se o estado for "on"
  runMotorContinuously();
}
