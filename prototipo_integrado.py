
import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#1.  DICCIONARIO DE PALABRAS
#RASGOS LEXICOS
lexico_emocional = [
    "miedo",
    "indignación",
    "rabia",
    "horror",
    "pánico",
    "amenaza",
    "dolor",
    "odio",
    "escándalo"
]

lexico_valorativo =[
     "terrible",
     "vergonzoso",
     "inaceptable",
     "lamentable",
     "brutal",
     "repugnante",
     "corrupto",
     "criminal",
     "fraude"
]

lexico_alarmista = [
     "urgente",
     "alerta",
     "peligro",
     "catástrofe",
     "crisis",
     "emergencia",
     "última hora"
]

intensificadores =[
     "muy",
     "totalmente",
     "absolutamente",
     "completamente",
     "extremadamente",
     "realmente",
     "sin precedentes",
     "jamás visto"
]
palabras_certeza = [
    "confirmado",
    "demostrado",
    "sin duda",
    "está claro",
    "es evidente",
    "la verdad",
    "siempre",
    "nunca",
    "es un hecho",
    "no hay duda"
]

palabras_generalización = [
    "todos",
    "nadie",
    "siempre",
    "nunca",
    "todo el mundo",
    "la gente",
    "los medios",
    "los políticos",
    "la población",
    "ninguno"
]

palabras_estrategia = [
    "comparte",
    "difunde",
    "hazlo viral",
    "antes de que lo borren",
    "no quieren que lo sepas",
    "nos ocultan",
    "te están engañando",
    "despierta",
    "abre los ojos",
    "ellos"
]

#RASGOS DISCURSIVOS
afirmaciones_categoricas =[
     "es un hecho",
     "está demostrado",
     "no hay ninguna duda",
     "esto confirma",
     "la verdad es",
     "está claro que",
     "es evidente que"
]

marcadores_matizacion =[
     "quizá",
     "tal vez",
     "podría",
     "posiblemente",
     "aproximadamente",
     "según",
     "parece",
     "probablemente"
    
]

polarizacion_nosotros_ellos =[
     "nosotros",
     "ellos",
     "los nuestros",
     "los otros",
     "contra nosotros",
     "esa gente",
     "los de siempre"
]

llamadas_compartir = [
     "comparte",
     "difunde",
     "hazlo viral",
     "pásalo",
     "envíalo",
     "que todo el mundo lo sepa"
]

ocultamiento_informativo = [
     "no quieren que lo sepas",
     "nos ocultan",
     "lo están ocultando",
     "los medios callan",
     "la prensa no lo cuenta",
     "antes de que lo borren",
     "te están engañando"
     
]

marcadores_evidencia =[
    "según",
    "fuente",
    "fuentes",
    "informe",
    "estudio",
    "investigación",
    "datos",
    "estadística",
    "documento",
    "publicado por",
    "de acuerdo con"
]


#FUNCION PARA BUSCAR PALABRAS
def buscar_palabras(texto, lista_palabras):
    palabras_encontradas =[]
    for palabra in lista_palabras:
        if palabra.lower() in texto:
            palabras_encontradas.append(palabra)
    return palabras_encontradas

def calcular_puntuacion(palabras_encontradas):
    cantidad=len(palabras_encontradas)
    if cantidad == 0:
        return 0
    elif cantidad ==1:
        return 1
    else:
        return 2

#2. RASGOS NO LÉXICOS
def calcular_porcentaje_mayusculas(texto):
     letras =[
          caracter
          for caracter in texto
          if caracter.isalpha()
     ]

     if len(letras)== 0:
        return 0
     
     mayusculas = [
          letra
          for letra in letras
          if letra.isupper()
     ]
     return len(mayusculas) / len(letras) *100


def contar_repeticion_signos(texto):
    repeticiones = 0
    if "!!" in texto or "¡¡" in texto:
        repeticiones += 1
    if "??" in texto or "¿¿" in texto:
        repeticiones += 1
    return repeticiones          


# CORPUS Y MODELO
from pathlib import Path

# ESTABLECER RUTA ABSOLUTA DEL ARCHIVO
RUTA_BASE = Path(__file__).resolve().parent
RUTA_CORPUS = RUTA_BASE / "rubrica_corpus.xlsx"


@st.cache_data
def cargar_corpus():
    corpus = pd.read_excel(RUTA_CORPUS)
    corpus = corpus.dropna(subset=["Texto", "Grado"])
    corpus["Texto"] = corpus["Texto"].astype(str)
    corpus["Grado"] = (
        corpus["Grado"]
        .astype(str)
        .str.lower()
        .str.strip()
    )
    return corpus


