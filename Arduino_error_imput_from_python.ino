

void setup() {

  pinMode(13,OUTPUT);
  Serial.begin(9600);

}

void loop() {
  
  if(Serial.available()> 0){
    String error_imput_str=Serial.readString(); 
    int error_imput=int(Serial.read());
    if(error_imput > 80){
      digitalWrite(13,HIGH);   
    }
    else{
      digitalWrite(13,LOW);
    }
    Serial.print(error_imput); 
  }
}
