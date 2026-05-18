# Clínica Veterinaria - Módulo Odoo 17

Módulo personalizado para Odoo 17 que permite gestionar una clínica veterinaria:
dueños, mascotas, citas y seguimiento de tratamientos.

## Requisitos

- Docker Desktop instalado
- Odoo 17
- PostgreSQL 15

## Instalación

1. Clona o descarga el repositorio en tu máquina local.

2. Copia la carpeta `vet_clinic` en el directorio de addons de tu instalación de Odoo,
   en nuestro caso `volumesOdoo/addons/`.

3. Levanta los contenedores:
```bash
   docker compose up -d
```

4. Accede a `http://localhost:8069` y configura la base de datos.

5. Ve a **Aplicaciones**, actualiza la lista y busca `Clinica Veterinaria`.

6. Haz click en **Instalar**.

7. Ve a **Ajustes → Usuarios → admin** y añade el grupo **Administrador Veterinario**
   para que el módulo aparezca en el menú principal.

## Uso

Una vez instalado, el módulo aparece en el menú de aplicaciones como **Clínica Veterinaria**.
Contiene cuatro secciones:

- **Dueños**: gestión de los propietarios de las mascotas.
- **Mascotas**: registro de animales con su especie, raza, peso y dueño asociado.
- **Citas**: gestión de consultas veterinarias con vista kanban por estado.
- **Tratamientos**: seguimiento post-consulta con vista kanban por estado de recuperación.

## Grupos y permisos

| Grupo | Permisos |
|---|---|
| Administrador Veterinario | Lectura, escritura, creación y borrado en todos los modelos |
| Usuario Veterinario | Lectura en dueños y mascotas. Lectura, escritura y creación en citas y tratamientos. Sin borrado. |

## Estructura del módulo

```
vet_clinic/
├── controllers/
├── models/
│   ├── owner.py
│   ├── pet.py
│   ├── appointment.py
│   └── treatment.py
├── views/
│   ├── owner_views.xml
│   ├── pet_views.xml
│   ├── appointment_views.xml
│   ├── treatment_views.xml
│   └── menu.xml
├── security/
│   ├── groups.xml
│   └── ir.model.access.csv
├── report/
│   └── appointment_report.xml
├── static/
│   └── description/
│       └── icon.png
└── __manifest__.py
```