@st.cache_resource
def entrenar_modelo(corpus):
    modelo = Pipeline([
        (
            "vectorizador",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2)
            )
        ),
        (
            "clasificador",
            LogisticRegression(max_iter=1000)
        )
    ])

    textos_entrenamiento, textos_prueba, grados_entrenamiento, grados_prueba = train_test_split(
        corpus["Texto"],
        corpus["Grado"],
        test_size=0.20,
        random_state=42,
        stratify=corpus["Grado"]
    )

    modelo.fit(textos_entrenamiento, grados_entrenamiento)
    predicciones_prueba = modelo.predict(textos_prueba)
    precision = accuracy_score(grados_prueba, predicciones_prueba)

    return modelo, precision


def analizar_publicacion(texto):
    texto_minusculas = texto.lower().strip()

    # Rasgos léxicos
    emocion_encontrada = buscar_palabras(texto_minusculas, lexico_emocional)
    valorativo_encontrado = buscar_palabras(texto_minusculas, lexico_valorativo)
    alarmista_encontrado = buscar_palabras(texto_minusculas, lexico_alarmista)
    intensificadores_encontrados = buscar_palabras(texto_minusculas, intensificadores)
    certeza_encontrada = buscar_palabras(texto_minusculas, palabras_certeza)
    generalizacion_encontrada = buscar_palabras(texto_minusculas, palabras_generalización)
    estrategia_encontrada = buscar_palabras(texto_minusculas, palabras_estrategia)

    # Rasgos formales
    numero_exclamaciones = texto.count("!") + texto.count("¡")
    numero_interrogaciones = texto.count("?") + texto.count("¿")
    numero_hashtags = texto.count("#")
    numero_menciones = texto.count("@")
    numero_enlaces = (
        texto_minusculas.count("http://")
        + texto_minusculas.count("https://")
        + texto_minusculas.count("www.")
    )
    porcentaje_mayusculas = calcular_porcentaje_mayusculas(texto)
    repeticion_signos = contar_repeticion_signos(texto)

    # Rasgos discursivos
    categoricas_encontradas = buscar_palabras(texto_minusculas, afirmaciones_categoricas)
    matizacion_encontrada = buscar_palabras(texto_minusculas, marcadores_matizacion)
    polarizacion_encontrada = buscar_palabras(texto_minusculas, polarizacion_nosotros_ellos)
    llamadas_encontradas = buscar_palabras(texto_minusculas, llamadas_compartir)
    ocultamiento_encontrado = buscar_palabras(texto_minusculas, ocultamiento_informativo)
    evidencia_encontrada = buscar_palabras(texto_minusculas, marcadores_evidencia)

    posible_interrogacion_retorica = numero_interrogaciones > 0

    ausencia_evidencia_explicita = (
        len(evidencia_encontrada) == 0
        and numero_enlaces == 0
        and len(categoricas_encontradas) > 0
    )

    falta_matizacion = (
        len(matizacion_encontrada) == 0
        and len(categoricas_encontradas) > 0
    )

    # Puntuación de emoción
    indicadores_emocion = (
        len(emocion_encontrada)
        + len(valorativo_encontrado)
        + len(alarmista_encontrado)
        + len(intensificadores_encontrados)
    )

    if numero_exclamaciones >= 2:
        indicadores_emocion += 1
    if porcentaje_mayusculas >= 30:
        indicadores_emocion += 1

    if indicadores_emocion == 0:
        puntuacion_emocion = 0
    elif indicadores_emocion <= 2:
        puntuacion_emocion = 1
    else:
        puntuacion_emocion = 2

    # Puntuación de certeza
    indicadores_certeza = len(certeza_encontrada) + len(categoricas_encontradas)
    if falta_matizacion:
        indicadores_certeza += 1

    if indicadores_certeza == 0:
        puntuacion_certeza = 0
    elif indicadores_certeza <= 2:
        puntuacion_certeza = 1
    else:
        puntuacion_certeza = 2

    # Puntuación de generalización
    indicadores_generalizacion = len(generalizacion_encontrada)

    if indicadores_generalizacion == 0:
        puntuacion_generalizacion = 0
    elif indicadores_generalizacion == 1:
        puntuacion_generalizacion = 1
    else:
        puntuacion_generalizacion = 2

    # Puntuación de estrategia discursiva
    indicadores_estrategia = (
        len(estrategia_encontrada)
        + len(polarizacion_encontrada)
        + len(llamadas_encontradas)
        + len(ocultamiento_encontrado)
    )

    if ausencia_evidencia_explicita:
        indicadores_estrategia += 1
    if posible_interrogacion_retorica:
        indicadores_estrategia += 1
    if repeticion_signos > 0:
        indicadores_estrategia += 1

    if indicadores_estrategia == 0:
        puntuacion_estrategia = 0
    elif indicadores_estrategia <= 2:
        puntuacion_estrategia = 1
    else:
        puntuacion_estrategia = 2

    puntuacion_total = (
        puntuacion_emocion
        + puntuacion_certeza
        + puntuacion_generalizacion
        + puntuacion_estrategia
    )

    if puntuacion_total <= 2:
        nivel_riesgo = "Bajo"
    elif puntuacion_total <= 5:
        nivel_riesgo = "Medio"
    else:
        nivel_riesgo = "Alto"

    return {
        "nivel_riesgo": nivel_riesgo,
        "puntuacion_total": puntuacion_total,
        "puntuacion_emocion": puntuacion_emocion,
        "puntuacion_certeza": puntuacion_certeza,
        "puntuacion_generalizacion": puntuacion_generalizacion,
        "puntuacion_estrategia": puntuacion_estrategia,
        "emocion_encontrada": emocion_encontrada,
        "valorativo_encontrado": valorativo_encontrado,
        "alarmista_encontrado": alarmista_encontrado,
        "intensificadores_encontrados": intensificadores_encontrados,
        "certeza_encontrada": certeza_encontrada,
        "generalizacion_encontrada": generalizacion_encontrada,
        "estrategia_encontrada": estrategia_encontrada,
        "porcentaje_mayusculas": porcentaje_mayusculas,
        "numero_exclamaciones": numero_exclamaciones,
        "numero_interrogaciones": numero_interrogaciones,
        "numero_hashtags": numero_hashtags,
        "numero_menciones": numero_menciones,
        "numero_enlaces": numero_enlaces,
        "repeticion_signos": repeticion_signos,
        "posible_interrogacion_retorica": posible_interrogacion_retorica,
        "categoricas_encontradas": categoricas_encontradas,
        "falta_matizacion": falta_matizacion,
        "evidencia_encontrada": evidencia_encontrada,
        "ausencia_evidencia_explicita": ausencia_evidencia_explicita,
        "polarizacion_encontrada": polarizacion_encontrada,
        "llamadas_encontradas": llamadas_encontradas,
        "ocultamiento_encontrado": ocultamiento_encontrado
    }


