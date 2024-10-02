## Erste Schritte
Dieses Kapitel beschreibt Schritt-für-Schritt wie die Installation und abschliessende Inbetriebnahme durchgeführt werden sollen.

### 1. Programm-Installationen auf dem Windows-Rechner
Die Zusammenstellung der benötigten Programm-Installationsdateien sind unter dem folgenden Kapitel
<a href="https://www.xlh.xemax.ch/3000_installation_ibn/1000_installation/#sps-entwicklungsumgebung" target="_blank">
   Download Windows-Programme
</a>
abgelegt.
1. Installation <i>SPS Entwicklungsumgebung (Codesys)</i>, gemäss Video aus dem Kapitel 
<a href="https://www.xlh.xemax.ch/3000_installation_ibn/1000_installation/#sps-entwicklungsumgebung" target="_blank">
   SPS Entwicklungsumgebung
</a>
2. Installation <i>SD Card Formatter</i>, gemäss Video aus dem Kapitel 
<a href="https://www.xlh.xemax.ch/3000_installation_ibn/1000_installation/#sps-entwicklungsumgebung" target="_blank">
   Hilfsprogramme
</a>
3. Installation <i>win32diskimager</i>, gemäss Video aus dem Kapitel 
<a href="https://www.xlh.xemax.ch/3000_installation_ibn/1000_installation/#sps-entwicklungsumgebung" target="_blank">
   Hilfsprogramme
</a>
4. Installation <i>putty</i>, gemäss Video aus dem Kapitel 
<a href="https://www.xlh.xemax.ch/3000_installation_ibn/1000_installation/#sps-entwicklungsumgebung" target="_blank">
   Hilfsprogramme
</a>
5. Installation <i>uaexpert</i>, gemäss Video aus dem Kapitel 
<a href="https://www.xlh.xemax.ch/3000_installation_ibn/1000_installation/#sps-entwicklungsumgebung" target="_blank">
   Hilfsprogramme
</a>

#### Hinweis:
Die Programme <i>SD Card Formatter</i> und <i>win32diskimager</i> (Schritte 2 und 3) werden benötigt, um das Image auf 
die SD-Karte zu laden. Das Programm <i>PuTTY</i> wird für den Direktzugang (Terminal) zum xLH_base verwendet. Abschliessend
wird das Programm <i>UaExpert</i> installiert. Dies ist ein OPCUA-Client, welcher für den Betrieb und Test der OPCUA-Schnittstelle
verwendet wird.


### 2. Inbetriebnahme xLH-Base

#### 1. Image auf SD-Karte laden
Die Vorgehensweise für das Laden eines Image auf die SD-Karte unterteilt sich in die folgenden Schritte:
1. SD-Karte formatieren, gemäss Video aus dem Kapitel 
<a href="https://www.xlh.xemax.ch/3000_installation_ibn/2000_inbetriebnahme_xlh/" target="_blank">
   xLH_base Installation Linux-Betriebssystem.
</a> Das Image <i>XLH_base_REV0.img</i> ist unterhalb des Videos abgelegt.
2. Image <i>XLH_base_REV0.img</i> mittels <i>win32diskimager</i> auf die SD-Karte laden bzw. schreiben. Die Schritte sind im Video aus dem Kapitel 
<a href="https://www.xlh.xemax.ch/3000_installation_ibn/2000_inbetriebnahme_xlh/" target="_blank">
   xLH_base Installation Linux-Betriebssystem
</a> ersichtlich.
3. SD-Karte korrekt in den Slot des xLH_base hineinstecken. Hierfür muss der Print aus dem Gehäuse entfernt werden.

#### 2. Konfiguration Ethernet und WiFi
In diesem Schritt werden die drei verschiedenen Arten der Konnektierung des xLH_base beschrieben. Alle Schritte sind im Video aus dem Kapitel 
<a href="https://www.xlh.xemax.ch/3000_installation_ibn/2000_inbetriebnahme_xlh/" target="_blank">
   xLH_base Konfiguration Ethernet & WiFi
</a> dokumentiert.
Dem xLH_base wird standardmässig die IP 192.168.31.31 zugewiesen. 
1. <b>USB-Kabel</b> (Empfehlung)
2. WiFi (Einstellungen via PuTTY vornehmen)
3. Ethernet-Adapter

Für die korrekte Funktionalität des xLH-base genügt es eine dieser drei Verbindungsmöglichkeiten einzurichten.
