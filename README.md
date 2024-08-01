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
class FullStackDeveloper:
    def __init__(self):
        self.skills = ["Python", "Django", "APIs", "HTML", "CSS", "Bootstrap", "JavaScript", "JQuery"]
        self.goal = "creación y optimización de aplicaciones web y móviles"

    def show_skills(self):
        return f"Habilidades de Full Stack: {', '.join(self.skills)}"

    def show_goal(self):
        return f"Objetivo: {self.goal}"


class DevOps:
    def __init__(self):
        self.devops_skills = ["VPS", "Gunicorn", "Nginx", "PostgreSQL"]
        self.devops_goal = "mejora continua y despliegue eficiente"

    def show_devops_skills(self):
        return f"Habilidades de DevOps: {', '.join(self.devops_skills)}"

    def show_devops_goal(self):
        return f"Objetivo de DevOps: {self.devops_goal}"


class JorgeLasherasCastillo(FullStackDeveloper, DevOps):
    def __init__(self):
        FullStackDeveloper.__init__(self)
        DevOps.__init__(self)
        self.name = "Jorge Lasheras Castillo"
        self.roles = ["Desarrollador Full Stack", "DevOps"]
        self.experience = 2  # años
        self.contact = {
            "Email": "lasherascastillojorge@gmail.com",
            "Phone": "+34 666 366 242",
            "Location": "Cenes de la Vega, Granada"
        }
        self.github = "github.com/Jorge15lc"
        self.linkedin = "linkedin.com/in/jorge15lc"

    def show_bio(self):
        return f"Soy {self.name}, un apasionado {', '.join(self.roles)} con más de {self.experience} años de experiencia."

    def show_contact(self):
        return f"Puedes contactarme a través de {self.contact['Email']} o al teléfono {self.contact['Phone']}. Estoy ubicado en {self.contact['Location']}."

    def show_socials(self):
        return f"Visita mi GitHub: {self.github} y mi LinkedIn: {self.linkedin}"

    def show_summary(self):
        return f"{self.show_bio()} {self.show_skills()} y {self.show_devops_skills()}. Me enfoco en la {self.goal} y la {self.devops_goal}."

    def __str__(self):
        return self.show_summary()


jorge = JorgeLasherasCastillo()
print(jorge.show_summary())
print(jorge.show_contact())
print(jorge.show_socials())
