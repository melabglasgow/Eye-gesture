int TMR0, TMR1, TMR2;
byte MSB1,LSB1,MSB2,LSB2,MSB3,LSB3;
//int F0, F1, F2;


void setup() {
  Serial.begin(115200);  //initial the Serial
}
  
void loop() {

    TMR0 = analogRead(A0);
    TMR1 = analogRead(A1);
    TMR2 = analogRead(A2);

    MSB1 = (TMR0>>8) & 0xFF;
    LSB1 = TMR0 & 0xFF;
    
    MSB2 = (TMR1>>8) & 0xFF;
    LSB2 = TMR1 & 0xFF;
    
    MSB3 = (TMR2>>8) & 0xFF;
    LSB3 = TMR2 & 0xFF;
    
    Serial.write("X");
    Serial.write(MSB1);
    Serial.write(LSB1);
    Serial.write(MSB2);
    Serial.write(LSB2);
    Serial.write(MSB3);
    Serial.write(LSB3);
    Serial.write("Y");

    
//    Serial.write(TMR2);
    delay(10);
}
