# Linguistic and Discursive Analysis of Misinformation on X

<p>
An experimental research prototype developed as part of a Master's Thesis in Digital Humanities (2026).
</p>

<h2>1. Overview</h2>

<p>
This project explores linguistic, formal, and discursive patterns associated with misinformation in Spanish-language posts on X. It combines corpus-based linguistic research, rule-based analysis, and basic Natural Language Processing (NLP) techniques within an interactive application developed with Python and Streamlit.
</p>

<p>
The primary objective is to identify and examine linguistic features that may be associated with potentially misleading discourse, rather than to determine the factual accuracy of individual claims.
</p>

<p>
The prototype prioritises interpretability by providing a transparent breakdown of the indicators detected and the criteria used to estimate discursive risk.
</p>

<h2>2. Research Methodology</h2>

<p>
The project follows a mixed methodological approach, integrating qualitative discourse analysis with quantitative linguistic feature extraction and computational text processing.
</p>

<p>
Its development comprises four main components:
</p>

<ul>
  <li><b>Corpus construction and annotation:</b> Compilation and manual annotation of 110 Spanish-language publications using a structured linguistic and discursive rubric.</li>
  <li><b>Linguistic feature extraction:</b> Identification of lexical, formal, and discursive indicators, including emotional language, categorical statements, generalisation, punctuation patterns, and persuasive strategies.</li>
  <li><b>Rule-based risk assessment:</b> Evaluation of four analytical dimensions (emotion, certainty, generalisation, and discursive strategy), each assigned a score between 0 and 2. The resulting score ranges from 0 to 8 and is classified into low, medium, or high discursive risk.</li>
  <li><b>Experimental machine learning:</b> Implementation of a text classification pipeline using TF-IDF vectorisation and logistic regression, evaluated through a stratified 80/20 training and test split.</li>
</ul>

<p>
The rule-based assessment and the machine-learning classifier serve different purposes. The risk level displayed for an analysed publication is calculated from the linguistic rubric, while the classifier's accuracy is reported separately as an experimental evaluation measure.
</p>

<h2>3. Application Features</h2>

<p>
The application provides an interactive environment for analysing short Spanish-language texts. Its main functionalities include:
</p>

<ul>
  <li>Analysis of user-submitted text.</li>
  <li>Estimation of discursive risk (low, medium, or high).</li>
  <li>Identification of lexical, formal, and discursive indicators.</li>
  <li>Individual scores for the four analytical dimensions.</li>
  <li>Visualisation of the overall risk score.</li>
  <li>Presentation of corpus statistics and experimental classification accuracy.</li>
</ul>

<h2>4. Technologies</h2>

<ul>
  <li><b>Python:</b> Application logic and linguistic processing.</li>
  <li><b>pandas:</b> Corpus loading and data processing.</li>
  <li><b>scikit-learn:</b> TF-IDF vectorisation, logistic regression, and model evaluation.</li>
  <li><b>Streamlit:</b> Interactive web application.</li>
  <li><b>openpyxl:</b> Reading the Excel-based research corpus.</li>
</ul>

<h2>5. Repository Structure</h2>

<pre><code>linguistic-misinformation-analysis/
|
|-- prototipo_integrado.py
|-- rubrica_corpus.xlsx
|-- requirements.txt
|-- README.md
</code></pre>

<h2>6. Local Installation</h2>

<p>
To run the prototype locally, install the required dependencies:
</p>

<pre><code>pip install -r requirements.txt</code></pre>

<p>
Then launch the Streamlit application:
</p>

<pre><code>streamlit run prototipo_integrado.py</code></pre>

<p>
The research corpus must be located in the same directory as the Python application.
</p>

<h2>7. Scope and Limitations</h2>

<p>
This project is an exploratory academic prototype and should not be interpreted as an automated fact-checking system.
</p>

<p>
The presence of linguistic indicators associated with misleading discourse does not establish that a statement is false. Such features may also occur in accurate, opinion-based, or context-dependent publications.
</p>

<p>
The limited corpus size, rule-based feature detection, and experimental classification approach constrain the generalisability of the results. Automated linguistic analysis may also fail to capture contextual meaning, irony, implicit references, or pragmatic nuances.
</p>

<p>
The application is intended to support linguistic research and critical discourse analysis. Its outputs should be interpreted as preliminary analytical indicators rather than definitive assessments of misinformation.
</p>

<hr>

<h1>Análisis lingüístico y discursivo de la desinformación en X</h1>

<p>
Prototipo experimental de investigación desarrollado como parte de un Trabajo Fin de Máster en Humanidades Digitales (2026).
</p>

<h2>1. Descripción del proyecto</h2>

<p>
Este proyecto estudia patrones lingüísticos, formales y discursivos asociados a la desinformación en publicaciones en español de la red social X. Combina investigación lingüística basada en corpus, análisis mediante reglas y técnicas básicas de Procesamiento del Lenguaje Natural (PLN) en una aplicación interactiva desarrollada con Python y Streamlit.
</p>

