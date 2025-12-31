import streamlit as st
from styles import get_css
from db_manager import init_db, salvar_contato, listar_mensagens

# Configurações de Página
st.set_page_config(page_title="LZWorldsTech | Portfólio", page_icon="🚀", layout="wide")
st.markdown(get_css(), unsafe_allow_html=True)
init_db()

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("LZWorldsTech")
    # Tente carregar a logo local, se não existir, usa placeholder
    try:
        st.image("assets/logo.png")
    except:
        st.image("https://via.placeholder.com/150/00f2ff/000000?text=LZ")
    
    st.markdown("### 📱 Redes & Contato")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/luiz-otavio-valenzi-sousa-1180bb360/)")
    st.markdown("[📸 Instagram](https://www.instagram.com/lzworldstech/)")
    st.markdown("[🟢 WhatsApp](https://wa.me/5535999215995)")
    st.write("📞 (35) 99921-5995")
    
    st.divider()
    menu = st.radio("Navegar por:", ["Sobre Mim", "Projetos", "Dashboard Admin"])

# --- SEÇÃO: SOBRE MIM ---
if menu == "Sobre Mim":
    st.title("🚀 Luiz Otávio Valenzi Sousa")
    st.markdown("email:valenzisousaluizotavio@gmail.com")
    st.markdown("Idade: 22 anos")
    st.markdown("### <span class='neon-blue'>Engenheiro de Software & Desenvolvedor de aplicativos e sites</span>", unsafe_allow_html=True)
    st.markdown("Cidade: Pouso Alegre - MG")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("📖 Minha História")
        st.write("""
        Sou um apaixonado por tecnologia e desenvolvimento de sistemas que iniciou sua trajetória em 2020. 
        Tenho foco total em criar ferramentas que tragam eficiência para negócios reais. 
        Minha base técnica é sólida e busco constantemente novas tecnologias para resolver problemas complexos.
        """)
        
        st.header("🎓 Formação Acadêmica")
        st.markdown(f"""
        * **Técnico em Informática** <span class='neon-purple'>Instituto Federal (IFSULDEMINAS) - Campus Pouso Alegre MG</span>  
            *Período: 2020 - 2023*
        
        * **Engenharia de Software (Bacharelado)** <span class='neon-purple'>Faculdade Anhanguera Pouso Alegre MG</span>  
            *Período: 2023 - 2026*
        """, unsafe_allow_html=True)

    with col2:
        st.header("🛠️ Skills")
        st.markdown("""
        - **Linguagens:** Python, HTML, CSS, JavaScript, Java
        - **Frameworks:** Django, Streamlit
        - **Banco de Dados:** MySQL, SQLite
        - **Habilidades:** Comunicação, Aprendizado Rápido, Desenvolvimento de Projetos.
        """)

# --- SEÇÃO: PROJETOS ---
# --- SEÇÃO: PROJETOS ---
elif menu == "Projetos":
    st.title("💻 Projetos Finalizados")
    st.write("Conheça os sistemas desenvolvidos pela LZWorldsTech que já estão operando com sucesso.")
    
    # --- PROJETO 1: CORES E FRAGRÂNCIAS ---
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        col_img1, col_txt1 = st.columns([1.2, 2])
        
        with col_img1:
            try:
                # Carrega a imagem da pasta assets/
                st.image("assets/cores_fragrancias.png", use_container_width=True)
            except:
                st.warning("📷 Foto do projeto 'Cores e Fragrâncias' não encontrada em assets/")
        
        with col_txt1:
            st.markdown("### <span class='neon-blue'>Cores e Fragrâncias by Berenice</span>", unsafe_allow_html=True)
            st.write("""
            **Descrição:** Aplicação robusta para gestão empresarial, focada no controle de estoque e monitoramento de vendas em tempo real. 
            Desenvolvido sob medida para a loja Cores e Fragrâncias by Berenice.
            """)
            st.markdown("<span class='neon-pink'>Status: Projeto Finalizado</span>", unsafe_allow_html=True)
            st.markdown("[🚀 Acessar Sistema Online](https://coresefragranciasbybereniceloja.streamlit.app/)")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- PROJETO 2: NTB CALIBRATION ---
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        col_img2, col_txt2 = st.columns([1.2, 2])
        
        with col_img2:
            try:
                # Carrega a imagem da pasta assets/
                st.image("assets/ntb_calibration.png", use_container_width=True)
                st.image("assets/ntb-inicio.png", use_container_width=True)
                st.image("assets/ntb-usuarioadministrador.png", use_container_width=True)
                st.image("assets/ntb-usuarionormal.png", use_container_width=True)
                st.image("assets/ntb-laudostecnicos.png", use_container_width=True)
                st.image("assets/ntb-perfil.png", use_container_width=True)
                st.image("assets/ntb-paineladministrativo (1).png", use_container_width=True)
                st.image("assets/ntb-paineladministrativo (2).png", use_container_width=True)
                st.image("assets/ntb-paineladministrativo (3).png", use_container_width=True)
            except:
                st.warning("📷 Foto do projeto 'NTB Calibration' não encontrada em assets/")
        
        with col_txt2:
            st.markdown("### <span class='neon-blue'>NTB Calibration</span>", unsafe_allow_html=True)
            st.write("""
            **Descrição:** Aplicativo focado em laudos técnicos e serviços de engenharia, desenvolvido em parceria com a NTB Engenharia e Serviços. 
            Otimiza a coleta de dados e geração de relatórios técnicos.
            """)
            st.markdown("<span class='neon-pink'>Status: Projeto Finalizado</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- FORMULÁRIO DE CONTATO ---
    st.divider()
    st.header("📩 Inicie um Projeto Comigo")
    st.write("Fale diretamente com a LZWorldsTech preenchendo o formulário abaixo.")
    
    with st.form("contato_direto"):
        nome = st.text_input("Seu Nome")
        email = st.text_input("Seu Email ou WhatsApp")
        mensagem = st.text_area("Como posso ajudar no seu próximo software?")
        
        btn_enviar = st.form_submit_button("Enviar Mensagem")
        
        if btn_enviar:
            if nome and email and mensagem:
                salvar_contato(nome, email, mensagem)
                st.balloons()
                st.success(f"Excelente, {nome}! Seus dados foram salvos. Entrarei em contato em breve!")
            else:
                st.error("Por favor, preencha todos os campos para enviar.")
# --- SEÇÃO: DASHBOARD ADMIN ---
elif menu == "Dashboard Admin":
    st.title("🔐 Dashboard de Mensagens")
    st.write("Área exclusiva para Luiz Otávio visualizar contatos do site.")
    
    senha = st.text_input("Senha de Acesso", type="password")
    if senha == "lz2025": # Altere sua senha aqui
        df = listar_mensagens()
        if not df.empty:
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhuma mensagem recebida ainda.")
    elif senha:
        st.error("Senha incorreta.")


st.markdown("<br><center>LZWorldsTech © 2025</center>", unsafe_allow_html=True)



