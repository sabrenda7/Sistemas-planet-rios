import streamlit as st
import pandas as pd
import numpy as np
from astropy import constants as const
from astropy import units as u

# Configuração da página
st.set_page_config(page_title="Parâmetros exoplanetários", layout="wide")

# Sidebar para navegação
st.sidebar.header("Navegue")
pagina = st.sidebar.radio("Selecione a página:", ["Introdução", "Calculadora"])

if pagina == "Introdução":
    st.title("Parâmetros exoplanetários")
    st.write("Trabalho de determinação de parâmetros exoplanetários utilizando dados de velocidade radial e de trânsito")
    st.subheader("Exoplanetas escolhidos para este trabalho")
    st.text("Para a realização deste trabalho, foram escolhidos dois exoplanetas. Um deles é o HD 209458b, que foi o primeiro exoplaneta a ser detectado e confirmado pelos métodos de velocidade radial e de transito. O outro exoplaneta é o LHS 1140b que vem sendo estudado como um planeta potencialmente habitável. Ao lado, há um navegador onde é possível escolher um dos dois sitemas escolhidos para este determinar seus parâmetros ou personalizar os dados para calcular os parâmetros de algum outro exoplaneta de interesse.")
    
    img_col2, img_col3= st.columns(2)        
    with img_col2:
        st.image("images/capa.png", width=400, caption="Ilustração do sistema HD 209458")
    with img_col3:
        st.image("images/superterra.jpg", width=350, caption="Ilustação do LHS 1140b, considerado uma Super Terra potencialmente habitável.")

    st.subheader("HD 209458b")
    st.image("images/ilustracao.jpg", width=250, caption="Ilustração dramática do planeta HD 209458b queimando em sua orbita")
    st.text("Este foi o pioneiro dos exoplanetas descobertos e confirmados pelos métodos de velocidade radial e de trânsito planetário. Também foi o primeiro exoplaneta onde foi detectada uma atmosfera. Ele é um gigante gasoso e está orbitando muito próximo de sua estrela hospedeira. Em 2003, astrônomos descobriram que o HD 209458b está perdendo sua atmosfera." \
    " A estrela hospederia, conhecida como V376 Pegasi, é bem parecida com a nossa estrela Sol, não é visivel a olho nu mas pode ser encontrada facilmete usando um binóculo ou telescópio. Ela está localizada na constelação de Pegasus.")
    imge_col1, imge_col2= st.columns(2)        
    with imge_col1:
        st.image("images/radialhd.gif", width=400, caption="Velocidades para HD 209458 (anã G0). A linha sólida é um ajuste sinusoidal com um período de 3,5239 dias e uma semiamplitude de 81 m s-1, resultando em uma massa mínima M sen i = 0,62 MJup para o companheiro. O rms do ajuste sinusoidal é de 2,27 m s-1, menor do que os erros esperados de 3,7 m s-1.")
    with imge_col1:
        st.image("images/transito hd.gif", width=400, caption="Observações fotométricas de HD 209458 da noite de 7 de novembro de 1999 UT mostrando a entrada do trânsito planetário. A profundidade de passagem medida é 0,017±0,002 mag ou 1,58%±0,18%. A barra de erro mostra o tempo de conjunção inferior e sua incerteza prevista a partir das velocidades radiais nesta Carta.")
    
    st.subheader("LHS 1140b")
    st.image("images/esolhs.jpg", width=350, caption="Ilustração artística do sistema LHS 1140.")
    st.text("O LHS 1140b foi descoberto em 2017 pelo método da trânsito planetário, e foi confirmado pelo método de velocidade radial. Ele é um planeta rochoso assim como a Terra e está orbitando na zona habitável de uma anã vermelha, a LHS 1140, localizada na constelação de Cetus. Dadas suas características parecidas com as da Terra, esse exoplaneta vem sendo visto como um forte candidato para a busca de vida extraterrestre. A estrela LHS 1140 não é visível a olho nu, mas é um alvo prioritário para o Telescópio Espacial James Webb.")
    lhs_col1, lhs_col2= st.columns(2)
    with lhs_col1:
        st.image("images/radial_lhs.jpg", width= 400, caption= "Velocidade radial do LHS 1140 dos conjuntos de dados HARPS (vermelho) e ESPRESSO (aberto para ESPRESSOpre e preenchido para ESPRESSOpost em verde). A linha preta mostra o modelo de velocidade radial mediana da análise fotométrica e de velocidade radial conjunta. As regiões sombreadas em cinza correspondem aos intervalos de confiança de 68,7% (cinza escuro) e 95% (cinza claro) do modelo. O modelo GP mediano é mostrado como uma linha azul tracejada. Meio: conjunto de dados de velocidade radial após a remoção do modelo GP mediano. O modelo Kepleriano é mostrado como uma linha preta sólida. Abaixo: resíduos de velocidade radial do modelo completo.")
    with lhs_col2:
         st.image("images/transitolhs.jpg", width= 400, caption= "Trânsito da curva de luz branca de LHS 1140 b com o WFC3 no HST. O modelo de transporte de transporte de melhor ajuste é mostrado em azul, com os resíduos do ajuste mostrados no painel inferior.")

    # Dados da tabela
    dados = {
        "": [
            "Transit Depth [%]",
            "Radial Velocity Amplitude [m/s]",
            "Orbital Period [days]",
            "Discovery Method",
            "Discovery Telescope",
            "Discovery Instrument",
            "Orbit Semi-Major Axis [au]",
            "Planet Radius [Earth Radius]",
            "Planet Mass [Earth Mass]",
            "Eccentricity",
            "Insolation Flux [Earth Flux]",
            "Equilibrium Temperature [K]",
            "Inclination [deg]",
            "Transit Duration [hours]",
            "Spectral Type",
            "Stellar Effective Temperature [K]",
            "Stellar Mass [Solar mass]",
            "Stellar Radius [Solar Radius]"
        ],
        "HD 209458 b": [
            "1.5000±0.0024",
            "84.7±0.7",
            "3.52474859±0.00000038",
            "Radial Velocity",
            "10 m Keck I Telescope",
            "HIRES Spectrometer",
            "",
            "15.6±0.2",
            "",
            "0.0",
            "",
            "",
            "86.71±0.05",
            "",
            "",
            "6091±10",
            "1.23±0.09",
            "1.19±0.02"
        ],
        "LHS 1140 b": [
            "0.538±0.006",
            "3.80±0.11",
            "24.73723±0.00002",
            "Transit",
            "0.4 m MEarth Telescope",
            "Apogee CCD Sensor",
            "0.0946±0.0017",
            "1.730±0.025",
            "5.60±0.19",
            "<0.043",
            "0.43±0.03",
            "226±4",
            "89.86±0.04",
            "2.15±0.05",
            "M4.5 V",
            "3096±48",
            "0.1844±0.0045",
            "0.2159±0.0030"
        ]
    }

    df = pd.DataFrame(dados)

    # Estilo CSS para a tabela
    st.markdown("""
    <style>
    table {
        border-collapse: collapse;
        width: 100%;
        background-color: #ffe6f0;
        text-align: center;
        font-size: 16px;
    }
    th {
        background-color: #800080;
        color: white;
        padding: 8px;
        text-align: center;
    }
    td {
        border: 1px solid #800080;
        padding: 6px;
    }
    tr:nth-child(even) {
        background-color: #f2b3d1;
    }
    caption {
        font-size: 20px;
        font-weight: bold;
        margin: 10px;
        color: #800080;
    }
    </style>
    """, unsafe_allow_html=True)

    # Exibir a tabela de dados
    st.header("Dados de entrada")
    st.subheader("Dados obtidos utilizando o Nasa Archive")
    st.text('Após buscas simples na base de dados Nasa Archive, foram obtidos os seguintes dados:')

    html_tabela = df.to_html(index=False, escape=False)
    html_tabela = html_tabela.replace("<table", "<table caption='Dados de entrada'")
    st.markdown(html_tabela, unsafe_allow_html=True)
    st.text('Para prosseguir, use o botão de navegação ao lado.')

