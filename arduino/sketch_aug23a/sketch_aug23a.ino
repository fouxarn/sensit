#include <Wire.h>
int number = -1;

double temp;

/* FSR testing sketch. 
Connect one end of FSR to power, the other end to Analog 0.
Then connect one end of a 10K resistor from Analog 0 to ground 
 
For more information see www.ladyada.net/learn/sensors/fsr.html */

void setup(void) {
  //Serial.begin(115200);   // We'll send debugging information via the Serial monitor
  // initialize i2c as slave
 Wire.begin(4);
 
 // define callbacks for i2c communication
 Wire.onReceive(receiveData);
 Wire.onRequest(sendData);
}
 
void loop(void) {
  
 temp = GetTemp();

  
  
}

// callback for received data
void receiveData(int byteCount){
 
 while(Wire.available()) {
  number = Wire.read();
  digitalWrite(13, HIGH); // set the LED on
 }
}
 
// callback for sending data
void sendData(){
  if(number >= 0 && number < 2) {
    int fsrForce = getPressure(number);
    digitalWrite(13, LOW); // set the LED off
    Wire.write(fsrForce);
  }
  
  /*int dataSize = 4;
    byte data[dataSize];

  data[0] = fsrForce & 0xFF;
  data[1] = (fsrForce >> 8) & 0xFF;
  data[2] = (fsrForce >> 16) & 0xFF;
  data[3] = (fsrForce >> 24) & 0xFF;

  Wire.write(data,dataSize);
  */
}



long getPressure(int fsrPin) {
  int fsrReading;     // the analog reading from the FSR resistor divider
  int fsrVoltage;     // the analog reading converted to voltage
  
  unsigned long fsrResistance;  // The voltage converted to resistance, can be very big so make "long"
  unsigned long fsrConductance; 
  long fsrForce;                // Finally, the resistance converted to force
 
  fsrReading = analogRead(fsrPin);  
  //Serial.print("Analog reading = ");
  //Serial.println(fsrReading);
 
  // analog voltage reading ranges from about 0 to 1023 which maps to 0V to 5V (= 5000mV)
  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  //Serial.print("Voltage reading in mV = ");
  //Serial.println(fsrVoltage);  
 
  if (fsrVoltage == 0) {
    //Serial.println("No pressure");
    return 0;  
  } else {
    // The voltage = Vcc * R / (R + FSR) where R = 10K and Vcc = 5V
    // so FSR = ((Vcc - V) * R) / V        yay math!
    fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
    fsrResistance *= 560;                // 560 resistor
    fsrResistance /= fsrVoltage;
    //Serial.print("FSR resistance in ohms = ");
    //Serial.println(fsrResistance);
 
    fsrConductance = 1000000;           // we measure in micromhos so 
    fsrConductance /= fsrResistance;
    //Serial.print("Conductance in microMhos: ");
    //Serial.println(fsrConductance);
 
    // Use the two FSR guide graphs to approximate the force
    if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
      //Serial.print("Force in Newtons: ");
      //Serial.println(fsrForce);      
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30;
      //Serial.print("Force in Newtons: ");
      //Serial.println(fsrForce);         
    }
    return fsrForce;
  }  
}
 
// Get the internal temperature of the arduino
double GetTemp(void)
{
 unsigned int wADC;
 double t;
 ADMUX = (_BV(REFS1) | _BV(REFS0) | _BV(MUX3));
 ADCSRA |= _BV(ADEN); // enable the ADC
 delay(20); // wait for voltages to become stable.
 ADCSRA |= _BV(ADSC); // Start the ADC
 while (bit_is_set(ADCSRA,ADSC));
 wADC = ADCW;
 t = (wADC - 324.31 ) / 1.22;
 return (t);
}