<p>
Su objetivo principal es identificar y analizar rasgos lingüísticos que pueden aparecer en discursos potencialmente desinformativos, sin determinar la veracidad factual de las afirmaciones individuales.
</p>

<p>
El prototipo prioriza la interpretabilidad de los resultados mediante un desglose transparente de los indicadores detectados y de los criterios utilizados para estimar el riesgo discursivo.
</p>

<h2>2. Metodología de investigación</h2>

<p>
El proyecto adopta un enfoque metodológico mixto que integra el análisis cualitativo del discurso con la extracción cuantitativa de características lingüísticas y el procesamiento computacional de textos.
</p>

<p>
Su desarrollo comprende cuatro componentes principales:
</p>

<ul>
  <li><b>Construcción y anotación del corpus:</b> Recopilación y anotación manual de 110 publicaciones en español mediante una rúbrica de análisis lingüístico-discursivo.</li>
  <li><b>Extracción de rasgos lingüísticos:</b> Identificación de indicadores léxicos, formales y discursivos, entre ellos lenguaje emocional, afirmaciones categóricas, generalizaciones, patrones de puntuación y estrategias persuasivas.</li>
  <li><b>Evaluación del riesgo mediante reglas:</b> Análisis de cuatro dimensiones (emoción, certeza, generalización y estrategia discursiva), con puntuaciones individuales de 0 a 2. La suma, comprendida entre 0 y 8, permite establecer tres niveles de riesgo discursivo: bajo, medio y alto.</li>
  <li><b>Aprendizaje automático experimental:</b> Implementación de un sistema de clasificación textual mediante vectorización TF-IDF y regresión logística, evaluado con una división estratificada del corpus en un 80 % de entrenamiento y un 20 % de prueba.</li>
</ul>

<p>
La evaluación mediante reglas y el clasificador de aprendizaje automático cumplen funciones diferentes. El nivel de riesgo mostrado para cada publicación se obtiene a partir de la rúbrica lingüística, mientras que la exactitud del clasificador se presenta por separado como medida de evaluación experimental.
</p>

<h2>3. Funcionalidades de la aplicación</h2>

<p>
La aplicación proporciona un entorno interactivo para el análisis de textos breves en español. Entre sus principales funcionalidades se encuentran:
</p>

<ul>
  <li>Análisis de textos introducidos por el usuario.</li>
  <li>Estimación del riesgo discursivo (bajo, medio o alto).</li>
  <li>Identificación de indicadores léxicos, formales y discursivos.</li>
  <li>Visualización de las puntuaciones individuales de las cuatro dimensiones analíticas.</li>
  <li>Representación de la puntuación global de riesgo.</li>
  <li>Consulta de estadísticas del corpus y de la exactitud experimental del modelo de clasificación.</li>
</ul>

<h2>4. Tecnologías utilizadas</h2>

<ul>
  <li><b>Python:</b> Lógica de la aplicación y procesamiento lingüístico.</li>
  <li><b>pandas:</b> Carga y tratamiento de los datos del corpus.</li>
  <li><b>scikit-learn:</b> Vectorización TF-IDF, regresión logística y evaluación del modelo.</li>
  <li><b>Streamlit:</b> Desarrollo de la interfaz web interactiva.</li>
  <li><b>openpyxl:</b> Lectura del corpus almacenado en formato Excel.</li>
</ul>

<h2>5. Estructura del repositorio</h2>

<pre><code>linguistic-misinformation-analysis/
|
|-- prototipo_integrado.py
|-- rubrica_corpus.xlsx
|-- requirements.txt
|-- README.md
</code></pre>

<h2>6. Ejecución en entorno local</h2>

<p>
Para ejecutar el prototipo localmente, deben instalarse las dependencias necesarias:
</p>

<pre><code>pip install -r requirements.txt</code></pre>

<p>
A continuación, se inicia la aplicación:
</p>

<pre><code>streamlit run prototipo_integrado.py</code></pre>

<p>
El archivo del corpus debe encontrarse en el mismo directorio que la aplicación de Python.
</p>

<h2>7. Alcance y limitaciones</h2>

<p>
Este proyecto constituye un prototipo académico exploratorio y no debe interpretarse como un sistema automatizado de verificación de información.
</p>

<p>
La presencia de indicadores lingüísticos asociados a discursos potencialmente desinformativos no implica que una afirmación sea falsa. Estos rasgos también pueden aparecer en publicaciones veraces, textos de opinión o mensajes cuyo significado dependa del contexto.
</p>

<p>
El tamaño reducido del corpus, la detección de indicadores mediante reglas y el carácter experimental del modelo de clasificación limitan la generalización de los resultados. Asimismo, el análisis automático puede presentar dificultades para interpretar el contexto, la ironía, las referencias implícitas y otros matices pragmáticos.
</p>

<p>
La herramienta se plantea como un recurso de apoyo a la investigación lingüística y al análisis crítico del discurso. Sus resultados deben interpretarse como indicadores analíticos preliminares, no como valoraciones definitivas sobre la presencia de desinformación.
</p>
