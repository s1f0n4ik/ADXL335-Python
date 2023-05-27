#define xPin A0
#define yPin A1
#define zPin A2

#define xMin 288
#define yMin 275
#define zMin 277

#define xMax 488
#define yMax 428
#define zMax 428

#define kX (xMax+xMin)/2
#define kY (yMax+yMin)/2
#define kZ (zMax+zMin)/2


//int count = 10;

int xVal, yVal, zVal, Max, dir;
//int xAv, yAv, zAv;


void setup()
{
  Serial.begin(9600);
//  calibrate();
}

void loop()
{
  getdata();

  getdirecrion();

  if (dir ==0)
  {
    if (xVal>0)
      Serial.println("+X");
    else
      Serial.println("-X");
  }
  
  if (dir ==1)
  {
    if (yVal>0)
      Serial.println("+Y");
    else
      Serial.println("-Y");
  }
  
  if (dir ==2)
  {
    if (zVal>0)
      Serial.println("+Z");
    else
      Serial.println("-Z");
  } 

}


void getdirecrion()
{
  Max=abs(xVal);
  dir=0;
  if (abs(yVal)>Max)
  {
    Max=abs(yVal);
    dir=1;
  }
  if (abs(zVal)>Max)
  {
    Max=abs(zVal);
    dir=2;
  }
    
  
}

void getdata()
{
  xVal = analogRead(xPin) - kX;
  yVal = analogRead(yPin) - kY;
  zVal = analogRead(zPin) - kZ;
}
