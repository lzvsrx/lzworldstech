def get_css():
    return """
    <style>
    /* Fundo Gradiente Tech */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #06061a 50%, #1a0033 100%);
    }

    /* Títulos com Efeito Glow */
    h1, h2, h3 {
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff;
        font-family: 'Courier New', monospace;
    }

    /* Cores Neon Específicas */
    .neon-purple { color: #bc13fe; text-shadow: 0 0 8px #bc13fe; font-weight: bold; }
    .neon-pink { color: #ff00ff; text-shadow: 0 0 8px #ff00ff; }
    .neon-orange { color: #ff8c00; text-shadow: 0 0 8px #ff8c00; }
    .neon-blue { color: #00f2ff; text-shadow: 0 0 8px #00f2ff; }

    /* Cartão de Projeto Futurista */
    .project-card {
        border: 1px solid #00f2ff;
        padding: 25px;
        border-radius: 15px;
        background: rgba(0, 242, 255, 0.03);
        margin-bottom: 25px;
        transition: 0.4s ease;
    }
    .project-card:hover {
        box-shadow: 0 0 25px rgba(188, 19, 254, 0.5);
        border-color: #bc13fe;
        transform: translateY(-5px);
    }

    /* Estilo de links e botões */
    a { text-decoration: none; font-weight: bold; }
    .stButton>button {
        background: linear-gradient(45deg, #bc13fe, #00f2ff);
        color: white;
        border: none;
        box-shadow: 0 0 10px rgba(0, 242, 255, 0.5);
    }
    </style>
    """