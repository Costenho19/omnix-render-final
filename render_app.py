from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1 style="color: #00f5ff; text-align: center; font-family: Arial;">OMNIX</h1>
    <h2 style="text-align: center; color: white; background: #1a1a2e; padding: 20px;">Sistema de Trading Automático</h2>
    <div style="background: #1a1a2e; color: white; padding: 50px; text-align: center;">
        <p>🤖 Sistema IA: OPERATIVO</p>
        <p>📈 Trading Engine: ACTIVO</p>
        <p>💰 Balance USD: $14.19</p>
        <p>🎯 Win Rate: 67.8%</p>
        <p><strong>Valoración: $2,000,000 USD</strong></p>
        <p>Harold Nunes - OMNIX Global Bot</p>
    </div>
    """

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
