from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import Calimaco, GestionRW

def index(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def inicio_login(request):
    return render(request, "inicio_login.html")

def cargar_archivo(request):
    try:
        if request.method == "POST":
            archivo = request.FILES.get("archivo")
            if not archivo:
                return JsonResponse(
                    {
                        "status_server": "error",
                        "message": "No se ha subido ningún archivo.",
                    }
                )

            try:
                if archivo.name.endswith(".xlsx") or archivo.name.endswith(".xls"):
                    df = pd.read_excel(archivo, header=0)
                elif archivo.name.endswith(".csv"):
                    df = pd.read_csv(archivo, header=0)
                else:
                    return JsonResponse(
                        {
                            "status_server": "error",
                            "message": "El archivo debe ser un archivo de Excel o CSV válido.",
                        }
                    )

                print(f"Archivo cargado correctamente: {archivo.name}")

                # Imprimir los nombres de las columnas antes de normalizarlas
                print(f"Columnas del archivo antes de normalizar: {list(df.columns)}")

                # Normalizar los nombres de las columnas (eliminar espacios, convertir a minúsculas)
                df.columns = df.columns.str.strip().str.lower()

                # Imprimir los nombres de las columnas después de normalizarlas
                print(f"Columnas del archivo después de normalizar: {list(df.columns)}")

            except Exception as e:
                print(f"Error al leer el archivo: {str(e)}")
                return JsonResponse(
                    {
                        "status_server": "error",
                        "message": f"Error al leer el archivo: {str(e)}",
                    }
                )

            # Diccionario para mapear nombres esperados a sus equivalentes normalizados
            column_mapping = {
                "identifer_cal": "identifer_cal",
                "fecha": "fecha",
                "estado": "estado",
                "fecha_modificacion": "fecha_modificacion",
                "usuario": "usuario",
                "email": "email",
                "cantidad": "cantidad",
                "id_externo": "id_externo",
                "metodo": "metodo",
                "respuesta": "respuesta",
                "agente": "agente",
                "fecha_de_registro_del_jugador": "fecha_de_registro_del_jugador",
            }

            # Verifica que las columnas requeridas existen en el archivo
            for key, normalized_name in column_mapping.items():
                if normalized_name not in df.columns:
                    print(f"Falta la columna: {key}")
                    return JsonResponse(
                        {
                            "status_server": "error",
                            "message": f"El archivo no tiene la columna {key}.",
                        }
                    )

            for _, row in df.iterrows():
                print(row)
                try:
                    Calimaco.objects.update_or_create(
                        identifer_cal=row[column_mapping["identifer_cal"]],
                        fecha=row[column_mapping["fecha"]],
                        estado=row[column_mapping["estado"]],
                        fecha_modificacion=row[column_mapping["fecha_modificacion"]],
                        usuario=row[column_mapping["usuario"]],
                        email=row[column_mapping["email"]],
                        cantidad=row[column_mapping["cantidad"]],
                        id_externo=row[column_mapping["id_externo"]],
                        metodo=row[column_mapping["metodo"]],
                        respuesta=row[column_mapping["respuesta"]],
                        agente=row[column_mapping["agente"]],
                        fecha_de_registro_del_jugador=row[
                            column_mapping["fecha_de_registro_del_jugador"]
                        ],
                    )
                except Exception as e:
                    print(f"Error procesando la fila: {row} - {str(e)}")
                    return JsonResponse(
                        {
                            "status_server": "error",
                            "message": f"Error procesando los datos del archivo: {str(e)}",
                        }
                    )

            return JsonResponse(
                {
                    "status_server": "success",
                    "message": "Felicitaciones, la data fue importada correctamente 😉",
                }
            )
        else:
            return render(request, "inicio_login.html")

    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")
        return JsonResponse({
                "status_server": "error",
                "message": f"Error interno del servidor: {str(e)}",
            }
        )

def cargar_archivo_gestionrw(request):
    try:
        if request.method == "POST":
            archivo = request.FILES.get("archivo")
            if not archivo:
                return JsonResponse(
                    {
                        "status_server": "error",
                        "message": "No se ha subido ningún archivo.",
                    }
                )

            try:
                if archivo.name.endswith(".xlsx") or archivo.name.endswith(".xls"):
                    df = pd.read_excel(archivo, header=0)
                elif archivo.name.endswith(".csv"):
                    df = pd.read_csv(archivo, header=0)
                else:
                    return JsonResponse(
                        {
                            "status_server": "error",
                            "message": "El archivo debe ser un archivo de Excel o CSV válido.",
                        }
                    )

                print(f"Archivo cargado correctamente: {archivo.name}")

                # Imprimir los nombres de las columnas antes de normalizarlas
                print(f"Columnas del archivo antes de normalizar: {list(df.columns)}")

                # Normalizar los nombres de las columnas (eliminar espacios, convertir a minúsculas)
                df.columns = df.columns.str.strip().str.lower()

                # Imprimir los nombres de las columnas después de normalizarlas
                print(f"Columnas del archivo después de normalizar: {list(df.columns)}")

            except Exception as e:
                print(f"Error al leer el archivo: {str(e)}")
                return JsonResponse(
                    {
                        "status_server": "error",
                        "message": f"Error al leer el archivo: {str(e)}",
                    }
                )

            # Diccionario para mapear nombres esperados a sus equivalentes normalizados
            column_mapping = {
                "identifier": "identifier",
                "local": "local",
                "registro": "registro",
                "tipo": "tipo",
                "proveedor": "proveedor",
                "bono": "bono",
                "telefono": "telefono",
                "tipo_documento": "tipo_documento",
                "numero_documento": "numero_documento",
                "web_id": "web_id",
                "cliente": "cliente",
                "recarga": "recarga",
                "bono_5_por_ciento": "bono_5_por_ciento",
                "promotor": "promotor",
            }

            # Verifica que las columnas requeridas existen en el archivo
            for key, normalized_name in column_mapping.items():
                if normalized_name not in df.columns:
                    print(f"Falta la columna: {key}")
                    return JsonResponse(
                        {
                            "status_server": "error",
                            "message": f"El archivo no tiene la columna {key}.",
                        }
                    )

            for _, row in df.iterrows():
                print(row)
                try:
                    GestionRW.objects.update_or_create(
                        identifier=row[column_mapping["identifier"]],
                        local=row[column_mapping["local"]],
                        registro=row[column_mapping["registro"]],
                        tipo=row[column_mapping["tipo"]],
                        proveedor=row[column_mapping["proveedor"]],
                        bono=row[column_mapping["bono"]],
                        telefono=row[column_mapping["telefono"]],
                        tipo_documento=row[column_mapping["tipo_documento"]],
                        numero_documento=row[column_mapping["numero_documento"]],
                        web_id=row[column_mapping["web_id"]],
                        cliente=row[column_mapping["cliente"]],
                        recarga=row[column_mapping["recarga"]],
                        bono_5_por_ciento=row[column_mapping["bono_5_por_ciento"]],
                        promotor=row[column_mapping["promotor"]],
                    )
                except Exception as e:
                    print(f"Error procesando la fila: {row} - {str(e)}")
                    return JsonResponse(
                        {
                            "status_server": "error",
                            "message": f"Error procesando los datos del archivo: {str(e)}",
                        }
                    )

            return JsonResponse(
                {
                    "status_server": "success",
                    "message": "Felicitaciones, la data fue importada correctamente got",
                }
            )
        else:
            return render(request, "cargar_gestionrw.html")

    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")
        return JsonResponse(
            {
                "status_server": "error",
                "message": f"Error interno del servidor: {str(e)}",
            }
        )
