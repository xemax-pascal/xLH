---
comments: true
---

ToDo Formulierung der Systemstruktur:

- Fluidsim als Simulationsumgebung Pneumatik
- SPS xLH_base für die Verarbeitung der Logik
- Gateway zwischen Fluidsim und xLH_base via DDE zu OPC-UA Kommunikation
    - Variante 1 via DDE => Verwendung einer Gateway-Applikation, einfach in der Anwendung aper proprietär
        - Umsetzung in der Form einer Windows - Exe bzw. Aufruf Pythoninterpreter aus dem Quellcode
        - <a href="https://github.com/xemax-pascal/xLH/tree/d89240d792d0439d9b8d1979ac4f5fef00753786/source/xLH_base/lernpfad_hydraulik_vps_sps/gateway" target="_blank">Quellcode GitHub</a>
        - ![Image Aufgabe Pneumatik](../assets/img/lernpfad_sps_simulation_uebersicht.drawio.png){ style="width:50%"}
    - Variante 2 via OPC-UA => Industriestandard, in der Anwendung anspruchsvoller
    

Exemplarische Arbeitssituation (zeit- und ortsunabhängig).

![Image Aufgabe Pneumatik](../assets/img/lernpfad_1e_simulation_mit_sps.gif){ style="width:100%"}

=== "Mögliche Lernfelder"
    | ID LFE                                                                                                                                                       | Name LFE                                                                                                       |
    | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_00/#F39F09C6-53EE-5846-B7F3-6F30D9381B97" target="_blank">LFB_Aa_FelSu</a>      | Fehler in automatisierten Anlagen suchen, analysieren und beheben                                              |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_00/#70CB8AB4-F0C0-1748-8949-E905B342E0BB" target="_blank">LFB_El_DT1</a>        | kombinatorische Digitaltechnik                                                                                 |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_00/#B2D8A172-016E-F441-AB34-ACEE81B44CAF" target="_blank">LFB_El_DT2</a>        | sequentielle Digitaltechnik                                                                                    |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_00/#456851AB-1DFF-8343-B99E-866FB47668E8" target="_blank">LFB_ES_cil</a>        | Entstehung von Logikschaltungen                                                                                |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_00/#317FFDA5-9A5A-5745-A74B-465C8B240745" target="_blank">LFB_ES_doc</a>        | Fertigungsunterlagen für automatisierte Anlagen erstellen                                                      |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_00/#1752BAD4-4106-C040-9B7C-B85D031BB64E" target="_blank">LFB_Es_Ks_Ef</a>      | Einfache Kleinspannungssteuerungen verstehen und aufbauen                                                      |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_00/#DF2DE14B-4A07-1D45-B325-01890A1A3288" target="_blank">LFB_Es_Ns_Ef</a>      | Einfache Niederspannungssteuerungen verstehen und aufbauen                                                     |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_01/#F75E0D55-2648-CE40-B78F-23D62B7D3A33" target="_blank">LFB_Hs_IuK</a>        | Entwickeln und visualisieren von Ideen und Konzepten                                                           |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_01/#95C74906-5C6D-BF4C-81E9-D58B52B53039" target="_blank">LFB_In_iaa</a>        | Inbetriebnahme automatisierter Anlagen                                                                         |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_02/#4F6D1388-1AEB-5D45-82EA-AE24BB2CA3BB" target="_blank">LFB_In_IBN</a>        | Inbetriebnahme                                                                                                 |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_02/#3E8D12CA-DB8E-894D-BB88-B027AA4C319F" target="_blank">LFB_In_IBS</a>        | In Betriebs Setzung                                                                                            |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_02/#8045EB34-E5B4-C544-B0C8-744109F0AA0F" target="_blank">LFB_MEM_PLG1b</a>     | Prozesse lesen und gestalten 3-3                                                                               |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_02/#06E8BEBE-1BD0-FB48-8B65-020FD4AA660E" target="_blank">LFB_MEM_PLG2</a>      | Prozesse lesen und gestalten 2-3                                                                               |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_02/#5CBC3C34-410A-A248-9B6F-3EF7EBE5D9E9" target="_blank">LFB_Pe_Es</a>         | Einfachen elektrische Steuerungen entwickeln                                                                   |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#1938F84C-32C3-FA4F-9993-6D830B19789E" target="_blank">LFB_Pn_PNAS</a>       | Automatisierte Steuerungen                                                                                     |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#28F47FD9-3970-204A-A566-271BB1F23F1E" target="_blank">LFB_Pn_PNES</a>       | Einfache Steuerungen                                                                                           |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#470852FD-6612-C94D-BD71-9D0F77327599" target="_blank">LFB_Pp_ePr</a>        | ein einfaches Projekt planen und realisieren                                                                   |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#CA4BFD57-C0ED-5648-BBD9-791CD4011384" target="_blank">LFB_Pü_PMc5</a>       | einfache automatisierte Anlagen zur Produktion von Produkten der MEM-Industrie aufbauen und in Betrieb nehmen  |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#CA4BFD57-C0ED-5648-BBD9-791CD4011384" target="_blank">LFB_Pü_PrD</a>        | Prozessdaten                                                                                                   |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#CA4BFD57-C0ED-5648-BBD9-791CD4011384" target="_blank">LFB_Pv_Auf1</a>       | Aufbau Programmieren und Visualisieren                                                                         |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#CA4BFD57-C0ED-5648-BBD9-791CD4011384" target="_blank">LFB_Pv_Auf2</a>       | Aufbau Programmieren und Visualisieren                                                                         |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#CA4BFD57-C0ED-5648-BBD9-791CD4011384" target="_blank">LFB_Pv_BAS</a>        | Programmieren und Visualisieren                                                                                |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#CA4BFD57-C0ED-5648-BBD9-791CD4011384" target="_blank">LFB_Pv_PrgVisu_la</a> | Software und Visualisierungen von automatisierten Anlagen laden                                                |
    | <a href="https://futuremem-docs-xemax.eu.pythonanywhere.com/de/data/4000_lfe_03/#CA4BFD57-C0ED-5648-BBD9-791CD4011384" target="_blank">LFB_Pv_PrgVisu_pt</a> | Software und Visualisierungen von automatisierten Anlagen programmieren und testen                             |

=== "Mögliche Aufgabenstellung"
    ToDo: Aufgabenstellung formulieren

=== "Mögliche Lösung"
    ![Image Aufgabe Pneumatik](../assets/img/lernpfad_1e_simulation_mit_sps.gif){ style="width:100%"}