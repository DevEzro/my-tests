# IMPORTS
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
import os, platform, subprocess

app = FastAPI()

# CAMPOS
class Source(BaseModel):
    sistema_operativo: str
    fuentes: list[str]

class InstallerResponse(BaseModel):
    installer_path: str
    os: str

# ENDPOINT
@app.post("/generate-installer", response_model=InstallerResponse)
async def generate_installer(source: Source):
    sistema_operativo = source.sistema_operativo
    fuentes = source.fuentes

    # GENERA EL INSTALADOR
    installer_path = create_installer(fuentes)

    # SI DA ERROR MUESTRA MENSAJE Y NO CREA EL INSTALADOR
    if not installer_path:
        raise HTTPException(status_code=500, detail="Error generating installer.")

    # RETURN DEL INSTALADOR Y DEL SISTEMA OPERATIVO
    return InstallerResponse(installer_path=installer_path, os=sistema_operativo)

# CREA EL INSTALADOR
def create_installer(fuentes):
    try:
        # Suponiendo que la fuente es el script principal que deseas empaquetar
        # Asegúrate de que el primer elemento de 'fuentes' sea un script de Python
        script_path = fuentes[0]  # Usamos la primera fuente como el script principal

        # DIR TEMPORAL PARA EL INSTALDOR
        temp_dir = "temp_installer"
        os.makedirs(temp_dir, exist_ok=True)

        # PYINSTALLER PARA CREAR EL EJECUTABLE JUNTO CON PARÁMETROS
        subprocess.run(["pyinstaller", "--onefile", script_path], cwd=temp_dir)

        # GUARDA EL INSTALADOR EN LA RUTA INDICADA
        installer_path = os.path.join(temp_dir, "dist", os.path.basename(script_path).replace('.py', ''))

        # COMPRUEBA QUE SE CREÓ BIEN
        if not os.path.exists(installer_path):
            raise Exception("El instalador no se generó correctamente.")

        return installer_path
    except Exception as e:
        print(f"Error generating installer: {e}")
        return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
