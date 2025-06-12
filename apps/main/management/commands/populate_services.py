from django.core.management.base import BaseCommand
from apps.main.models import Service

class Command(BaseCommand):
    help = 'Populate the database with initial service data'

    def handle(self, *args, **kwargs):
        services = [
            {
                "title": "Desarrollo Full Stack de Aplicaciones Web",
                "icon": "flaticon-code",
                "description": "Desarrollo integral de aplicaciones web optimizadas con Django. Ideal para empresas que necesitan escalar rápido sin sacrificar rendimiento.",
                "additional_info": "Caso real: marketplace B2B que redujo tiempos de compra en un 30% tras migrar a esta plataforma.",
                "modal_image": "services/web_development.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Desarrollo Full Stack",
                "modal_content": "Planteamos el problema de negocio, diseñamos la arquitectura y construimos el backend con Django REST Framework. Integramos APIs de pago y servicios externos, entregando un frontend ligero que carga en milisegundos.",
                "process_title": "Proceso de Desarrollo Full Stack",
                "process_description": "El proceso incluye la definición de la arquitectura, desarrollo del backend con Django, integración de APIs y pruebas exhaustivas.",
                "process_steps": "Análisis, Diseño, Desarrollo, Pruebas, Despliegue",
            },
            {
                "title": "Optimización y Mantenimiento de eCommerce",
                "icon": "flaticon-bezier-tool",
                "description": "Creación y optimización de tiendas en línea seguras, pensadas para aumentar tu conversión.",
                "additional_info": "Ejemplo: migración de catálogo a medida que redujo un 20% los costos de mantenimiento.",
                "modal_image": "services/ecommerce_optimization.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Optimización de eCommerce",
                "modal_content": "Analizamos cuellos de botella, optimizamos bases de datos y aplicamos mejoras en la interfaz para incrementar la retención de clientes.",
                "process_title": "Proceso de Optimización de eCommerce",
                "process_description": "Incluye análisis de necesidades, diseño personalizado, integración de métodos de pago y pruebas de rendimiento.",
                "process_steps": "Análisis, Desarrollo, Integración de Pagos, Optimización, Mantenimiento",
            },
            {
                "title": "Desarrollo de Marketplaces y Plataformas Multiusuario",
                "icon": "flaticon-browser",
                "description": "Desarrollo de plataformas que conectan a múltiples usuarios y gestionan transacciones en tiempo real.",
                "additional_info": "Ejemplo: marketplace corporativo que incrementó en un 40% las ventas al integrar pasarelas de pago personalizadas.",
                "modal_image": "services/marketplace_development.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Desarrollo de Marketplaces",
                "modal_content": "Definimos la arquitectura multiusuario, desarrollamos módulos de pagos y notificaciones, y optimizamos la escalabilidad con Docker y Kubernetes.",
                "process_title": "Proceso de Desarrollo de Marketplaces",
                "process_description": "Configuración de la infraestructura, desarrollo backend y frontend, integración de funcionalidades y pruebas de escalabilidad.",
                "process_steps": "Planificación, Diseño, Desarrollo, Integración, Pruebas",
            },
            {
                "title": "Integración de Inteligencia Artificial",
                "icon": "flaticon-smartphone",
                "description": "Implementación de soluciones de IA que automatizan procesos repetitivos y mejoran la toma de decisiones.",
                "additional_info": "Caso de éxito: chatbot con OpenAI que redujo un 50% las consultas de soporte humano.",
                "modal_image": "services/ai_integration.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Integración de IA",
                "modal_content": "Analizamos tus datos, integramos modelos preentrenados y desplegamos pipelines de IA que generan valor inmediato a tu negocio.",
                "process_title": "Proceso de Integración de IA",
                "process_description": "Análisis de requerimientos, integración de APIs de IA, desarrollo de funcionalidades personalizadas y optimización continua.",
                "process_steps": "Análisis, Integración de APIs, Desarrollo, Optimización",
            },
            {
                "title": "Desarrollo de ERP y CRM Personalizados",
                "icon": "flaticon-ui-design",
                "description": "Desarrollo de sistemas ERP y CRM totalmente ajustados a tus flujos internos.",
                "additional_info": "Caso real: implementación de ERP que redujo un 25% los tiempos de facturación.",
                "modal_image": "services/erp_crm_development.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Desarrollo de ERP y CRM",
                "modal_content": "Analizamos procesos, modelamos la base de datos y desarrollamos módulos a medida para optimizar cada área de tu empresa.",
                "process_title": "Proceso de Desarrollo de ERP y CRM",
                "process_description": "Reunión de requisitos, diseño de base de datos robusta, desarrollo de módulos específicos e integración continua.",
                "process_steps": "Planificación, Diseño, Desarrollo, Integración, Soporte",
            },
            {
                "title": "Servicios DevOps",
                "icon": "flaticon-web-design",
                "description": "Automatización de despliegues y gestión de infraestructura con Docker y Kubernetes.",
                "additional_info": "Ejemplo: pipeline CI/CD en GitLab que redujo en 60% el tiempo de entrega.",
                "modal_image": "services/devops.webp",
                "modal_subtitle": "SERVICES",
                "modal_title": "Servicios DevOps",
                "modal_content": "Configuramos contenedores multi-stage, definimos workflows de CI/CD y aplicamos monitoreo continuo para mantener tus proyectos siempre online.",
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