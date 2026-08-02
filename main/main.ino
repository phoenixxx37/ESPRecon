#include <config.h>
#include <ESP8266WiFi.h>
String command = "";
#define led_red 2
#define led_green 16

void setup() {
	pinMode(led_red, OUTPUT);
	pinMode(led_green, OUTPUT);
	Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
//==================================
	for(int i = 0; i < 10; i++) {
		digitalWrite(led_red, 1); digitalWrite(led_green, 1); delay(200); digitalWrite(led_red, 0); digitalWrite(led_green, 0); delay(200);
	}
}
void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "RED ON") {
      digitalWrite(led_red, 1);
      Serial.println("LED RED turned ON");
    }
    else if (command == "GREEN ON") {
      digitalWrite(led_green, 1);
      Serial.println("LED GREEN turned ON");
    }
    else if (command == "RED OFF") {
      digitalWrite(led_red, 0);
      Serial.println("LED RED turned OFF");
    }
    else if (command == "wifianalyzer") {

      int channels[14] = {0};

      Serial.println("===== WIFI RADIO ANALYZER =====");

      int networks = WiFi.scanNetworks();

      if (networks == 0) {
        Serial.println("WiFi networks not found");
        Serial.println("END");
        return;
      }


      for (int i = 0; i < networks; i++) {

        int ch = WiFi.channel(i);

        if (ch >= 1 && ch <= 13) {
          channels[ch]++;
        }

      }


      int maxChannel = 1;
      int maxValue = 0;


      for (int i = 1; i <= 13; i++) {

        Serial.print("Channel ");
        Serial.print(i);
        Serial.print(" ");

        for (int j = 0; j < channels[i]; j++) {
          Serial.print("#");
        }

        Serial.print("  ");
        Serial.print(channels[i]);
        Serial.println(" networks");


        if (channels[i] > maxValue) {
          maxValue = channels[i];
          maxChannel = i;
        }

      }


      Serial.println("----------------------------");

      Serial.print("Most crowded channel: ");
      Serial.println(maxChannel);

      Serial.println("END");


      WiFi.scanDelete();
    }
    else if (command == "GREEN OFF") {
      digitalWrite(led_green, 0);
      Serial.println("LED GREEN turned OFF");
    }
    else if (command == "scanapp") {
      int networks = WiFi.scanNetworks();
      
      if (networks == 0) {
        Serial.println("Сети не найдены!");
        Serial.println("END");
        } else {
        Serial.print("Найдено сетей: ");
        Serial.println(networks);
        Serial.println("=========================================");
        
        for (int i = 0; i < networks; i++) {
          Serial.println("\n--- Сеть #" + String(i + 1) + " ---");
          
          Serial.print("SSID: ");
          Serial.println(WiFi.SSID(i));
          
          Serial.print("BSSID: ");
          Serial.println(WiFi.BSSIDstr(i));
          
          Serial.print("RSSI: ");
          Serial.print(WiFi.RSSI(i));
          Serial.println(" dBm");
          
          Serial.print("Канал: ");
          Serial.println(WiFi.channel(i));
          
          Serial.print("Шифрование: ");
          uint8_t encryption = WiFi.encryptionType(i);
          switch (encryption) {
            case ENC_TYPE_NONE:
              Serial.println("ОТКРЫТАЯ (без пароля)");
              break;
            case ENC_TYPE_TKIP:
              Serial.println("WPA (TKIP)");
              break;
            case ENC_TYPE_CCMP:
              Serial.println("WPA2 (AES)");
              break;
            case ENC_TYPE_AUTO:
              Serial.println("WPA/WPA2 (авто)");
              break;
            default:
              Serial.println("Неизвестно");
              break;
          }
          
          Serial.print("Скрытая: ");
          Serial.println(WiFi.isHidden(i) ? "ДА" : "НЕТ");
        }
        
        Serial.println("\n=========================================");
        Serial.println("Сканирование завершено!");
        WiFi.scanDelete();
        Serial.println("END");
      }
    }
    else {
      Serial.println("Неизвестная команда");
      Serial.println("END");
    }
  }
}