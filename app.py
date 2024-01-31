from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Adrian_Sanchez.pdf"
profile_pic = current_dir / "assets" / "profile-pic3.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Adrián Sánchez"
PAGE_ICON = ":wave:"
NAME = "Adrián Sánchez"
DESCRIPTION = """
Contabilidad🔢 | Finanzas📝 | Analista de datos 📊 | Python 🐍 | Excel📉 | Power BI📊| Excel📉 | SQL🐬|
"""
EMAIL = "adriansg1991@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/adri%C3%A1n-s%C3%A1nchez-garc%C3%ADa-822676114/",
    "GitHub": "https://github.com/adriansg1991",
    "Medium": "https://medium.com/@adriansg1991",
    "Portfolio Python": "https://adriansanchez.streamlit.app/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Descargar CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")




# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experiencia laboral")
st.write("---")

# --- JOB 1
st.write("💼", "**Finance & Accounting**")
st.write('🏢​ Corus, 📍 Sant Cugat del Vallés')
st.write("03/2021 - 09/2023")
st.write(
    """
- ► Contabilidad: Contabilidad Holding España (Ciclo contable completo) | Impuestos | Cuentas anuales | Certificados digitales | Reporting
- ► Finanzas: Informes económicos | Informes stock & WIP | Presupuestos
- ► Automatización de procesos/Data analyst : Python | Pandas | Numpy | Selenium | Tkinter| Power BI:
    * Automatización de informes.
    * Carga masiva de datos en el CRM mediante script.
    * Programa carga masiva de facturas a SAP.
- ► Key User SAP.
- ► Integración nuevos programas IT (OCR, gestión de gastos, gestión de viajes).
- ► Auditoria IT (dpto. finanzas).

"""
)

# --- JOB 2
st.write('\n')
st.write("💼", "**Técnico contable | Administrativo**")
st.write('🏢​ UAB Idiomes Barcelona, 📍Barcelona')
st.write("2017 - 2020")
st.write(
    """
- ► Encargado de la facturación de las diferentes actividades del centro.
- ► Reporting: Realización de informes económicos, estadísticas, previsiones, etc.
- ► Diseño y seguimiento del presupuesto de la empresa.
- ► Control de cartera de clientes.
- ► Tareas administrativas.
"""
)

# --- JOB 3
st.write('\n')
st.write("💼", "**Técnico de contabilidad**")
st.write('🏢​ Fundació UAB, 📍Barcelona')
st.write("11/2016 - 06/2017")
st.write(
    """
- ► Contabilización de facturas de proveedores/clientes.
- ► Contabilización de pagos/cobros.
- ► Control de conciliaciones bancarias y gestión de banca electrónica.
- ► Identificación y contabilización de cobros de visa, efectivo, transferencias de código de barras y códigos de barras y cobros a cuenta.
- ► Contabilización de gastos de gestión corriente (caja, tickets...).
- ► Control de cartera de clientes y proveedores.
- ► Emisión de facturas.
- ► Resolución de consultas y aportación de soluciones en informes de Excel.
- ► Reporting.
- ► Elaboración de impuestos 347, IVA y IRPF.
- ► Colaboración en la revisión de Cuentas Anuales.
- ► Elaboración de informes de cierre y presupuestos en Excel a partir de la contabilidad en SAP.

"""
)
# --- JOB 4
st.write('\n')
st.write("💼", "**Departamento de Control Económico Financiero**")
st.write('🏢​ Ajuntament de Barcelona, 📍Barcelona')
st.write("06/2015 - 01/2016")
st.write(
    """
- ►  Reporting: Informe económico financiero
- ►  Contabilidad presupuestaria
"""
)
# --- JOB 5
st.write('\n')
st.write("💼", "**Contable administrativo**")
st.write('🏢​ Accesorios y Recambios Los Juanes, SA, 📍Terrassa')
st.write("06/2015 - 01/2016")
st.write(
    """
- ►  Contabilidad financiera
"""
)



# --- EXPERIENCE & QUALIFICATIONS ---
    
# --- Educación
st.write('\n')
st.subheader( "**Educación**")
st.write("---")
st.write("")

# Educación 1
st.write('🏫 Datahack school')
st.write("Data science - big data, Procesamiento de datos")
st.write("2020 - 2020")
st.write(
    """
    Reskilling course organized by Barcelona Activa:
- ✔️ Python Language
- ✔️ Data Analysis Libraries:
    - * > Pandas
    - * > Numpy
- ✔️ Data Visualization Libraries:
    - * > Matplotlib
    - * > Seaborn
"""
)


# Educación 2
st.write('🏫 Universitat Autònoma de Barcelona')
st.write("Grado en Administración y Dirección de empresas con Mención PUE")
st.write("2012 - 2016")

# Educación 3
st.write('🏫 INS Santa Eulàlia')
st.write("CFGS Administración y Finanzas")
st.write("2010 - 2012")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write('---')
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, numpy, selenium, matplotlib, seaborn).
- 📊 Data Visualization: PowerBi, MS Excel.
- 🗄️ Databases: MySQL,Postgres.
"""
)

#url = 'https://www.linkedin.com/in/adrián-sánchez-garcía-822676114/'
#st.link_button("Go to gallery", url)


# --- SKILLS ---
st.write('\n')
st.subheader("Idiomas")
st.write('---')
st.write(
    """
- Castellano: Lengua materna
- Catalán: Lengua materna
- Inglés: Nivel intermedio
"""
)

#PROJECTS = {
#    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
#}

# --- Projects & Accomplishments ---
#st.write('\n')
#st.subheader("Projects & Accomplishments")
#st.write("---")
#for project, link in PROJECTS.items():
#    st.write(f"[{project}]({link})")
