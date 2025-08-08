🔍 Cercatore — Data Discovery e Analisi dei Dati Sensibili
Cercatore è un tool open-source per la scansione automatica di file su file system locali o condivisi, progettato per identificare e classificare dati sensibili all'interno di file .txt, .pdf, .docx, .xlsx, immagini e altro.

Il sistema genera report completi in Excel, PDF, e grafici interattivi. Include una Web GUI semplice da usare.

📦 Funzionalità principali
✅ Estrazione e analisi di contenuto da file di vario tipo
✅ OCR integrato per analizzare immagini (.jpg, .png, .pdf scannerizzati)
✅ Classificazione per livello di rischio (Alto, Medio, Manuale)
✅ Generazione report .xlsx, .pdf + grafici .png
✅ Web GUI per avviare scansioni, scaricare report e filtrare per rischio o tipo di dato
✅ Nessuna installazione complessa richiesta

📁 Struttura del progetto

cercatore/
├── Cercatore.py             # Motore principale
├── app.py                   # Web GUI in Flask
├── templates/
│   ├── index.html           # Home GUI
│   ├── reports.html         # Lista dei report
│   ├── filtered_risk.html   # Report filtrati per rischio
│   └── filtered_tags.html   # Report filtrati per tag
├── static/                  # (opzionale: favicon, sfondo)
└── report/                  # Cartella dove vengono generati i report
⚙️ Requisiti
Python 3.8+

Librerie Python:

pip install flask pandas matplotlib pytesseract fpdf openpyxl python-docx PyPDF2 tqdm
(Opzionale) Tesseract OCR installato nel sistema:

Ubuntu: sudo apt install tesseract-ocr

Windows: Tesseract GitHub

🚀 Avvio rapido
1. Avvio via Web GUI

python app.py
Poi visita: http://localhost:5000

2. Uso da linea di comando

python Cercatore.py --path "/percorso/da/scansionare" --max-size 10 --output ./report
Argomenti:

--path: cartella da scansionare

--max-size: dimensione massima in MB dei file da analizzare

--output: cartella dove salvare i report

--search (opzionale): parola o regex da cercare

📊 Dati cercati
Il motore identifica automaticamente:

📧 Email

📞 Numeri di telefono

💳 IBAN e carte di credito

🧬 Dati sanitari (patologie, esami, farmaci…)

🔐 Password e credenziali

🏛️ Dati giudiziari, politici, religiosi, sindacali

I dati vengono classificati per rischio: Alto, Medio, o Manuale (nessun pattern rilevato ma file potenzialmente utile).

📈 Report generati

Ogni scansione produce:

report.xlsx: dati completi

report.pdf: riepilogo sintetico

rischi.png: grafico a torta per rischio

sensibili.png: grafico a barre dei tag

🧠 Esempio d'uso

python Cercatore.py --path "/mnt/c/Users/NomeUtente/Documents" --max-size 15
Oppure via interfaccia Web:

Seleziona percorso dal menu a tendina

Inserisci dimensione massima

Clicca Avvia scansione

📂 Visualizzazione e download dei report
Accedi alla sezione Visualizza report per:

Visualizzare tutti i report salvati

Filtrare i risultati per tag o per rischio

Scaricare singoli file .xlsx, .pdf, .png

💬 Suggerimenti
Usa questo tool come supporto manuale all’audit dei dati

Integra nella tua pipeline DLP, SOC o IT

Pianifica scansioni automatiche tramite cron o scheduler

🔒 Sicurezza
I file e i report non escono mai dalla tua rete. Tutto il contenuto rimane in locale sul sistema dove è eseguito.

📜 Licenza
MIT License — uso libero anche in ambienti aziendali.

🤝 Autori
Realizzato con ❤️ per l'automazione della data discovery 
