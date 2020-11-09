#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include "DHT.h"
#include "FS.h"

//sensor de humedad-----------
#define DHTTYPE DHT11
#define DHT_pin 4

DHT dht(DHT_pin, DHTTYPE);
float Temperature;
float Humidity;
int Water;
int led_pin = 5;
int water_pin = A0; 
//-----------------------------

const char* ssid = "Ubee4C00-2.4G";
const char* password = "5F99F84C00";
ESP8266WebServer server(80);

String load_file(int op){
    String tfile = "";
    if(op == 0){
        tfile = "/web.html";
    }
    else{
        tfile = "/web2.html";
    }

    SPIFFS.begin();
    File file = SPIFFS.open(tfile, "r");
    if(!file){
        Serial.println("[!] Error al leer el archivo");
    }
    else{
        String out_file = "";
        while(file.available()){
            String line = file.readStringUntil('\n');
            out_file += line + "\n";
        }
        file.close();
        return out_file;
        Serial.println("Archivo cargado");
    }
}

String html_file_main, html_file_aux;
void setup(){
    //inicializar cosas
    Serial.begin(115200);
    delay(100);

    pinMode(led_pin, OUTPUT);
    pinMode(DHT_pin, INPUT);
    digitalWrite(led_pin, LOW);
    dht.begin();

    //cargar wifi
    Serial.print("Conectando a: "); Serial.println(ssid);

    WiFi.begin(ssid, password);
    while(WiFi.status() != WL_CONNECTED){
        delay(1000);
        Serial.print(".");
    }
    digitalWrite(led_pin, HIGH);
    Serial.println("");
    Serial.println("WiFi conectado...!");
    Serial.print("IP: "); Serial.println(WiFi.localIP());

    html_file_main = load_file(0);
    html_file_aux = load_file(1);

    server.on("/", handle_OnConnect);

    server.on("/fetch", handle_more);

    server.onNotFound(handle_NotFound);
    server.begin();
    Serial.println("HTTP server enabled");
}

void loop(){
    server.handleClient();
}

void handle_OnConnect(){
    Temperature = dht.readTemperature();
    Humidity = dht.readHumidity();
    server.send(200, "text/html", SendHTML(Temperature,Humidity));
}

void handle_more(){
    Humidity = dht.readHumidity();
    Temperature = dht.readTemperature();
    Water = analogRead(water_pin);
    //data_out = html_file_main + Humidity + html_file_aux;
    
    server.send(200, "text/html", SendHTMLhidden(Temperature,Humidity,Water));
}


void handle_NotFound(){
    server.send(404, "text/plain", "El sitio no existe");
}


String SendHTMLhidden(float Temp, float Humi, int Water){
  String ptr = "<!DOCTYPE html><html>\n";
  ptr += "<title>Sensor DHT</title>\n";
  ptr += "</head><meta http-equiv=\"refresh\" content=\"2\"\n>";
  ptr += "<body>\n";
  ptr += "<div><label>Temperatura: ";
  ptr += Temp;
  ptr += "\n";
  ptr += "</label></div>\n";
  ptr += "<div><label>Humedad: ";
  ptr += Humi;
  ptr += "\n";
  ptr += "<div><label>Nivel de agua: ";
  ptr += Water;
  ptr += "\n";
  ptr += "</label></div>\n";
  ptr += "</body></html>\n";
  return ptr;
}

