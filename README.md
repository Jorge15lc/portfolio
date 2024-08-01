# Jorge Lasheras Castillo

**Desarrollador Full Stack y DevOps**

---

## Sobre Mí

Soy Jorge Lasheras Castillo, un apasionado Desarrollador Full Stack y DevOps con más de 2 años de experiencia en la creación, despliegue y optimización de aplicaciones web y móviles. Me especializo en tecnologías como Python, Django, APIs, HTML, CSS, Bootstrap, JavaScript y JQuery. Me enfoco en la innovación y en ofrecer experiencias de usuario excepcionales.

## Habilidades Técnicas

### Full Stack
- Python
- Django
- APIs
- HTML, CSS, Bootstrap
- JavaScript, JQuery

### DevOps
- VPS
- Gunicorn
- Nginx
- PostgreSQL

## Contacto

- Email: lasherascastillojorge@gmail.com
- Teléfono: +34 666 366 242
- Ubicación: Cenes de la Vega, Granada

## Redes Sociales

- GitHub: [github.com/Jorge15lc](https://github.com/Jorge15lc)
- LinkedIn: [linkedin.com/in/jorge15lc](https://www.linkedin.com/in/jorge15lc)

## Experiencia Laboral

### Desarrollador Full Stack y DevOps | Buyback - Granada | 2023 - 2024
- Creación y optimización de aplicaciones web eCommerce, Marketplace y eLearning.
- Integración y desarrollo de APIs (Google Auth, Maps, Sage, OpenAI, Redsys, Stripe, Brevo...).
- Desarrollo de Backend con Python, Django, DRF, Postgres, SQL y tecnologías como pandas, numpy y celery.
- Desarrollo de Frontend con HTML, CSS, Bootstrap, JavaScript y JQuery.
- Participación en equipos siguiendo CI/CD, AGILE, SCRUM, OKR y principios SOLID y DRY.

### Desarrollador Full Stack y DevOps | Grupo VyA | 2023 - Actualmente
- Creación, despliegue y mantenimiento de aplicaciones ERP y Marketplace.
- Diseño de bases de datos y desarrollo de Backend y Frontend con Python, Django, Postgres, HTML, CSS, JavaScript, JQuery y Postgis.

## Proyectos Destacados

### [Proyecto 1](#)
Descripción breve del proyecto 1.

### [Proyecto 2](#)
Descripción breve del proyecto 2.

## Educación

- **Desarrollo de Aplicaciones Multiplataforma** | Escuela Arte Granada - FP Superior | 2021-2023
- **Bachiller** | Beatriz Galindo | 2016-2018

## Idiomas

- Español (Nativo)
- Inglés (Nivel B2)

---

## Código de Ejemplo

```python
class DesarrolladorFullStack:
    def __init__(self):
        self.habilidades = ["Python", "Django", "APIs", "HTML", "CSS", "Bootstrap", "JavaScript", "JQuery"]
        self.objetivo = "creación y optimización de aplicaciones web y móviles"

    def mostrar_habilidades(self):
        return f"Habilidades de Full Stack: {', '.join(self.habilidades)}"

    def mostrar_objetivo(self):
        return f"Objetivo: {self.objetivo}"


class DevOps:
    def __init__(self):
        self.habilidades_devops = ["VPS", "Gunicorn", "Nginx", "PostgreSQL"]
        self.objetivo_devops = "mejora continua y despliegue eficiente"

    def mostrar_habilidades_devops(self):
        return f"Habilidades de DevOps: {', '.join(self.habilidades_devops)}"

    def mostrar_objetivo_devops(self):
        return f"Objetivo de DevOps: {self.objetivo_devops}"


class JorgeLasherasCastillo(DesarrolladorFullStack, DevOps):
    def __init__(self):
        DesarrolladorFullStack.__init__(self)
        DevOps.__init__(self)
        self.nombre = "Jorge Lasheras Castillo"
        self.roles = ["Desarrollador Full Stack", "DevOps"]
        self.experiencia = 2  # años
        self.contacto = {
            "Email": "lasherascastillojorge@gmail.com",
            "Teléfono": "+34 666 366 242",
            "Ubicación": "Cenes de la Vega, Granada"
        }
        self.github = "github.com/Jorge15lc"
        self.linkedin = "linkedin.com/in/jorge15lc"

    def mostrar_bio(self):
        return f"Soy {self.nombre}, un apasionado {', '.join(self.roles)} con más de {self.experiencia} años de experiencia."

    def mostrar_contacto(self):
        return f"Puedes contactarme a través de {self.contacto['Email']} o al teléfono {self.contacto['Teléfono']}. Estoy ubicado en {self.contacto['Ubicación']}."

    def mostrar_redes(self):
        return f"Visita mi GitHub: {self.github} y mi LinkedIn: {self.linkedin}"

    def mostrar_resumen(self):
        return f"{self.mostrar_bio()} {self.mostrar_habilidades()} y {self.mostrar_habilidades_devops()}. Me enfoco en la {self.objetivo} y la {self.objetivo_devops}."

    def __str__(self):
        return self.mostrar_resumen()


jorge = JorgeLasherasCastillo()
print(jorge.mostrar_resumen())
print(jorge.mostrar_contacto())
print(jorge.mostrar_redes())
