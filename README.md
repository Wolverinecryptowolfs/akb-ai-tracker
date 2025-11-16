# Autonomous Knowledge Broker (AKB) - AI Model Update & Benchmark Tracker

Dies ist der Code für Ihr **super einzigartiges** Projekt, das die programmatische Paywall-Funktion von Paywen.dev und das x402-Protokoll nutzt, um einen autonomen, KI-gesteuerten Informationsdienst zu schaffen.

## Projekt-Zusammenfassung

*   **Nische:** AI Model Update & Benchmark Tracker
*   **Technologie:** Python, `requests`, `beautifulsoup4`, `openai` (für `gemini-2.5-flash`), Paywen.dev API.
*   **Funktion:** Sammelt automatisch die neuesten AI-Forschungspapiere (z.B. von arXiv), fasst sie mit einem LLM zu einem hochwertigen, monetarisierbaren Report zusammen und erstellt eine Paywall über die Paywen API.

## Wichtige Anweisungen zur Inbetriebnahme

### 1. Vorbereitung (Einmalig)

1.  **Code-Upload:** Laden Sie den gesamten Inhalt dieses Ordners in Ihr GitHub-Repository (`wolverinecryptowolfs/akb-ai-tracker`) hoch.
2.  **GitHub Pages aktivieren:** Gehen Sie in den Repository-Einstellungen zu **Pages** und aktivieren Sie die Veröffentlichung vom `main`-Branch (oder `master`) aus dem `/root`-Ordner.
3.  **Basis-URL ermitteln:** Warten Sie, bis GitHub Pages die URL anzeigt (sie sollte etwa so aussehen: `https://wolverinecryptowolfs.github.io/akb-ai-tracker/`). **Diese URL ist Ihre AKB_BASE_URL.**

### 2. Konfiguration (Einmalig)

Der Code ist so konfiguriert, dass er die Basis-URL über eine **Umgebungsvariable** liest.

Öffnen Sie Ihr Terminal und setzen Sie die Variable. **Ersetzen Sie den Platzhalter durch Ihre tatsächliche GitHub Pages URL:**

```bash
export AKB_BASE_URL="https://wolverinecryptowolfs.github.io/akb-ai-tracker/"
```

**Wichtig:** Achten Sie darauf, dass die URL mit einem Schrägstrich (`/`) endet.

### 3. Tägliche Ausführung

Führen Sie den AKB in zwei einfachen Schritten aus:

#### Schritt A: Report generieren

Dieser Befehl sammelt Daten, generiert den Report und speichert ihn in `reports/ai_research_briefing_JJJJ-MM-TT.md`.

```bash
./run_akb.sh
```

#### Schritt B: Upload und Paywall erstellen (Manuell/Final)

Das Skript `run_akb.sh` kann den Report nicht automatisch auf GitHub hochladen. **Sie müssen dies tun.**

1.  **Upload:** Laden Sie die neu generierte Datei (`reports/ai_research_briefing_JJJJ-MM-TT.md`) in Ihr GitHub-Repository hoch.
2.  **Paywall erstellen:** Führen Sie den finalen Befehl aus, um die Paywall zu erstellen. Das Skript `run_akb.sh` gibt Ihnen diesen Befehl am Ende aus. Er wird etwa so aussehen:

    ```bash
    python3 paywen_integrator.py ai_research_briefing_2025-11-16.md
    ```

Dieser Befehl gibt Ihnen den **finalen Paywall-Link** aus, den Sie dann verbreiten können.

---

**Viel Erfolg mit Ihrem Autonomous Knowledge Broker!**
