from django.core.management.base import BaseCommand
from apps.main.models import Service

class Command(BaseCommand):
    help = 'Populate the database with initial service data'

    def handle(self, *args, **kwargs):
        services = [
            {
                "title": "Desarrollo Full Stack de Aplicaciones Web",
                "icon": "flaticon-code",
                "description": "Desarrollo integral de aplicaciones web optimizadas, utilizando tecnologías como Python, Django, y JavaScript.",
                "modal_image": "services/web_development.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Desarrollo Full Stack",
                "modal_content": "Ofrezco un desarrollo completo de aplicaciones web, desde el backend robusto hasta interfaces de usuario intuitivas, asegurando una experiencia de usuario fluida y eficiente.",
                "process_title": "Proceso de Desarrollo Full Stack",
                "process_description": "El proceso incluye la definición de la arquitectura, desarrollo del backend con Django, integración de APIs y pruebas exhaustivas.",
                "process_steps": "Análisis, Diseño, Desarrollo, Pruebas, Despliegue",
            },
            {
                "title": "Optimización y Mantenimiento de eCommerce",
                "icon": "flaticon-bezier-tool",
                "description": "Creación y optimización de plataformas de eCommerce robustas y seguras.",
                "modal_image": "services/ecommerce_optimization.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Optimización de eCommerce",
                "modal_content": "Desarrollo y mantenimiento de plataformas de comercio electrónico, optimizando para mejorar la conversión y la experiencia del usuario.",
                "process_title": "Proceso de Optimización de eCommerce",
                "process_description": "Incluye análisis de necesidades, diseño personalizado, integración de métodos de pago y pruebas de rendimiento.",
                "process_steps": "Análisis, Desarrollo, Integración de Pagos, Optimización, Mantenimiento",
            },
            {
                "title": "Desarrollo de Marketplaces y Plataformas Multiusuario",
                "icon": "flaticon-browser",
                "description": "Desarrollo de plataformas que conectan a múltiples usuarios de manera eficiente.",
                "modal_image": "services/marketplace_development.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Desarrollo de Marketplaces",
                "modal_content": "Diseño y desarrollo de marketplaces personalizados que facilitan la interacción entre usuarios, asegurando un flujo de trabajo sin problemas.",
                "process_title": "Proceso de Desarrollo de Marketplaces",
                "process_description": "Configuración de la infraestructura, desarrollo backend y frontend, integración de funcionalidades y pruebas de escalabilidad.",
                "process_steps": "Planificación, Diseño, Desarrollo, Integración, Pruebas",
            },
            {
                "title": "Integración de Inteligencia Artificial",
                "icon": "flaticon-smartphone",
                "description": "Implementación de soluciones de IA para automatización avanzada.",
                "modal_image": "services/ai_integration.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Integración de IA",
                "modal_content": "Implementación de tecnologías de inteligencia artificial para mejorar la automatización y análisis en tus aplicaciones, transformando la experiencia del usuario.",
                "process_title": "Proceso de Integración de IA",
                "process_description": "Análisis de requerimientos, integración de APIs de IA, desarrollo de funcionalidades personalizadas y optimización continua.",
                "process_steps": "Análisis, Integración de APIs, Desarrollo, Optimización",
            },
            {
                "title": "Desarrollo de ERP y CRM Personalizados",
                "icon": "flaticon-ui-design",
                "description": "Desarrollo de sistemas ERP y CRM adaptados a las necesidades de tu negocio.",
                "modal_image": "services/erp_crm_development.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Desarrollo de ERP y CRM",
                "modal_content": "Diseño y desarrollo de soluciones ERP y CRM que automatizan procesos clave y mejoran la gestión empresarial, personalizadas para tu negocio.",
                "process_title": "Proceso de Desarrollo de ERP y CRM",
                "process_description": "Reunión de requisitos, diseño de base de datos robusta, desarrollo de módulos específicos e integración continua.",
                "process_steps": "Planificación, Diseño, Desarrollo, Integración, Soporte",
            },
            {
                "title": "Servicios DevOps",
                "icon": "flaticon-web-design",
                "description": "Configuración de servidores y automatización de despliegue de aplicaciones.",
                "modal_image": "services/devops.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Servicios DevOps",
                "modal_content": "Administración y configuración de servidores, implementación de pipelines CI/CD y despliegue eficiente de aplicaciones, garantizando alta disponibilidad y rendimiento.",
                "process_title": "Proceso de Servicios DevOps",
                "process_description": "Configuración de entornos, automatización del despliegue, monitoreo de servidores y ajustes continuos.",
                "process_steps": "Configuración, Automatización, Despliegue, Monitoreo, Ajustes",
            },
        ]

        for service_data in services:
            service, created = Service.objects.get_or_create(**service_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Service "{service.title}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Service "{service.title}" already exists'))