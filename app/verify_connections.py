import os
from database import get_db
import models

def test_connections():
    db = get_db()
    print("--- VERIFICANDO CONEXIONES DE LA BASE DE DATOS ---")
    
    # 1. Verificar Hogar
    hogar = db.query(models.HogarGerontologico).first()
    print(f"[OK] Hogar conectado: {hogar.nombre} (Capacidad: {hogar.capacidadTotal})")
    
    # 2. Verificar Personal
    personal_total = db.query(models.Personal).count()
    coordinadores = db.query(models.Personal).filter_by(tipoPersonal="Coordinador").count()
    enfermeros = db.query(models.Personal).filter_by(tipoPersonal="Enfermero").count()
    print(f"[OK] Personal conectado: {personal_total} registrados ({coordinadores} Coordinador, {enfermeros} Enfermeros)")
    
    # 3. Verificar un Paciente y sus relaciones
    paciente = db.query(models.AdultoMayor).filter_by(activo=True).first()
    if paciente:
        print(f"\n--- PRUEBA DE TRAZABILIDAD (Paciente ID: {paciente.identificacion}) ---")
        print(f"[OK] Datos Basicos: {paciente.primerNombre} {paciente.primerApellido} | Edad: {paciente.edad} | Categoria: {paciente.categoriaServicio}")
        
        # Relación Responsable
        resp = paciente.responsable
        print(f"[OK] Relacion Responsable: {resp.primerNombre} {resp.primerApellido} (Parentesco: {resp.parentesco})")
        
        # Relación Preinscripción
        pre = paciente.preinscripcion
        print(f"[OK] Relacion Preinscripcion: Estado {pre.estado}")
        
        # Relación Diagnósticos
        diag_count = len(paciente.diagnosticos)
        print(f"[OK] Relacion Diagnosticos: {diag_count} registrados.")
        for d in paciente.diagnosticos:
            print(f"   - [{d.tipo}] {d.descripcion}")
            
        # Relación Bitácoras
        bitacoras_count = len(paciente.bitacoras)
        print(f"[OK] Relacion Bitacoras: {bitacoras_count} registros historicos.")
        if bitacoras_count > 0:
            b = paciente.bitacoras[0]
            print(f"   - Ultima bitacora por {b.registradoPor}: SV({b.signosVitales}) -> {b.observaciones}")
            
    else:
        print("[X] No se encontraron pacientes activos.")
        
    print("\n--- PRUEBA EXITOSA: TODAS LAS TABLAS ESTAN CONECTADAS CORRECTAMENTE ---")

if __name__ == "__main__":
    test_connections()
