from flask import Flask, render_template, request, redirect, url_for
from database import init_db, save_comment, get_all_comments
from sentiment import analyze_sentiment

app = Flask(__name__)

# Garante a criação da tabela do banco de dados na inicialização
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        comment_text = request.form.get("comment", "").strip()
        
        # Validação simples de entrada
        if comment_text:
            sentiment, score = analyze_sentiment(comment_text)
            save_comment(comment_text, sentiment, score)
            
        return redirect(url_for("index"))

    comments = get_all_comments()
    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    app.run(debug=True)