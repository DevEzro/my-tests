from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml
import subprocess
import os
from fastapi.responses import FileResponse

app = FastAPI()

# Modelo para crear el proyecto
class ProyectoAvalonia(BaseModel):
    nombre: str
    ruta: str
    so: str

# Endpoint para crear el proyecto, compilarlo y publicarlo
@app.post("/proyecto-avalonia/")
def proyecto_avalonia(proyecto_data: ProyectoAvalonia):
    nombre = proyecto_data.nombre
    ruta = proyecto_data.ruta
    so = proyecto_data.so

    try:
        # Si el SO es Windows, crea el proyecto con las instrucciones adecuadas
        if so.lower() == "windows":
            os.chdir(ruta)
            comando = ["dotnet", "new", "avalonia.app", "-n", nombre]
            resultado = subprocess.run(comando, check=True, capture_output=True, text=True)

            ruta_instalador = os.path.join(ruta, nombre)
            # Compila el proyecto para obtener el '.exe'
            try:
                # Comando de publicación que incluye las dependencias para que se ejecute correctamente
                compilado = [
                        "dotnet", "publish", ruta_instalador, 
                        "--configuration", "Release", 
                        "--self-contained", 
                        "-r", "win-x64", 
                        "/p:PublishSingleFile=true", 
                        "/p:IncludeNativeLibrariesForSelfExtract=true", 
                        "/p:PublishTrimmed=false"
                ]
                    
                resultado = subprocess.run(compilado, check=True, capture_output=True, text=True)
                print(f"Resultado de la publicación: {resultado.stdout}")
                
                # Ruta del ejecutable publicado
                ruta_windows = os.path.join(ruta_instalador, "bin", "Release", "net8.0", "win-x64", "publish", f"{nombre}.exe")
                print(f"Buscando ejecutable en: {ruta_windows}")
                    
                if os.path.isfile(ruta_windows):
                    return FileResponse(
                        path=ruta_windows,
                        filename=f"{nombre}.exe",
                        media_type='application/octet-stream'
                    )
                # Errores y casos de uso
                else:
                    raise HTTPException(status_code=500, detail="No se pudo encontrar el archivo ejecutable publicado.")

            except subprocess.CalledProcessError as e:
                raise HTTPException(status_code=500, detail=f"Error al publicar el proyecto: {e.stderr}")

        elif so.lower() == "linux":
            os.chdir(ruta)
            comando = ["sudo", "dotnet", "new", "avalonia.app", "-n", nombre]
            resultado = subprocess.run(comando, check=True, capture_output=True, text=True)
        
            ruta_instalador = os.path.join(ruta, nombre)
            try:
                # Comando de publicación que incluye las dependencias para que se ejecute correctamente
                compilado = [
                    "sudo", "dotnet", "publish", ruta_instalador, 
                    "--configuration", "Release", 
                    "--self-contained", 
                    "-r", "linux-x64", 
                    "/p:PublishSingleFile=true", 
                    "/p:IncludeNativeLibrariesForSelfExtract=true", 
                    "/p:PublishTrimmed=false"
                ]
                
                resultado = subprocess.run(compilado, check=True, capture_output=True, text=True)
                print(f"Resultado de la publicación: {resultado.stdout}")
                
                # Ruta del ejecutable publicado
                ruta_linux = os.path.join(ruta_instalador, "bin", "Release", "net8.0", "linux-x64", "publish", f"{nombre}")
                print(f"Buscando ejecutable en: {ruta_linux}")

                if os.path.isfile(ruta_linux):
                    # Dar permisos de ejecución al archivo antes de servirlo
                    os.chmod(ruta_linux, 0o755)  # Esto otorga permisos de lectura, escritura y ejecución

                    return FileResponse(
                        path=ruta_linux,
                        filename=f"{nombre}",
                        media_type='application/octet-stream',
                    )
                # Errores y casos de uso
                else:
                    raise HTTPException(status_code=500, detail="No se pudo encontrar el archivo ejecutable publicado.")
            except subprocess.CalledProcessError as e:
                raise HTTPException(status_code=500, detail=f"Error al publicar el proyecto: {e.stderr}")
            
        else:
            raise HTTPException(status_code=501, detail=f"Generación de instaladores no implementada para {so}")
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el proyecto: {e.stderr}")
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"La ruta destino '{ruta}' no existe.")