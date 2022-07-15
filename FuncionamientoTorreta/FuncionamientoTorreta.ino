//Lllamamos la libreria del servo
#include  <Servo.h>
Servo servo1;
//Instanciamos el Motor A
int ENA = 4;
int IN1 = 3;
int IN2 = 8; 

//Instanciamos el motor B
int ENB=5;
int IN3 = 7;
int IN4 = 6;

//Definimos entradaSerial como nulo y entradaCompleta como falso
String entradaSerial ="";
bool entradaCompleta = false;

//Entregamos los datos del servo
int pin=10;
int pulsoMinimo = 580;
int pulsoMaximo = 2500;
int angulo=0;
//Indicamos el periodo y el tiempo anterior para la funcionalidad de la funcion millis y asi realizar el movimiento
//de los motores
int periodo=1000;
int tiempoAnterior = -10000;

//Inicializamos el servo y los motores
void setup(){
  servo1.attach(pin,pulsoMinimo,pulsoMaximo);
  Serial.begin(9600);
  servo1.write(90);
  pinMode (ENA, OUTPUT);
  pinMode (ENB, OUTPUT);
  pinMode (IN1, OUTPUT);
  pinMode (IN2, OUTPUT);
  pinMode (IN3, OUTPUT);
  pinMode (IN4, OUTPUT);
}

//Provoca el movimiento de los motores con uno girando hacia la izquierda y otro hacia la derecha
void Desplazar(){
  //Motor A
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  analogWrite(ENA,255); //Velocidad del motor A
  //Motor B
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  analogWrite(ENB,255);//Velocidad del motor B
}

//Paramos el movimiento de los motores
void Parar(){
  //Parar movimiento de motot A
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  analogWrite(ENA,0); //Disminuir la velocidad del motor A

  //Parar movimiento del motor B
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
  analogWrite(ENB,0); //Disminuir la velocidad del motor B
}

//Obtiene la respuesta del codigo en python según lo obtenido al reconocimiento de la camara
void serialEvent(){
  while(Serial.available()){
    char inChar = (char)Serial.read();
    entradaSerial +=inChar;
    if(inChar == '\n'){
      entradaCompleta = true;
    }else if(inChar =='n'){
      entradaCompleta = false;
      }
  }
}

//Realiza el movimiento del servo según siga el movimiento del color pre-codificado
//Para cuando es detectado los motores comenzaran el movimiento, al dejar de seguirlo estos se detendran.
void loop(){
  
   serialEvent();
   if(entradaCompleta){
      if(entradaSerial == "izq51\n")
    {
         servo1.write(44);
    }
    if(entradaSerial == "izq52\n")
    {
         servo1.write(45);
    }
    if(entradaSerial == "izq53\n")
    {
         servo1.write(46);
    }
    if(entradaSerial == "izq54\n")
    {
         servo1.write(47);
    }
    if(entradaSerial == "izq55\n")
    {
         servo1.write(48);
    }
    if(entradaSerial == "izq56\n")
    {
         servo1.write(49);
    }
    if(entradaSerial == "izq57\n")
    {
         servo1.write(50);
    }
    if(entradaSerial == "izq58\n")
    {
         servo1.write(51);
    }
    if(entradaSerial == "izq59\n")
    {
         servo1.write(52);
    }
    if(entradaSerial == "izq60\n")
    {
         servo1.write(53);
    }
    if(entradaSerial == "izq61\n")
    {
         servo1.write(54);
    }
    if(entradaSerial == "izq62\n")
    {
         servo1.write(55);
    }
    if(entradaSerial == "izq63\n")
    {
         servo1.write(56);
    }
    if(entradaSerial == "izq64\n")
    {
         servo1.write(57);
    }
    if(entradaSerial == "izq65\n")
    {
         servo1.write(58);
    }
    if(entradaSerial == "izq66\n")
    {
         servo1.write(59);
    }
    if(entradaSerial == "izq67\n")
    {
         servo1.write(60);
    }
    if(entradaSerial == "izq68\n")
    {
         servo1.write(61);
    }
    if(entradaSerial == "izq69\n")
    {
         servo1.write(62);
    }
    if(entradaSerial == "izq70\n")
    {
         servo1.write(63);
    }
    if(entradaSerial == "izq71\n")
    {
         servo1.write(64);
    }
    if(entradaSerial == "izq72\n")
    {
         servo1.write(65);
    }
    if(entradaSerial == "izq73\n")
    {
         servo1.write(66);
    }
    if(entradaSerial == "izq74\n")
    {
         servo1.write(67);
    }
    if(entradaSerial == "izq75\n")
    {
         servo1.write(68);
    }
    if(entradaSerial == "izq76\n")
    {
         servo1.write(69);
    }
    if(entradaSerial == "izq77\n")
    {
         servo1.write(70);
    }
    if(entradaSerial == "izq78\n")
    {
         servo1.write(71);
    }
    if(entradaSerial == "izq79\n")
    {
         servo1.write(72);
    }
    if(entradaSerial == "izq80\n")
    {
         servo1.write(73);
    }
    if(entradaSerial == "izq81\n")
    {
         servo1.write(74);
    }
    if(entradaSerial == "izq82\n")
    {
         servo1.write(75);
    }
    if(entradaSerial == "izq83\n")
    {
         servo1.write(76);
    }
    if(entradaSerial == "izq84\n")
    {
         servo1.write(77);
    }
    if(entradaSerial == "izq85\n")
    {
         servo1.write(78);
    }
    if(entradaSerial == "izq86\n")
    {
         servo1.write(79);
    }
    if(entradaSerial == "izq87\n")
    {
         servo1.write(80);
    }
    if(entradaSerial == "izq88\n")
    {
         servo1.write(81);
    }
    if(entradaSerial == "izq89\n")
    {
         servo1.write(82);
    }
    if(entradaSerial == "ctr90\n")
    {
         servo1.write(90);
    }
    if(entradaSerial == "der1\n")
    {
         servo1.write(84);
    }
    if(entradaSerial == "der2\n")
    {
         servo1.write(85);
    }
    if(entradaSerial == "der3\n")
    {
         servo1.write(86);
    }
    if(entradaSerial == "der4\n")
    {
         servo1.write(87);
    }
    if(entradaSerial == "der5\n")
    {
         servo1.write(88);
    }
    if(entradaSerial == "der6\n")
    {
         servo1.write(89);
    }
    if(entradaSerial == "der7\n")
    {
         servo1.write(90);
    }
    if(entradaSerial == "der8\n")
    {
         servo1.write(91);
    }
    if(entradaSerial == "der9\n")
    {
         servo1.write(92);
    }
    if(entradaSerial == "der10\n")
    {
         servo1.write(93);
    }
    if(entradaSerial == "der11\n")
    {
         servo1.write(94);
    }
    Desplazar();
    
   
   
    entradaSerial ="";
    entradaCompleta = false;
    
    
      
    }else if(millis() - tiempoAnterior >= periodo){
      Parar();
      tiempoAnterior=millis();
      }    
  }
