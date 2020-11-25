const int led=5;
const int boton=4;
int val;

void setup() {
  Serial.begin(115200);
  delay(100);
  pinMode(led, OUTPUT);
  pinMode(boton, INPUT);

}

void loop() {
  val=digitalRead(boton);
  Serial.println(val);
  if(val == HIGH){
    digitalWrite(led, LOW);
  }
  else{
    digitalWrite(led, HIGH);
  }

}