else:
    # Constantes fundamentais
    R_sun = const.R_sun.value  # Raio solar em metros
    M_sun = const.M_sun.value  # Massa solar em kg
    R_jup = const.R_jup.value  # Raio de Júpiter em metros
    M_jup = const.M_jup.value  # Massa de Júpiter em kg
    R_earth = const.R_earth.value  # Raio terrestre em metros
    M_earth = const.M_earth.value  # Massa terrestre em kg
    AU = const.au.value  # Unidade astronômica em metros
    G = const.G.value  # Constante gravitacional
    sigma = const.sigma_sb.value  # Constante de Stefan-Boltzmann
    S_0 = 1361  # Constante solar (W/m²)

    # Sidebar para seleção do sistema planetário
    st.sidebar.header("Seleção do Sistema Planetário")
    sistema = st.sidebar.selectbox(
        "Escolha o sistema planetário:",
        ("HD 209458 b", "LHS 1140 b", "Personalizado")
    )

    # Função para extrair valores numéricos dos dados com incertezas
    def extract_value(value_str):
        if "±" in value_str:
            return float(value_str.split("±")[0])
        elif "<" in value_str:
            return float(value_str.split("<")[1])
        elif value_str == "":
            return None
        else:
            return float(value_str)

    # Parâmetros padrão para cada sistema
    if sistema == "HD 209458 b":
        st.sidebar.info("Sistema HD 209458 (planeta HD 209458 b - 'Osiris')")
        
        # Extrair valores da tabela
        depth_val = extract_value("1.5000±0.0024")
        K_val = extract_value("84.7±0.7")
        P_val = extract_value("3.52474859±0.00000038")
        R_planet_val = extract_value("15.6±0.2")
        i_val = extract_value("86.71±0.05")
        T_star_val = extract_value("6091±10")
        M_star_val = extract_value("1.23±0.09")
        R_star_val = extract_value("1.19±0.02")
        
        # Parâmetros da estrela HD 209458
        M_star = M_star_val if M_star_val else 1.23
        R_star = R_star_val if R_star_val else 1.19
        T_star = T_star_val if T_star_val else 6091
        # Calcular luminosidade estelar usando a relação L ∝ R²T⁴
        L_star = (R_star ** 2) * (T_star / 5778) ** 4  # Luminosidade em L☉
        
        # Parâmetros do planeta HD 209458 b
        P = P_val if P_val else 3.52474859
        # Calcular semi-eixo maior usando a 3ª lei de Kepler
        a = ((P / 365.25) ** 2 * M_star) ** (1/3)  # em UA
        e = 0.0
        i = i_val if i_val else 86.71
        omega = 0.0
        # Calcular massa do planeta a partir da amplitude RV
        if K_val:
            M_planet_sini = (K_val * (M_star * M_sun) ** (2/3) * np.sin(i * np.pi/180) * 
                            (P * 24 * 3600 / (2 * np.pi * G)) ** (1/3)) / M_earth
            M_planet = M_planet_sini / np.sin(i * np.pi/180)
        else:
            M_planet = 232.0  # Massa planetária em M⊕ (0.73 M_jup)
        
        R_planet = R_planet_val if R_planet_val else 15.6
        albedo = 0.3
        K = K_val if K_val else 84.7
        depth = depth_val if depth_val else 1.5

    elif sistema == "LHS 1140 b":
        st.sidebar.info("Sistema LHS 1140 (planeta LHS 1140 b)")
        
        # Extrair valores da tabela
        depth_val = extract_value("0.538±0.006")
        K_val = extract_value("3.80±0.11")
        P_val = extract_value("24.73723±0.00002")
        a_val = extract_value("0.0946±0.0017")
        R_planet_val = extract_value("1.730±0.025")
        M_planet_val = extract_value("5.60±0.19")
        flux_val = extract_value("0.43±0.03")
        T_eq_val = extract_value("226±4")
        i_val = extract_value("89.86±0.04")
        T_star_val = extract_value("3096±48")
        M_star_val = extract_value("0.1844±0.0045")
        R_star_val = extract_value("0.2159±0.0030")
        
        # Parâmetros da estrela LHS 1140
        M_star = M_star_val if M_star_val else 0.184
        R_star = R_star_val if R_star_val else 0.216
        T_star = T_star_val if T_star_val else 3096
        # Calcular luminosidade estelar usando a relação L ∝ R²T⁴
        L_star = (R_star ** 2) * (T_star / 5778) ** 4  # Luminosidade em L☉
        
        # Parâmetros do planeta LHS 1140 b
        P = P_val if P_val else 24.737
        a = a_val if a_val else 0.0946
        e = 0.0
        i = i_val if i_val else 89.86
        omega = 0.0
        M_planet = M_planet_val if M_planet_val else 5.60
        R_planet = R_planet_val if R_planet_val else 1.73
        albedo = 0.3
        K = K_val if K_val else 3.80
        depth = depth_val if depth_val else 0.538
        flux = flux_val if flux_val else 0.43
        T_eq = T_eq_val if T_eq_val else 226

    else:  # Personalizado
        st.sidebar.info("Sistema Personalizado")
        
        # Parâmetros da estrela
        st.sidebar.subheader("Parâmetros Estelares")
        M_star = st.sidebar.number_input("Massa estelar (M☉)", min_value=0.01, value=1.0, step=0.01)
        R_star = st.sidebar.number_input("Raio estelar (R☉)", min_value=0.01, value=1.0, step=0.01)
        T_star = st.sidebar.number_input("Temperatura estelar (K)", min_value=2000, value=5778, step=50)
        # Calcular luminosidade estelar
        L_star = (R_star ** 2) * (T_star / 5778) ** 4

        # Parâmetros do planeta
        st.sidebar.subheader("Parâmetros Planetários")
        P = st.sidebar.number_input("Período orbital (dias)", min_value=0.1, value=365.25, step=1.0)
        a = st.sidebar.number_input("Semi-eixo maior (UA)", min_value=0.01, value=1.0, step=0.01)
        e = st.sidebar.number_input("Excentricidade orbital", min_value=0.0, max_value=0.99, value=0.0, step=0.01)
        i = st.sidebar.number_input("Inclinação orbital (graus)", min_value=0.0, max_value=90.0, value=90.0, step=0.1)
        omega = st.sidebar.number_input("Argumento do periastro (graus)", min_value=0.0, max_value=360.0, value=0.0, step=1.0)
        M_planet = st.sidebar.number_input("Massa planetária (M⊕)", min_value=0.01, value=1.0, step=0.01)
        R_planet = st.sidebar.number_input("Raio planetário (R⊕)", min_value=0.01, value=1.0, step=0.01)
        albedo = st.sidebar.number_input("Albedo", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
        K = st.sidebar.number_input("Amplitude de velocidade radial (m/s)", min_value=0.0, value=10.0, step=0.1)
        depth = st.sidebar.number_input("Profundidade do trânsito (%)", min_value=0.0, value=1.0, step=0.01)

    # Exibir os parâmetros do sistema selecionado
    st.header(f"Parâmetros do Sistema {sistema}")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Estrela")
        st.write(f"Massa: {M_star} M☉")
        st.write(f"Raio: {R_star} R☉")
        st.write(f"Temperatura: {T_star} K")
        st.write(f"Luminosidade: {L_star:.4f} L☉")
        st.image("exoplanetas/exoplanet.jpg", width=400)

    with col2:
        st.subheader("Planeta")
        st.write(f"Período orbital: {P} dias")
        st.write(f"Semi-eixo maior: {a} UA")
        st.write(f"Excentricidade: {e}")
        st.write(f"Inclinação: {i}°")
        st.write(f"Massa: {M_planet} M⊕")
        st.write(f"Raio: {R_planet} R⊕")
        st.write(f"Albedo: {albedo}")
        if sistema != "Personalizado":
            st.write(f"Amplitude RV: {K} m/s")
            st.write(f"Profundidade do trânsito: {depth}%")
            if sistema == "LHS 1140 b":
                st.write(f"Fluxo de insolação: {flux} S⊕")
                st.write(f"Temperatura de equilíbrio: {T_eq} K")

    # Conversões de unidades
    P_sec = P * 24 * 3600  # Período em segundos
    a_m = a * AU  # Semi-eixo maior em metros
    i_rad = np.radians(i)  # Inclinação em radianos
    omega_rad = np.radians(omega)  # Argumento do periastro em radianos

    # Cálculos
    st.header("Resultados dos Cálculos")

     # 1. Determinação do semi-eixo maior do planeta via lei de Kepler
    st.subheader("1. Semi-eixo maior do planeta via lei de Kepler")
    st.text("Com as massas em massas solares, o período em anos e o semi-eixo maior em unidades astrônomicas,utilizamos a terceira lei de Kepler generalizada para obter o semi-eixo maior (a) do planeta.")
    st.latex(r"a = \sqrt[3]{\frac{G(M_* + M_p)P^2}{4\pi^2}}")
    st.text("Onde, ")
    st.latex(r"G= \text{constante gravitacional}")
    st.latex(r"P= \text{período}")
    st.latex(r"a= \text{semi-eixo maior}")
    st.latex(r"M_*= \text{massa da estrela}")
    st.latex(r"M_p= \text{massa da planeta}")
    a_kepler = (G * (M_star * M_sun + M_planet * M_earth) * (P_sec)**2 / (4 * np.pi**2))**(1/3)
    st.text("Com isso, obtemos os seguntes resultados:")
    st.write(f"a_kepler = {a_kepler/AU:.6f} UA")
    st.write(f"a_kepler = {a_kepler:.3e} m")

    # 2. Determinação do semi-eixo maior do baricentro do sistema
    st.subheader("2. Semi-eixo maior do baricentro do sistema")
    st.text("O semi-eixo maior do baricentro é dado pela equação:")
    st.latex(r"a_{\text{barycenter}} = a \cdot \frac{M_p}{M_* + M_p}")
    st.text("Onde,")
    st.latex(r"a= \text{semi-eixo maior}")
    st.latex(r"M_*, M_p = \text{já conhecemos do item anterior}")
    a_barycenter = a_m * M_planet * M_earth / (M_star * M_sun + M_planet * M_earth)
    st.text("Resultados obtidos:")
    st.write(f"a_barycenter = {a_barycenter/AU:.8f} UA")
    st.write(f"a_barycenter = {a_barycenter:.3e} m")

    # 3. Determinação da massa do planeta
    st.subheader("3. Massa do planeta")
    st.text("Para obter a massa do planeta, podemos usar a seguinte relação:")
    st.latex(r"M_p = \frac{K (M_*)^{2/3} \sin i}{G^{1/3}} \left( \frac{P}{2\pi} \right)^{1/3} \frac{1}{\sqrt{1-e^2}}")
    st.text("Onde,")
    st.latex(r"K= \text{semiamplitude da velocidade radial}")
    st.latex(r"i= \text{inclinação da órbita(assumimos 90°)}")
    st.latex(r"e= \text{excentricidade da órbita}")
    st.text("Os demais componentes já são conhecidos.")
    st.text("Resultados obtidos:")
    st.write(f"M_planeta = {M_planet:.3f} M⊕")
    st.write(f"M_planeta = {M_planet * M_earth/M_jup:.6f} M_jup")

    # 4. Determinação do raio do planeta
    st.subheader("4. Raio do planeta")
    st.text("Para obter o raio do planeta podemos usar a variação do fluxo de luz da estrela (\u2206F) durante o trânsito planetário, fazendo a seguinte relação:")
    st.latex(r"R_p = R_* \sqrt{\frac{\Delta F}{F}}")
    st.text("Onde,")
    st.latex(r"R_p = \text{Raio do planeta}")
    st.latex(r"R_* = \text{Raio da estrela}")
    st.latex(r"F= \text{Fluxo de luminosidade da estrela}")
    st.latex(r"\Delta F= \text{Variação do fluxo de luminosidade}")
    st.text("Assim, obtemos:")
    st.write(f"R_planeta = {R_planet:.3f} R⊕")
    st.write(f"R_planeta = {R_planet * R_earth/R_jup:.6f} R_jup")

    # 5. Determinação da probabilidade de trânsito do planeta
    st.subheader("5. Probabilidade de trânsito do planeta")
    st.text("A probabilidae do trânsito ocorrer será proporcional ao raio da planeta com o raio da estrela e o semi-eixo maior, da seguinte maneira:")
    st.latex(r"P_{\text{transit}} = \frac{R_* + R_p}{a}")
    P_transit = (R_star * R_sun + R_planet * R_earth) / a_m

    st.text("A probabilidade do trânsio ocorrer será:")
    st.write(f"P_transit = {P_transit:.6f}")
    st.write(f"Probabilidade = {P_transit * 100:.4f}%")

    # 6. Determinação do tempo de trânsito do planeta
    st.subheader("6. Tempo de trânsito do planeta")
    st.text("Para o cálculo do tempo de trânsito do planeta, foi usada a equação abaixo:")
    st.latex(r"T_{\text{duration}} = \frac{P}{\pi} \arcsin\left( \frac{\sqrt{(R_* + R_p)^2 - (a \cos i)^2}}{a \sin i} \right)")
    # Corrigindo o cálculo do tempo de trânsito
    b = a_m * np.cos(i_rad) / (R_star * R_sun)  # Parâmetro de impacto
    T_duration = (P_sec / np.pi) * np.arcsin(np.sqrt((R_star * R_sun + R_planet * R_earth)**2 - 
                                                   (b * R_star * R_sun)**2) / (a_m * np.sin(i_rad)))
    T_duration_hours = T_duration / 3600
    st.text("Resultado obtido:")
    st.write(f"T_duration = {T_duration_hours:.3f} horas")

    # 7. Determinação do grau de insolação do planeta
    st.subheader("7. Grau de insolação do planeta")
    st.text("O grau de insolação do planeta é proporcional a luminosidade (L) da estrela e inversamente proporcional ao quadrado da distância entre o planeta e a estrela.")
    st.latex(r"S_p = \frac{L_*}{4\pi a^2}")
    S_p = L_star * S_0 / a**2
    st.text("Resultados obtidos:")
    st.write(f"S_p = {S_p:.3f} W/m²")
    st.write(f"S_p/S_0 = {S_p/S_0:.3f}")

    # 8. Determinação da temperatura de equilíbrio do planeta
    st.subheader("8. Temperatura de equilíbrio do planeta")
    st.text("Podemos obter a temperatura de equilibrio do planeta pla seguinte equação:")
    st.latex(r"T_{\text{eq}} = T_* \sqrt{\frac{R_*}{2a}} (1 - A)^{1/4}")
    T_eq_calc = T_star * np.sqrt(R_star * R_sun / (2 * a_m)) * (1 - albedo)**0.25
    st.text("Onde,")
    st.latex(r"T_{\text{eq}} = \text{temperatura de equilíbrio}")
    st.latex(r"T_* = \text{Temperatura da estrela}")
    st.latex(r"A = \text{Albedo}")
    st.text("Os demais dados já foram apresentados.")
    st.text("Resultados obtidos:")
    st.write(f"T_eq = {T_eq_calc:.2f} K")
    st.write(f"T_eq = {T_eq_calc - 273.15:.2f} °C")

    # 9. Determinação da zona de habitabilidade da estrela
    st.subheader("9. Zona de habitabilidade da estrela")
    st.text("A zona de habitabilidade de uma estrela é proporconal a sua luminosidade.")
    st.latex(r"d = \sqrt{L_*} \cdot d_{\oplus}")
    st.text("Onde,")
    st.latex(r"L_*= \text{luminosidade da estrela}")
    st.latex(r"d_{\odot}= \text{referência de zona habitável no sitema solar}")
    d_inner = 0.75 * np.sqrt(L_star)
    d_center = 1.0 * np.sqrt(L_star)
    d_outer = 1.77 * np.sqrt(L_star)
    st.text("Os resultados obtidos foram:")
    st.write(f"Zona habitável interna: {d_inner:.3f} UA")
    st.write(f"Zona habitável central: {d_center:.3f} UA")
    st.write(f"Zona habitável externa: {d_outer:.3f} UA")

    # 10. Discussão da densidade planetária em relação aos corpos do sistema solar
    st.subheader("10. Densidade planetária em comparação")
    st.latex(r"\rho_p = \frac{M_p}{\frac{4}{3}\pi R_p^3}")
    rho_planet = (M_planet * M_earth) / (4/3 * np.pi * (R_planet * R_earth)**3)
    rho_earth = 5514  # kg/m³
    rho_jupiter = 1326  # kg/m³
    rho_saturn = 687   # kg/m³
    rho_neptune = 1638  # kg/m³
    rho_uranus = 1270  # kg/m³

    st.write(f"Densidade do planeta: {rho_planet:.1f} kg/m³")
    st.write(f"Densidade da Terra: {rho_earth} kg/m³")
    st.write(f"Densidade de Júpiter: {rho_jupiter} kg/m³")
    st.write(f"Densidade de Saturno: {rho_saturn} kg/m³")
    st.write(f"Densidade de Netuno: {rho_neptune} kg/m³")
    st.write(f"Densidade de Urano: {rho_uranus} kg/m³")

    # Interpretação da densidade
    if rho_planet > 5000:
        interpretation = "O valor da densidade encontrado está mais próximo da densidade da Terra. Provavelmente este é um planeta rochoso, similar à Terra."
    elif 2000 < rho_planet <= 5000:
        interpretation = "Possivelmente um planeta oceânico ou com composição mista."
    elif 1000 < rho_planet <= 2000:
        interpretation = "O valor da densidade encontrado está mais próximo da densidade de gigantes de gelo do sitema solar. Provavelmente esteé um gigante gelado, similar a Netuno ou Urano."
    else:
        interpretation = "O valor da densidade encontrado está mais próximo da densidade de Saturno. Provavelmente este planeta é um gigante gasoso, similar a Júpiter ou Saturno."

    st.write(f"**Interpretação**: {interpretation}")

    # Adicionar comparação com valores da tabela quando aplicável
    if sistema != "Personalizado":
        st.header("Comparação com Valores da Tabela")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Valores Calculados")
            st.write(f"Profundidade do trânsito: {(R_planet * R_earth / (R_star * R_sun))**2 * 100:.3f}%")
            st.write(f"Amplitude RV: {K} m/s")
            if sistema == "LHS 1140 b":
                st.write(f"Fluxo de insolação: {S_p/S_0:.2f} S⊕")
                st.write(f"Temperatura de equilíbrio: {T_eq_calc:.0f} K")
        
        with col2:
            st.subheader("Valores da Tabela")
            st.write(f"Profundidade do trânsito: {depth}%")
            st.write(f"Amplitude RV: {K} m/s")
            if sistema == "LHS 1140 b":
                st.write(f"Fluxo de insolação: {flux} S⊕")

                st.write(f"Temperatura de equilíbrio: {T_eq} K")
