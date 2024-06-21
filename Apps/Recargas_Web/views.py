from django.shortcuts import render
import pandas as pd
from .models import Calimaco
from django.http import JsonResponse

def inicio_login(request):
    return render(request, 'inicio_login.html')

def cargar_archivo(request):
    try:
        if request.method == 'POST':
            archivo = request.FILES.get('archivo')
            if not archivo:
                return JsonResponse({'status_server': 'error', 'message': 'No se ha subido ningún archivo.'})

            try:
                if archivo.name.endswith('.xlsx') or archivo.name.endswith('.xls'):
                    df = pd.read_excel(archivo, header=0)
                elif archivo.name.endswith('.csv'):
                    df = pd.read_csv(archivo, header=0)
                else:
                    return JsonResponse({'status_server': 'error', 'message': 'El archivo debe ser un archivo de Excel o CSV válido.'})

                print(f"Archivo cargado correctamente: {archivo.name}")

                # Imprimir los nombres de las columnas antes de normalizarlas
                print(f"Columnas del archivo antes de normalizar: {list(df.columns)}")

                # Normalizar los nombres de las columnas (eliminar espacios, convertir a minúsculas)
                df.columns = df.columns.str.strip().str.lower()

                # Imprimir los nombres de las columnas después de normalizarlas
                print(f"Columnas del archivo después de normalizar: {list(df.columns)}")

            except Exception as e:
                print(f"Error al leer el archivo: {str(e)}")
                return JsonResponse({'status_server': 'error', 'message': f'Error al leer el archivo: {str(e)}'})

            # Diccionario para mapear nombres esperados a sus equivalentes normalizados
            column_mapping = {
                'cliente': 'Cliente',
                'fecha': 'Fecha',
                'estado': 'Estado',
                'fecha de modificacion': 'Fecha_de_modificacion',
                'usuario': 'Usuario',
                'email': 'Email',
                'cantidad': 'Cantidad',
                'id externo': 'Id_externo',
                'respuesta': 'Respuesta',
                'agente': 'Agente',
                'fecha de registro del jugador': 'Fecha_de_registro_del_jugador'
            }

            # Verifica que las columnas requeridas existen en el archivo
            for key, normalized_name in column_mapping.items():
                if normalized_name not in df.columns:
                    print(f"Falta la columna: {key}")
                    return JsonResponse({'status_server': 'error', 'message': f'El archivo no tiene la columna {key}.'})

            for _, row in df.iterrows():
                try:
                    Cliente = row[column_mapping['cliente']]
                    Fecha = row[column_mapping['fecha']]
                    Estado = row[column_mapping['estado']]
                    Fecha_de_modificacion = row[column_mapping['fecha de modificacion']]
                    Usuario = row[column_mapping['usuario']]
                    Email = row[column_mapping['email']]
                    Cantidad = row[column_mapping['cantidad']]
                    Id_externo = row[column_mapping['id externo']]
                    Respuesta = row[column_mapping['respuesta']]
                    Agente = row[column_mapping['agente']]
                    Fecha_de_registro_del_jugador = row[column_mapping['fecha de registro del jugador']]

                    Calimaco.objects.update_or_create(
                        Email=Email,
                        defaults={
                            'Cliente': Cliente,
                            'Fecha': Fecha,
                            'Estado': Estado,
                            'Fecha_de_modificacion': Fecha_de_modificacion,
                            'Usuario': Usuario,
                            'Id_externo': Id_externo,
                            'Cantidad': Cantidad,
                            'Respuesta': Respuesta,
                            'Agente': Agente,
                            'Fecha_de_registro_del_jugador': Fecha_de_registro_del_jugador,
                        }
                    )
                except Exception as e:
                    print(f"Error procesando la fila: {row} - {str(e)}")
                    return JsonResponse({'status_server': 'error', 'message': f'Error procesando los datos del archivo: {str(e)}'})

            return JsonResponse({'status_server': 'success', 'message': 'Felicitaciones, la data fue importada correctamente 😉'})
        else:
            return render(request, 'inicio_login.html')

    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")
        return JsonResponse({'status_server': 'error', 'message': f'Error interno del servidor: {str(e)}'})
