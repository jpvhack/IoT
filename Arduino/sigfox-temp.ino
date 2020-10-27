#include <SigFox.h>

void setup() {
  // Configuración del monitor serie
  Serial.begin(9600);
  delay(500);
  
  // Iniciamos módulo Sigfox
  if(!SigFox.begin()){
    Serial.println("Error al iniciar módulo Sigfox");
    return;
  }

  // Mostramos la información del ID y de PAC
  Serial.println("ID = " + SigFox.ID());
  Serial.println("PAC = " + SigFox.PAC());

  // Apagamos el módulo
  SigFox.end();
}

void loop() {
  // En el loop no hacemos nada

}
