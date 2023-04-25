//PD controller 
float u=0;
float k=65000;
float d=0;
float e_i=0;
float e_f=0;
float error=0;
//
float goal= 0.5;
//Input
int value = 0;
float voltage;
float psi;
float tactile_sensor;
//On-off device
bool on=false;
String readString="OFF";


void setup()
{
  pinMode(6, OUTPUT);
  Serial.begin(115200);
}

void loop()
{
  while(Serial.available()) 
  {
      readString=Serial.readString();
  }
  if (readString =="ON")
    {
      if (on==false) 
      {
        Serial.println("Device on");
        on=true;
      }
      value = analogRead(A2);
      voltage = value * 5.0/12;
      psi = ((voltage * 0.175)-14.6959)-2.2;
      //tactile_sensor = (psi /14.80)+1;
      error=goal-psi;
      u=k*error+d*(error-e_f);
      e_f=error;
      if (u>255) u=255;
      if (u<0) u=0;
      //Serial.println("Preasure goal = "+String(goal));
      //Serial.println("psi = "+String(psi));
      //Serial.println("Error = "+ String(error));
      analogWrite(6,round(u));
      //analogWrite(6,round(255));
    }
    if (readString =="OFF")
    {
      if (on==true) 
      {
        Serial.println("Device off");
        analogWrite(6,round(0));
        on=false;
      }
    }
    if (readString !="OFF" && readString !="ON")
    {
      goal =readString.substring(0, 3).toFloat();
      Serial.println("Set preassure to: "+String(goal));
      readString="OFF";
    }
  }

