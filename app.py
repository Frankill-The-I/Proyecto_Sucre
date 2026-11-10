import os
from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd

@app.route('/importar', methods=['GET', 'POST'])
def importar_excel():
    if request.method == 'POST':
        
        if 'archivo_excel' not in request.files:
            flash('No se seleccionó ningún archivo', 'danger')
            return redirect(request.url)
            
        archivo = request.files['archivo_excel']
        
        if archivo.filename == '':
            flash('Archivo no válido', 'danger')
            return redirect(request.url)
            
        if archivo and archivo.filename.endswith('.xlsx'):
            
            df = pd.read_excel(archivo)
            
            
            for index, row in df.iterrows():
                cedula = str(row['Cedula'])
                nombre = row['Nombre']
                apellido = row['Apellido']
                
            
         
            flash('¡Importación de estudiantes realizada con éxito!', 'success')
            return redirect(url_for('importar_excel'))
            
    return render_template('importar.html')