String SendHTML(float Temperaturestat, float Humiditystat){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<head><meta http-equiv=\"refresh\" content=\"1000\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<link href=\"https://fonts.googleapis.com/css?family=Open+Sans:300,400,600\" rel=\"stylesheet\">\n";
  ptr +="<title>ESP8266 Weather Report</title>\n";
  ptr +="<style>html { font-family: 'Open Sans', sans-serif; display: block; margin: 0px auto; text-align: center;color: #333333;}\n";
  ptr +="body{margin-top: 50px;}\n";
  ptr +="h1 {margin: 50px auto 30px;}\n";
  ptr +=".side-by-side{display: inline-block;vertical-align: middle;position: relative;}\n";
  ptr +=".humidity-icon{background-color: #3498db;width: 30px;height: 30px;border-radius: 50%;line-height: 36px;}\n";
  ptr +=".humidity-text{font-weight: 600;padding-left: 15px;font-size: 19px;width: 160px;text-align: left;}\n";
  ptr +=".humidity{font-weight: 300;font-size: 60px;color: #3498db;}\n";
  ptr +=".temperature-icon{background-color: #f39c12;width: 30px;height: 30px;border-radius: 50%;line-height: 40px;}\n";
  ptr +=".temperature-text{font-weight: 600;padding-left: 15px;font-size: 19px;width: 160px;text-align: left;}\n";
  ptr +=".temperature{font-weight: 300;font-size: 60px;color: #f39c12;}\n";
  ptr +=".superscript{font-size: 17px;font-weight: 600;position: absolute;right: -20px;top: 15px;}\n";
  ptr +=".data{padding: 10px;}\n";
  ptr +="</style>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  
   ptr +="<div id=\"webpage\">\n";
   
   ptr +="<h1>ESP8266 Weather Report</h1>\n";
   ptr +="<div class=\"data\">\n";
   ptr +="<div class=\"side-by-side temperature-icon\">\n";
   ptr +="<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\"\n";
   ptr +="width=\"9.915px\" height=\"22px\" viewBox=\"0 0 9.915 22\" enable-background=\"new 0 0 9.915 22\" xml:space=\"preserve\">\n";
   ptr +="<path fill=\"#FFFFFF\" d=\"M3.498,0.53c0.377-0.331,0.877-0.501,1.374-0.527C5.697-0.04,6.522,0.421,6.924,1.142\n";
   ptr +="c0.237,0.399,0.315,0.871,0.311,1.33C7.229,5.856,7.245,9.24,7.227,12.625c1.019,0.539,1.855,1.424,2.301,2.491\n";
   ptr +="c0.491,1.163,0.518,2.514,0.062,3.693c-0.414,1.102-1.24,2.038-2.276,2.594c-1.056,0.583-2.331,0.743-3.501,0.463\n";
   ptr +="c-1.417-0.323-2.659-1.314-3.3-2.617C0.014,18.26-0.115,17.104,0.1,16.022c0.296-1.443,1.274-2.717,2.58-3.394\n";
   ptr +="c0.013-3.44,0-6.881,0.007-10.322C2.674,1.634,2.974,0.955,3.498,0.53z\"/>\n";
   ptr +="</svg>\n";
   ptr +="</div>\n";
   ptr +="<div class=\"side-by-side temperature-text\">Temperature</div>\n";
   ptr +="<div class=\"side-by-side temperature\">";
   ptr +=Temperaturestat;
   ptr +="<span class=\"superscript\">C</span></div>\n";
   ptr +="</div>\n";
   ptr +="<div class=\"data\">\n";
   ptr +="<div class=\"side-by-side humidity-icon\">\n";
   ptr +="<svg version=\"1.1\" id=\"Layer_2\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\"\n\"; width=\"12px\" height=\"17.955px\" viewBox=\"0 0 13 17.955\" enable-background=\"new 0 0 13 17.955\" xml:space=\"preserve\">\n";
   ptr +="<path fill=\"#FFFFFF\" d=\"M1.819,6.217C3.139,4.064,6.5,0,6.5,0s3.363,4.064,4.681,6.217c1.793,2.926,2.133,5.05,1.571,7.057\n";
   ptr +="c-0.438,1.574-2.264,4.681-6.252,4.681c-3.988,0-5.813-3.107-6.252-4.681C-0.313,11.267,0.026,9.143,1.819,6.217\"></path>\n";
   ptr +="</svg>\n";
   ptr +="</div>\n";
   ptr +="<div class=\"side-by-side humidity-text\">Humidity</div>\n";
   ptr +="<div class=\"side-by-side humidity\">";
   ptr +=Humiditystat;
   ptr +="<span class=\"superscript\">%</span></div>\n";
   ptr +="</div>\n";

  ptr +="</div>\n";
  ptr +="</body>\n";
  ptr +="</html>\n";
  return ptr;
}
