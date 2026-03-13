import argparse

# --- CLI Argument Parser ---
parser_cli = argparse.ArgumentParser(
    description="Herramienta CLI para organizar archivos por extensión, detectar duplicados y crear snapshots (ZIP).",
    epilog="Ejemplos de uso:\n  tool organize --dir ./mi_carpeta --log --no-zip\n  tool snap create --name antes-de-cambios\n  tool snap list\n  tool snap restore antes-de-cambios --target ./restaurado",
    usage=None,
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# --- Subparsers for commands ---
subparsers = parser_cli.add_subparsers(
    dest='command', title='Subcomandos', description='Comandos disponibles',
    help='Descripción de los comandos', required=True)

# --- Organize command ---
cmd_organize = subparsers.add_parser(
    'organize',
    help='Organiza los archivos en diferentes carpetas segun su extensión.'
)

cmd_organize.add_argument(
    '--dir',
    type=str,
    default='.',
    help='Directorio a organizar.'
)

cmd_organize.add_argument(
    '--simulate',
    action='store_true',
    help='Modo dry-run: no se realizan cambios, solo se muestra lo que se haría.'
)

cmd_organize.add_argument(
    '--log',
    action='store_true',
    help='Crea un archivo de log con las operaciones realizadas.'
)

cmd_organize.add_argument(
    '--no-zip',
    dest='create_zip',
    action='store_false',
    help='No crear un archivo ZIP con los archivos procesados.'
)

cmd_organize.add_argument(
    '--change-template',
    action='store_true',
    help='Cambia la plantilla de organización de archivos.'
)

cmd_organize.add_argument(
    '--no-duplicates',
    dest='detect_duplicates',
    action='store_false',
    help='No detectar archivos duplicados por hash ni moverlos a la carpeta "duplicados".'
)

# --- Report command ---

cmd_report = subparsers.add_parser(
    'report',
    help='Genera un informe de los archivos organizados, incluyendo estadísticas y posibles errores.'
)

cmd_report_exgroup = cmd_report.add_mutually_exclusive_group()

cmd_report_exgroup.add_argument(
    '--output',
    type=str,
    default="./report.txt",
    help='Archivo de salida para el informe generado.'
)

cmd_report_exgroup.add_argument(
    '--show',
    action='store_true',
    help='Muestra el informe en consola lugar de guardar en un archivo.'
)

cmd_report.add_argument(
    '--simulate',
    action='store_true',
    help='Modo dry-run: no se generan cambios, solo se muestra lo que se haría.'
)

# --- Config command ---
cmd_config = subparsers.add_parser(
    'config',
    help='Configura las opciones predeterminadas para la organización de archivos en el archivo de configuración JSON.',
)

cmd_config.add_argument(
    '--set',
    nargs=2,
    metavar=('OPCIÓN', 'VALOR'),
    help='Establece una opción de configuración. Ejemplo: --set organize_template "nuevo_template.json"'
)

cmd_config.add_argument(
    '--show',
    action='store_true',
    help='Muestra la configuración actual en consola.'
)

cmd_config.add_argument(
    '--simulate',
    action='store_true',
    help='Modo dry-run: no se realizan cambios, solo se muestra lo que se haría.'
)

# --- List command ---
cmd_list = subparsers.add_parser(
    'list',
    help='Lista los archivos organizados, mostrando su nueva ubicación y cualquier error encontrado.'
)

cmd_list.add_argument(
    '--dir',
    type=str,
    default='.',
    help='Directorio a listar.'
)

# --- Search command ---
cmd_search = subparsers.add_parser(
    'search',
    help='Busca archivos organizados por nombre, extensión o fecha de modificación.'
)

cmd_search.add_argument(
    '--name',
    type=str,
    help='Busca archivos por nombre.'
)

cmd_search.add_argument(
    '--extension',
    type=str,
    help='Busca archivos por extensión.'
)

cmd_search.add_argument(
    '--date',
    type=str,
    help='Busca archivos por fecha de modificación.'
)

# --- Snap command ---
cmd_snap = subparsers.add_parser(
    'snap',
    help='Módulo de snapshots para guardar y restaurar estados de organización de archivos.'
)

snap_sub = cmd_snap.add_subparsers(
    dest='snap_command',
    title='Subcomandos de snap',
    description='Comandos disponibles para snap',
    help='Descripción de los comandos de snap',
    required=True
)

# --- Snap create subcommand ---
snap_create = snap_sub.add_parser(
    'create',
    help='Crea un snapshot (ZIP) del directorio especificado.'
)

snap_create.add_argument(
    '--dir',
    type=str,
    default='.',
    help='Directorio cuyo estado será capturado en el snapshot.'
)

snap_create.add_argument(
    '--name',
    type=str,
    help='Nombre del snapshot (se usará para el nombre del archivo ZIP).' 
)

snap_create.add_argument(
    '--description',
    type=str,
    help='Descripción del snapshot a crear.'
)

snap_create.add_argument(
    '--simulate',
    action='store_true',
    help='Modo dry-run: no se generan cambios, solo se muestra lo que se haría.'
)

# --- Snap list subcommand ---
snap_list = snap_sub.add_parser(
    'list',
    help='Lista los snapshots disponibles.'
)

snap_list.add_argument(
    '--dir',
    type=str,
    default='.',
    help='Directorio donde se encuentran los snapshots (por defecto: actual).'
)

# --- Snap restore subcommand ---
snap_restore = snap_sub.add_parser(
    'restore',
    help='Restaura un snapshot en un directorio destino.'
)

snap_restore.add_argument(
    'name',
    type=str,
    help='Nombre del snapshot a restaurar (sin extensión .zip).'
)

snap_restore.add_argument(
    '--target',
    type=str,
    default='.',
    help='Directorio donde se restaurará el snapshot.'
)

snap_restore.add_argument(
    '--overwrite',
    action='store_true',
    help='Sobrescribir archivos existentes en el directorio destino.'
)

snap_restore.add_argument(
    '--simulate',
    action='store_true',
    help='Modo dry-run: no se generan cambios, solo se muestra lo que se haría.'
)

# --- Snap delete subcommand ---
snap_delete = snap_sub.add_parser(
    'delete',
    help='Elimina un snapshot existente.'
)

snap_delete.add_argument(
    'name',
    type=str,
    help='Nombre del snapshot a eliminar (sin extensión .zip).'
)

snap_delete.add_argument(
    '--simulate',
    action='store_true',
    help='Modo dry-run: no se generan cambios, solo se muestra lo que se haría.'
)