def mostrar_lista(nombre, elementos):
    if elementos:
        st.markdown(f"**{nombre}:** {', '.join(elementos)}")
    else:
        st.markdown(f"**{nombre}:** No detectado")


# CONFIGURACIÓN DE LA WEB
st.set_page_config(
    page_title="Análisis discursivo de publicaciones en X",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F6F8FA;
    }

    .main-title {
        color: #174A5B;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .main-subtitle {
        color: #52656D;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .result-card {
        background-color: white;
        border-radius: 14px;
        padding: 24px;
        border: 1px solid #DCECF1;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.06);
        margin-bottom: 18px;
    }

    .risk-low {
        border-left: 8px solid #2E7D6E;
    }

    .risk-medium {
        border-left: 8px solid #D99000;
    }

    .risk-high {
        border-left: 8px solid #B23A48;
    }

    .risk-title {
        font-size: 14px;
        color: #65777E;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .risk-value {
        color: #174A5B;
        font-size: 34px;
        font-weight: 700;
        margin: 4px 0;
    }

    div.stButton > button {
        background-color: #174A5B;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 25px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #21677D;
        color: white;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

corpus = cargar_corpus()
modelo, precision = entrenar_modelo(corpus)

if "resultado" not in st.session_state:
    st.session_state.resultado = None

st.markdown(
    '<div class="main-title">Prototipo de detección de desinformación</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="main-subtitle">Análisis de rasgos lingüísticos, formales y discursivos en publicaciones de X.</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.subheader("Información del prototipo")
    st.metric("Publicaciones del corpus", len(corpus))
    st.metric("Precisión experimental", f"{precision * 100:.2f} %")
    st.divider()
    st.caption(
        "La precisión corresponde al modelo experimental entrenado con el corpus. "
        "La puntuación discursiva mostrada en la interfaz procede de la rúbrica de indicadores."
    )

col_entrada, col_resultado = st.columns([1.15, 1], gap="large")

with col_entrada:
    st.subheader("Introduce la publicación")

    texto = st.text_area(
        "Texto de la publicación",
        height=230,
        placeholder="Escribe o pega aquí el contenido del mensaje...",
        label_visibility="collapsed"
    )

    st.caption(f"{len(texto)} caracteres")

    analizar = st.button(
        "Analizar publicación",
        type="primary",
        use_container_width=True
    )

    if analizar:
        if texto.strip() == "":
            st.warning("Escribe una publicación antes de analizarla.")
        else:
            with st.spinner("Analizando rasgos discursivos..."):
                st.session_state.resultado = analizar_publicacion(texto)

with col_resultado:
    st.subheader("Resultado general")

    resultado = st.session_state.resultado

    if resultado is None:
        st.info("El resultado aparecerá aquí después de analizar la publicación.")
    else:
        nivel = resultado["nivel_riesgo"]
        clase_riesgo = {
            "Bajo": "risk-low",
            "Medio": "risk-medium",
            "Alto": "risk-high"
        }[nivel]

        st.markdown(
            f"""
            <div class="result-card {clase_riesgo}">
                <div class="risk-title">Nivel de riesgo discursivo</div>
                <div class="risk-value">{nivel}</div>
                <div>El resultado indica la intensidad de los rasgos detectados, no la veracidad del contenido.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.metric(
            label="Puntuación de riesgo",
            value=f'{resultado["puntuacion_total"]}/8'
        )

        st.progress(resultado["puntuacion_total"] / 8)

        if nivel == "Bajo":
            st.success("Se han detectado pocos indicadores asociados al riesgo discursivo.")
        elif nivel == "Medio":
            st.warning("Se han detectado varios indicadores que requieren una lectura crítica.")
        else:
            st.error("Se ha detectado una concentración elevada de indicadores discursivos.")

st.divider()
st.subheader("Desglose del análisis")

resultado = st.session_state.resultado

if resultado is None:
    st.info("Realiza un análisis para consultar el desglose de indicadores.")
else:
    tab_lexicos, tab_formales, tab_discursivos, tab_puntuaciones = st.tabs([
        "Rasgos léxicos",
        "Rasgos formales",
        "Rasgos discursivos",
        "Puntuaciones"
    ])

    with tab_lexicos:
        mostrar_lista("Léxico emocional", resultado["emocion_encontrada"])
        mostrar_lista("Léxico valorativo", resultado["valorativo_encontrado"])
        mostrar_lista("Palabras alarmistas", resultado["alarmista_encontrado"])
        mostrar_lista("Intensificadores", resultado["intensificadores_encontrados"])
        mostrar_lista("Marcadores de certeza", resultado["certeza_encontrada"])
        mostrar_lista("Términos generalizadores", resultado["generalizacion_encontrada"])
        mostrar_lista("Estrategias léxicas", resultado["estrategia_encontrada"])

    with tab_formales:
        col1, col2, col3 = st.columns(3)
        col1.metric("Mayúsculas", f'{resultado["porcentaje_mayusculas"]:.2f} %')
        col2.metric("Exclamaciones", resultado["numero_exclamaciones"])
        col3.metric("Interrogaciones", resultado["numero_interrogaciones"])

        col4, col5, col6 = st.columns(3)
        col4.metric("Hashtags", resultado["numero_hashtags"])
        col5.metric("Menciones", resultado["numero_menciones"])
        col6.metric("Enlaces", resultado["numero_enlaces"])

        st.write("**Repetición de signos:**", resultado["repeticion_signos"])
        st.write(
            "**Posible interrogación retórica:**",
            "Sí" if resultado["posible_interrogacion_retorica"] else "No"
        )

    with tab_discursivos:
        mostrar_lista("Afirmaciones categóricas", resultado["categoricas_encontradas"])
        mostrar_lista("Referencias explícitas a evidencia", resultado["evidencia_encontrada"])
        mostrar_lista("Polarización nosotros/ellos", resultado["polarizacion_encontrada"])
        mostrar_lista("Llamadas a compartir", resultado["llamadas_encontradas"])
        mostrar_lista("Ocultamiento informativo", resultado["ocultamiento_encontrado"])

        st.write(
            "**Falta de matización:**",
            "Sí" if resultado["falta_matizacion"] else "No"
        )
        st.write(
            "**Ausencia de evidencia explícita:**",
            "Sí" if resultado["ausencia_evidencia_explicita"] else "No"
        )

    with tab_puntuaciones:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Emoción", f'{resultado["puntuacion_emocion"]}/2')
        col2.metric("Certeza", f'{resultado["puntuacion_certeza"]}/2')
        col3.metric("Generalización", f'{resultado["puntuacion_generalizacion"]}/2')
        col4.metric("Estrategia", f'{resultado["puntuacion_estrategia"]}/2')

        st.metric("Puntuación total", f'{resultado["puntuacion_total"]}/8')

with st.expander("¿Cómo se interpreta el resultado?"):
    st.write(
        "El prototipo analiza indicadores léxicos, formales y discursivos. "
        "Cada una de las cuatro dimensiones aporta entre 0 y 2 puntos, por lo que "
        "la puntuación máxima es 8. El nivel bajo corresponde a 0-2 puntos; el nivel "
        "medio, a 3-5; y el nivel alto, a 6-8."
    )

st.info(
    "Este prototipo no determina si una publicación es verdadera o falsa. "
    "Solo estima su nivel de riesgo discursivo a partir de los indicadores analizados."
)
