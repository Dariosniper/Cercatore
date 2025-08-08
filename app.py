from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash
import os
import subprocess
from datetime import datetime
import pandas as pd

app = Flask(__name__)
app.secret_key = "cercatore-secret"

UPLOAD_FOLDER = os.path.abspath("./uploads")
REPORT_FOLDER_DEFAULT = os.path.abspath("./report")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER_DEFAULT, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_path = request.form.get("path_select")
        custom_path = request.form.get("custom_path")
        path = custom_path if selected_path == "custom" else selected_path

        output = REPORT_FOLDER_DEFAULT
        max_size = request.form.get("max_size") or "10"

        if not path or not os.path.exists(path):
            flash("Percorso da scansionare non valido.", "danger")
            return redirect(url_for("index"))

        try:
            subprocess.run([
                "python3", "Cercatore.py",
                "--path", path,
                "--output", output,
                "--max-size", max_size
            ], check=True)
            flash("Scansione completata con successo.", "success")
            return redirect(url_for("report_list"))
        except subprocess.CalledProcessError:
            flash("Errore durante l'esecuzione dello script.", "danger")

    return render_template("index.html")

@app.route("/report")
def report_list():
    all_reports = []
    search_dirs = [REPORT_FOLDER_DEFAULT, "/mnt/c", "/mnt/e"]

    for base_dir in search_dirs:
        if not os.path.exists(base_dir):
            continue
        for entry in os.listdir(base_dir):
            full_path = os.path.join(base_dir, entry)
            if os.path.isdir(full_path) and entry.startswith("report_"):
                try:
                    files = os.listdir(full_path)
                    all_reports.append({
                        "name": entry,
                        "path": full_path,
                        "files": files
                    })
                except Exception:
                    continue

    return render_template("reports.html", reports=all_reports)

@app.route("/download/<report>/<filename>")
def download_file(report, filename):
    search_dirs = [REPORT_FOLDER_DEFAULT, "/mnt/c", "/mnt/e"]
    for base in search_dirs:
        target_dir = os.path.join(base, report)
        if os.path.exists(os.path.join(target_dir, filename)):
            return send_from_directory(target_dir, filename, as_attachment=True)
    return "File non trovato", 404

@app.route("/report/<report>/filter/<filter>")
def filtered_view(report, filter):
    search_dirs = [REPORT_FOLDER_DEFAULT, "/mnt/c", "/mnt/e"]
    for base in search_dirs:
        report_dir = os.path.join(base, report)
        excel_path = os.path.join(report_dir, "report.xlsx")
        if os.path.exists(excel_path):
            df = pd.read_excel(excel_path)
            if filter == "rischio":
                grouped = df.groupby("Rischio")
                return render_template("filtered_risk.html", grouped=grouped, report=report)
            elif filter == "tags":
                from collections import defaultdict
                tag_rows = defaultdict(list)
                for _, row in df.iterrows():
                    if pd.isna(row["Tags"]): continue
                    for tag in str(row["Tags"]).split(","):
                        tag_rows[tag.strip()].append(row)
                return render_template("filtered_tags.html", tags=tag_rows, report=report)
            else:
                return "Filtro non valido", 400
    return "Report non trovato", 404

if __name__ == "__main__":
    app.run(debug=True)
