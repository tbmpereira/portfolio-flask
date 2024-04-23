from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import username, password

app = Flask(__name__)
app.secret_key = "tbmpereira"

mail_settings = {
    "MAIL_SERVER": 'live.smtp.mailtrap.io',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": username,
    "MAIL_PASSWORD": password
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        contato = Contato(nome, email, mensagem)

        msg = Message(
            subject= f'{nome} te mandou uma mensagem pelo site!',
            sender= app.config.get("MAIL_USERNAME"),
            recipients=['mpereiraufv@gmail.com'],
            body=f'''
            Nome: {contato.nome}
            Email: {contato.email}
            Mensagem: {contato.mensagem}
            '''
        )

        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
