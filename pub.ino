#define inPin 3

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(inPin, INPUT);
}

bool flg = false;
void loop() {

  // put your main code here, to run repeatedly:
  if (digitalRead(inPin) == 1) {
    if (!flg) {
      Serial.print(1);
      flg = true;
    }
  }  else {
      flg = false;
  }
}
