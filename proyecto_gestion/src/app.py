from flask import Flask, render_template,request,redirect, url_for,flash,session 
from datetime import datetime 
from flask import send_from_directory
import os  
import database as db

# con esto accedemos a la carpeta "proyecto_gestion"
template_dir= os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# unimos las carpetas src y templates a la carpeta del proyecto
template_dir=os.path.join(template_dir,'src','templates')

#inicializamos flask 
app = Flask(__name__,template_folder=template_dir)

#sesiones
app.secret_key="develoteca"

# ======rutas de la aplicacion===== 
# === Pagina de Inicio ===
@app.route('/')
def home():
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM informacionweb")
    myresult = cursor.fetchall()
    # convertimos los datos a diccionario
    insertObject=[]
    columNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close()
    print(insertObject)
    return render_template('index.html', data=insertObject)

@app.route('/')
def home_base():
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM informacionweb")
    myresult = cursor.fetchall()
    # convertimos los datos a diccionario
    insertObject=[]
    columNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close()
    print(insertObject)
    return render_template('base.html', data=insertObject)

# === IMAGENES ===
@app.route('/img/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/img'),imagen) 






@app.route('/evento.html')
def evento():
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM evento_academico")
    eventos = cursor.fetchall()
    db.database.commit()
    return render_template('evento.html',eventos_acad=eventos)


@app.route('/programa_general.html')
def programa_general():

    return render_template('programa_general.html')

# =================== ADMINISTRADOR ===================

@app.route('/admin/')
def administrador():
    if not 'login' in session  or session["tipo_usuario"]!="admin" :
        return redirect("/admin/login")
    return render_template('admin/index.html')

@app.route('/admin/login')
def login_admin():

    return render_template('admin/login.html')

@app.route('/admin/login', methods=['POST'])
def login_admin_post():
    _usuario=request.form['txtusuarioAdmin']
    _password=request.form['txtpasswordAdmin']
    print(_usuario)
    print(_password)
        
    #aumentar para la base de datos 2:43:01 (ya esta)
    cursor=db.database.cursor()
    cursor.execute("SELECT usuario, contrasena,tipo FROM usuario WHERE tipo='admin'")
    admin = cursor.fetchone()
    db.database.commit()
        
    usuario_admin=str(admin[0])
    pass_admin=str(admin[1])
    tipo_usuario = str(admin[2])

    

    if _usuario==usuario_admin and _password==pass_admin:
        session["login"]=True
        session["usuario"]="Administrador" 
        session["tipo_usuario"]=tipo_usuario
        return redirect('/admin')   
    return render_template('/admin/login.html',mensaje="Acceso denegado")

# ________ configuracion  de informacion web __________

@app.route('/admin/informacion_web')
def login_admin_inf_web():
    if not 'login' in session or session["tipo_usuario"]!="admin":
        return redirect("/admin/login")
    
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM informacionweb")
    informacion_web = cursor.fetchall()
    db.database.commit()
    #print(informacion_web)
    
    return render_template('admin/informacion_web.html',infor_web=informacion_web)

# editar imagen e informacion web:

@app.route('/admin/informacion_web/editar_img/<string:id>',methods=['POST'])
def informacion_web_editar_imagen(id):
    tiempo=datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')
    _imagenx = request.files['img_logo']
    _imagen_portadax = request.files['img_portada1']
    _imagen_portada2x = request.files['img_portada2']
    _imagen_portada3x = request.files['img_portada3']
    if _imagenx.filename!="":
        _imagen = request.files['img_logo']
        # Resto del código para procesar la imagen
        if _imagen.filename!="":
            nuevoNombre=horaActual+" "+_imagen.filename
            _imagen.save("templates/img/"+nuevoNombre)
        else:
            nuevoNombre=None
        
        cursor=db.database.cursor()
        cursor.execute("SELECT logotipo, portada1,portada2,portada3 FROM informacionweb WHERE id_info=%s",(id,))
        evento = cursor.fetchone()
        db.database.commit()
        
        if nuevoNombre is not None and os.path.exists("templates/img/"+str(evento[0])):
            os.unlink("templates/img/"+str(evento[0]))
            
        
    else:
        cursor=db.database.cursor()
        cursor.execute("SELECT logotipo, portada1,portada2,portada3 FROM informacionweb WHERE id_info=%s",(id,))
        evento = cursor.fetchone()
        db.database.commit()
        
        nuevoNombre=str(evento[0])
        
    if _imagen_portadax.filename!="":
        _imagen_portada = request.files['img_portada1']
        
        # Resto del código para procesar la imagen
        if _imagen_portada.filename!="":
            nuevoNombre_portada=horaActual+" "+_imagen_portada.filename
            _imagen_portada.save("templates/img/"+nuevoNombre_portada)
        else:
            nuevoNombre_portada=None
        cursor=db.database.cursor()
        cursor.execute("SELECT logotipo, portada1,portada2,portada3 FROM informacionweb WHERE id_info=%s",(id,))
        evento = cursor.fetchone()
        db.database.commit()
        if nuevoNombre_portada is not None and os.path.exists("templates/img/"+str(evento[1])):
            os.unlink("templates/img/"+str(evento[1]))
        
        
    else:
        cursor=db.database.cursor()
        cursor.execute("SELECT logotipo, portada1,portada2,portada3 FROM informacionweb WHERE id_info=%s",(id,))
        evento = cursor.fetchone()
        db.database.commit()
        nuevoNombre_portada=str(evento[1])
    
    #portada 2:
    
    if _imagen_portada2x.filename!="":
        _imagen_portada2 = request.files['img_portada2']
        
        # Resto del código para procesar la imagen
        if _imagen_portada2.filename!="":
            nuevoNombre_portada2=horaActual+" "+_imagen_portada2.filename
            _imagen_portada2.save("templates/img/"+nuevoNombre_portada2)
        else:
            nuevoNombre_portada2=None
        cursor=db.database.cursor()
        cursor.execute("SELECT logotipo, portada1,portada2,portada3 FROM informacionweb WHERE id_info=%s",(id,))
        evento = cursor.fetchone()
        db.database.commit()
        if nuevoNombre_portada2 is not None and os.path.exists("templates/img/"+str(evento[2])):
            os.unlink("templates/img/"+str(evento[2]))

    else:
        cursor=db.database.cursor()
        cursor.execute("SELECT logotipo, portada1,portada2,portada3 FROM informacionweb WHERE id_info=%s",(id,))
        evento = cursor.fetchone()
        db.database.commit()
        nuevoNombre_portada2=str(evento[2])
    
     #portada 3:
    
    if _imagen_portada3x.filename!="":
        _imagen_portada3 = request.files['img_portada3']
        
        # Resto del código para procesar la imagen
        if _imagen_portada3.filename!="":
            nuevoNombre_portada3=horaActual+" "+_imagen_portada3.filename
            _imagen_portada3.save("templates/img/"+nuevoNombre_portada3)
        else:
            nuevoNombre_portada3=None
        cursor=db.database.cursor()
        cursor.execute("SELECT logotipo, portada1,portada2,portada3 FROM informacionweb WHERE id_info=%s",(id,))
        evento = cursor.fetchone()
        db.database.commit()
        if nuevoNombre_portada3 is not None and os.path.exists("templates/img/"+str(evento[3])):
            os.unlink("templates/img/"+str(evento[3]))

    else:
        cursor=db.database.cursor()
        cursor.execute("SELECT logotipo, portada1,portada2,portada3 FROM informacionweb WHERE id_info=%s",(id,))
        evento = cursor.fetchone()
        db.database.commit()
        nuevoNombre_portada3=str(evento[3])
      
    
    cursor2 = db.database.cursor()
    sql="UPDATE `informacionweb` SET logotipo=%s, portada1=%s,portada2=%s,portada3=%s WHERE id_info=%s"
    datos=(nuevoNombre,nuevoNombre_portada,nuevoNombre_portada2,nuevoNombre_portada3, id)
    cursor2.execute(sql,datos)
    db.database.commit()
  
    return redirect("/admin/informacion_web")

# editar texto:
    
@app.route('/admin/informacion_web/editar/<string:id>',methods=['POST'])
def informacion_web_editar(id):
    _nom=request.form['txtnombre']
    _desc=request.form['txtdesc']
    _mision=request.form['txtmision']
    _vision=request.form['txtvision']
    _obj=request.form['txtobj']
    _direc=request.form['txtdirec']
    _contacto=request.form['txtcontacto']
    _correo=request.form['txtcorreo']
    
    
    if _nom and _desc and _mision and _vision and _obj and _direc and _contacto and _correo :
        cursor = db.database.cursor()
        sql="UPDATE `informacionweb` SET`direccion`=%s,`descripcion`=%s,`mision`=%s,`vision`=%s,`objetivo`=%s,`nombre`=%s,`celular`=%s,`correo_el`=%s WHERE id_info=%s"
        datos=( _direc ,_desc, _mision , _vision , _obj , _nom,_contacto , _correo,id)
        cursor.execute(sql,datos)
        db.database.commit()
    
    return redirect("/admin/informacion_web")
    
# ________ configuracion  de eventos __________

@app.route('/admin/gestion_eventos')
def login_admin_eventos():
    if not 'login' in session  or session["tipo_usuario"]!="admin":
        return redirect("/admin/login")
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM evento_academico")
    evento_acad = cursor.fetchall()
    db.database.commit()
    return render_template('admin/gestion_eventos.html',eventos=evento_acad)


@app.route('/admin/gestion_eventos/guardar',methods=['POST'])
def login_admin_evento_guardar():
    _titulo=request.form['txttituloevento']
    _tipo=request.form['txttipoevento']
    _capmax=request.form['txtcapmaxevento']
    _precio=request.form['txtprecioevento']
    _descripcion=request.form['txtdescevento']
    _area=request.form['txtareaevento']
    _fecha=request.form['txtfechaevento']
    _imagen=request.files['txtimagenevento']
    
    tiempo=datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')
    
    if _imagen.filename!="":
        nuevoNombre=horaActual+" "+_imagen.filename
        _imagen.save("templates/img/"+nuevoNombre)
        
    sql="INSERT INTO `evento_academico`(`id_evento`, `tipo`, `portada_even`, `capacidadmax`, `precio`, `titulo`, `descripcion`, `area`, `fecha`, `id_control`, `id_administrador`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,NULL,NULL);"
    datos=(_tipo,nuevoNombre,_capmax,_precio,_titulo,_descripcion,_area,_fecha)
    
    cursor=db.database.cursor()
    cursor.execute(sql,datos)
    db.database.commit()
    
    return redirect('/admin/gestion_eventos')

@app.route('/admin/gestion_eventos/borrar',methods=['POST'])
def login_admin_evento_borrar():
    _id=request.form['txtID']
    
    cursor=db.database.cursor()
    cursor.execute("SELECT portada_even FROM evento_academico WHERE id_evento=%s",(_id,))
    evento = cursor.fetchall()
    db.database.commit()
   #print(evento)
    if os.path.exists("templates/img/"+str(evento[0][0])):
       os.unlink("templates/img/"+str(evento[0][0]))
    
    cursor=db.database.cursor()
    #cursor.execute("DELETE FROM `evento_academico` WHERE id_evento=%s",(_id,))
    cursor.execute("INSERT INTO evento_eliminado ( id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador) SELECT id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador FROM evento_academico WHERE id_evento = %s", (_id,))
    cursor.execute("DELETE FROM `evento_academico` WHERE id_evento=%s",(_id,))
    db.database.commit() 
    
    return redirect('/admin/gestion_eventos')

# editar imagen 

@app.route('/admin/gestion_eventos/editar_imagen/<string:id>',methods=['POST'])
def login_admin_evento_editar_imagen(id):
    
       
    _imagen=request.files['img_evento']
    tiempo=datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')
    
    if _imagen.filename!="":
        nuevoNombre=horaActual+" "+_imagen.filename
        _imagen.save("templates/img/"+nuevoNombre)
    else:
        return redirect('/admin/gestion_eventos')
    
    cursor=db.database.cursor()
    cursor.execute("SELECT portada_even FROM evento_academico WHERE id_evento=%s",(id,))
    evento = cursor.fetchall()
    db.database.commit()
    
    if os.path.exists("templates/img/"+str(evento[0][0])):
       os.unlink("templates/img/"+str(evento[0][0]))
       
    cursor = db.database.cursor()
    sql="UPDATE `evento_academico` SET portada_even=%s WHERE id_evento=%s"
    datos=(nuevoNombre,id)
    cursor.execute(sql,datos)
    db.database.commit()
    return redirect('/admin/gestion_eventos')
    
@app.route('/admin/gestion_eventos/editar/<string:id>',methods=['POST'])
def login_admin_evento_editar(id):
    _titulo=request.form['txttituloevento']
    _tipo=request.form['txttipoevento']
    _capmax=request.form['txtcapmaxevento']
    _precio=request.form['txtprecioevento']
    _descripcion=request.form['txtdescevento']
    _area=request.form['txtareaevento']
    _fecha=request.form['txtfechaevento']
    
    
    if _titulo and _tipo and _capmax and _precio and _descripcion and _area and _fecha :
        cursor = db.database.cursor()
        sql="UPDATE `evento_academico` SET tipo=%s, capacidadmax=%s, precio=%s, titulo=%s, descripcion=%s, area=%s, fecha=%s WHERE id_evento=%s"
        datos=(_tipo, _capmax,_precio,_titulo,_descripcion,_area,_fecha,id)
        cursor.execute(sql,datos)
        db.database.commit()
        
    return redirect('/admin/gestion_eventos')




# ________ configuracion  de participantes __________

@app.route('/admin/gestion_participantes')
def login_admin_participantes():
    if not 'login' in session  or session["tipo_usuario"]!="admin":
        return redirect("/admin/login")
    
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM usuario")
    myresult = cursor.fetchall()
    # convertimos los datos a diccionario
    insertObject=[]
    columNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close()
    
    return render_template('admin/gestion_participantes.html',data=insertObject)

@app.route('/admin/gestion_participantes/borrar',methods=['POST'])
def login_admin_participante_borrar():
    _id=request.form['txtID']
    
    
    cursor=db.database.cursor()
    #cursor.execute("DELETE FROM `evento_academico` WHERE id_evento=%s",(_id,))
    #cursor.execute("INSERT INTO evento_eliminado ( id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador) SELECT id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador FROM evento_academico WHERE id_evento = %s", (_id,))
    cursor.execute("DELETE FROM `usuario` WHERE id_usuario=%s",(_id,))
    db.database.commit() 
    
    return redirect('/admin/gestion_participantes')

# ________ configuracion  de control __________

@app.route('/admin/gestion_control')
def login_admin_control():
    if not 'login' in session  or session["tipo_usuario"]!="admin":
        return redirect("/admin/login")

    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM usuario WHERE tipo='control'")
    usuario_control = cursor.fetchall()
    db.database.commit()
    return render_template('admin/gestion_control.html',u_control=usuario_control)
    
@app.route('/admin/gestion_control/borrar',methods=['POST'])
def login_admin_control_borrar():
    _id=request.form['txtID']
   # cursor=db.database.cursor()
   # cursor.execute("SELECT portada_even FROM evento_academico WHERE id_evento=%s",(_id,))
   # evento = cursor.fetchall()
   # db.database.commit()
   #print(evento)
    #if os.path.exists("templates/img/"+str(evento[0][0])):
     #  os.unlink("templates/img/"+str(evento[0][0]))
    
    cursor=db.database.cursor()
    #cursor.execute("DELETE FROM `evento_academico` WHERE id_evento=%s",(_id,))
   # cursor.execute("INSERT INTO evento_eliminado ( id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador) SELECT id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador FROM evento_academico WHERE id_evento = %s", (_id,))
    cursor.execute("DELETE FROM `usuario` WHERE id_usuario=%s",(_id,))
    db.database.commit() 
    
    return redirect('/admin/gestion_control')


@app.route('/admin/gestion_control/guardar',methods=['POST'])
def login_admin_control_guardar():
    _usuario=request.form['txtusuario']
    _pass=request.form['txtpass']
    _correo=request.form['txtcorreo']

  #  tiempo=datetime.now()
  #  horaActual=tiempo.strftime('%Y%H%M%S')
    
   # if _imagen.filename!="":
    #    nuevoNombre=horaActual+" "+_imagen.filename
     #   _imagen.save("templates/img/"+nuevoNombre)
        
    sql="INSERT INTO `usuario`(`id_usuario`, `tipo`, `ci`, `contrasena`, `correo_elec`, `nombre`, `apellido_p`, `apellido_m`, `fecha_naci`, `usuario`, `celular`, `id_administrador`, `portada`, `perfil`) VALUES (NULL,'control',NULL,%s,%s,NULL,NULL,NULL,NULL,%s,NULL,NULL,NULL,NULL);"
    datos=(_pass,_correo,_usuario)
    cursor=db.database.cursor()
    cursor.execute(sql,datos)
    db.database.commit()
    
    return redirect('/admin/gestion_control')

# ________ configuracion  de expositor __________

@app.route('/admin/gestion_expositor')
def login_admin_expositor():
    if not 'login' in session  or session["tipo_usuario"]!="admin":
        return redirect("/admin/login")
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM usuario WHERE tipo='expositor'")
    usuario_expositor = cursor.fetchall()
    db.database.commit()
    return render_template('admin/gestion_expositor.html',u_expositor=usuario_expositor)
    
@app.route('/admin/gestion_expositor/guardar',methods=['POST'])
def login_admin_expositor_guardar():
    _usuario=request.form['txtusuario']
    _pass=request.form['txtpass']
    _correo=request.form['txtcorreo']

    sql="INSERT INTO `usuario`(`id_usuario`, `tipo`, `ci`, `contrasena`, `correo_elec`, `nombre`, `apellido_p`, `apellido_m`, `fecha_naci`, `usuario`, `celular`, `id_administrador`, `portada`, `perfil`) VALUES (NULL,'expositor',NULL,%s,%s,NULL,NULL,NULL,NULL,%s,NULL,NULL,NULL,NULL);"
    datos=(_pass,_correo,_usuario)
    cursor=db.database.cursor()
    cursor.execute(sql,datos)
    db.database.commit()
    
    return redirect('/admin/gestion_expositor')

@app.route('/admin/gestion_expositor/borrar',methods=['POST'])
def login_admin_expositor_borrar():
    _id=request.form['txtID']
   # cursor=db.database.cursor()
   # cursor.execute("SELECT portada_even FROM evento_academico WHERE id_evento=%s",(_id,))
   # evento = cursor.fetchall()
   # db.database.commit()
   #print(evento)
    #if os.path.exists("templates/img/"+str(evento[0][0])):
     #  os.unlink("templates/img/"+str(evento[0][0]))
    
    cursor=db.database.cursor()
    #cursor.execute("DELETE FROM `evento_academico` WHERE id_evento=%s",(_id,))
   # cursor.execute("INSERT INTO evento_eliminado ( id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador) SELECT id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador FROM evento_academico WHERE id_evento = %s", (_id,))
    cursor.execute("DELETE FROM `usuario` WHERE id_usuario=%s",(_id,))
    db.database.commit() 
    
    return redirect('/admin/gestion_expositor')

# cerramos administrador: 
@app.route('/admin/cerrar')
def admin_login_cerrar():
    session.clear()
    return redirect('/admin/login')

# =================== CONTROL ===================



@app.route('/control/')
def control():
    if not 'login' in session  or session["tipo_usuario"]!="control":
        return redirect("/control/login")
    return render_template('control/index.html')

#perfil:

@app.route('/control/perfil')
def control_perfil():
    if not 'login' in session  or session["tipo_usuario"]!="control":
        return redirect("/control/login")
    id_usuario = session.get('id_usuario') 
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s",(id_usuario,))
    usuario = cursor.fetchone()
    db.database.commit()

    resultado = {'perfil': usuario}
    
    mensaje = request.args.get('mensaje')
    mensaje2 = request.args.get('mensaje2')

    return render_template('control/perfil.html',resultado=resultado,mensaje=mensaje, mensaje2=mensaje2)

@app.route('/control/perfil/editar/<string:id>',methods=['POST'])
def login_control_perfil_editar(id):
 
    _usuario=request.form['txtusuario']
    _apPat=request.form['txtappat']
    _apMat=request.form['txtapmat']
    _nombre=request.form['txtnom']
    _correo=request.form['txtemail']
    _celu=request.form['txtcel']
    _ci=request.form['txtci']

    
    if  _usuario and _apPat and _apMat and _nombre and _correo and _celu and _ci :
        cursor = db.database.cursor()
        sql="UPDATE `usuario` SET `ci`=%s,`correo_elec`=%s,`nombre`=%s,`apellido_p`=%s,`apellido_m`=%s,`usuario`=%s,`celular`=%s  WHERE id_usuario=%s"
        datos=(_ci, _correo,_nombre,_apPat,_apMat,_usuario,_celu,id)
        cursor.execute(sql,datos)
        db.database.commit()
        
    return redirect('/control/perfil')

@app.route('/control/perfil/editarPass/<string:id>',methods=['POST'])
def login_control_perfil_editarPass(id):
 
    _pass=request.form['txtpass']
    _passsnueva=request.form['txtpassnueva']

    cursor = db.database.cursor()
    cursor.execute("SELECT contrasena FROM usuario WHERE id_usuario= %s", (id,))
    usuario = cursor.fetchone()
    db.database.commit()
    contra= str(usuario[0])
    mensaje = ""
    mensaje2 = ""
    if  _pass and _passsnueva :
        if _pass == contra:
            cursor = db.database.cursor()
            sql="UPDATE `usuario` SET `contrasena`=%s  WHERE id_usuario=%s"
            datos=(_passsnueva,id)
            cursor.execute(sql,datos)
            db.database.commit()
            mensaje2 = "Contraseña Guardada Exitosamente"
        else:
            mensaje = "Contraseña incorrecta"
    else:
        mensaje = "Contraseña incorrecta"
        
    
    return redirect(url_for('control_perfil', mensaje=mensaje, mensaje2=mensaje2))

@app.route('/control/login')
def login_control():

    return render_template('control/login.html')

@app.route('/control/login', methods=['POST'])
def login_control_post():
    _usuario=request.form['txtusuarioControl']
    _password=request.form['txtpasswordControl']
    cursor=db.database.cursor()
    
    cursor.execute("SELECT usuario, contrasena,tipo,id_usuario FROM usuario WHERE usuario= %s", (_usuario,))
    usuario = cursor.fetchone()
    db.database.commit()

    if usuario is not None:
        usuario_c = str(usuario[0])
        pass_c = str(usuario[1])
        tipo_usuario = str(usuario[2])
        id_usuario= str(usuario[3])

        if _password == pass_c and tipo_usuario=='control':
            # Autenticación exitosa, establecer variables de sesión
            session['login'] = True
            session['usuario'] = usuario_c
            session['tipo_usuario'] = tipo_usuario
            session['id_usuario'] = id_usuario
            return redirect('/control')
        else:
            mensaje = "Contraseña incorrecta"
    else:
        mensaje = "Usuario no encontrado"
        
    return render_template('/control/login.html', mensaje=mensaje)

# gestion de eventos:

@app.route('/control/gestion_eventos')
def login_control_eventos():
    if not 'login' in session or session["tipo_usuario"]!="control":
        return redirect("/control/login")
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM evento_academico")
    evento_acad = cursor.fetchall()
    db.database.commit()
    
    cursor=db.database.cursor()
    cursor.execute("SELECT a.id_ambiente, xr.id_evento, a.tipo_ambiente, a.capacidadmax, a.ubicacion FROM ambiente a, realiza_en xr WHERE a.id_ambiente like xr.id_ambiente")
    ambiente = cursor.fetchall()
    db.database.commit()
    
    cursor=db.database.cursor()
    cursor.execute("SELECT DISTINCT r.id_ambiente, r.id_evento, h.id_gestiona_hora, a.tipo_ambiente, a.ubicacion, h.fecha, h.hora_ini, h.hora_fin FROM `gestiona_hora` h, `ambiente` a, `realiza_en` r WHERE h.id_ambiente like a.id_ambiente and r.id_ambiente like a.id_ambiente and r.id_evento like h.id_evento ")
    horario = cursor.fetchall()
    db.database.commit()
   
    return render_template('control/gestion_eventos.html',eventos=evento_acad,ambientes=ambiente, horarios=horario)


@app.route('/control/gestion_eventos/guardar',methods=['POST'])
def login_control_evento_guardar():
    _idevento=request.form['txtidevento']
    _idambiente=request.form['txtidambiente']
    _fecha=request.form['txtfecha']
    _horai=request.form['txthora_i']
    _horaf=request.form['txthora_f']
    
    id_usuario = session.get('id_usuario') 

    sql="INSERT INTO `gestiona_hora`(`id_gestiona_hora`, `fecha`, `hora_ini`, `hora_fin`, `id_evento`, `id_control`,`id_ambiente`) VALUES (NULL,%s,%s,%s,%s,%s,%s);"
    datos=(_fecha,_horai,_horaf,_idevento,id_usuario,_idambiente)    
    
    sql2="INSERT INTO `realiza_en`(`id_evento`, `id_ambiente`) VALUES (%s,%s);"
    datos2=(_idevento,_idambiente)
    
    cursor=db.database.cursor()
    cursor.execute(sql,datos)
    cursor.execute(sql2,datos2)
    db.database.commit()
    
    return redirect('/control/gestion_eventos')

    
@app.route('/control/gestion_eventos/borrar',methods=['POST'])
def login_control_gestion_Eventos_borrar():
    _id=request.form['txtID']
    
    cursor=db.database.cursor()
    #cursor.execute("INSERT INTO evento_eliminado ( id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador) SELECT id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador FROM evento_academico WHERE id_evento = %s", (_id,))
    cursor.execute("DELETE FROM `gestiona_hora`  WHERE id_gestiona_hora=%s",(_id,))
    db.database.commit() 
    
    return redirect('/control/gestion_eventos')



# gestion de ambientes: 

@app.route('/control/ambientes')
def login_control_ambientes():
    if not 'login' in session or session["tipo_usuario"]!="control":
        return redirect("/control/login")
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM ambiente")
    ambiente = cursor.fetchall()
    db.database.commit()
    
    cursor=db.database.cursor()
    cursor.execute("SELECT a.id_ambiente, e.id_equipoelec, e.tipo, e.descripcion, e.catidad FROM `ambiente` a, `equipo_elec`e WHERE a.id_ambiente like e.id_ambiente")
    eq_elec = cursor.fetchall()
    db.database.commit()
    
    cursor=db.database.cursor()
    cursor.execute("SELECT a.id_ambiente, e.id_rudi, e.tipo, e.descripcion, e.catidad FROM `ambiente` a, `rudimentario`e WHERE a.id_ambiente like e.id_ambiente")
    rudimentario = cursor.fetchall()
    db.database.commit()
    
    return render_template('control/ambientes.html',eventos=ambiente,electrico=eq_elec, equipo_rud=rudimentario)


@app.route('/control/ambientes/guardar_amb',methods=['POST'])
def login_control_amb_guardaramb():
    _tipo=request.form['txttipo']
    _capmax=request.form['txtcapmax']
    _ubi=request.form['txtubic']

    
    sql1="INSERT INTO `ambiente`(`id_ambiente`, `tipo_ambiente`, `capacidadmax`, `ubicacion`) VALUES (NULL,%s,%s,%s);"
    datos1=(_tipo,_capmax,_ubi)    
    
    cursor=db.database.cursor()
    cursor.execute(sql1,datos1)
    db.database.commit()
    

    return redirect('/control/ambientes')

@app.route('/control/ambientes/guardar_eq_el',methods=['POST'])
def login_control_amb_guardarel():
    _id=request.form['txtid']
    _tipo=request.form['txttipoeq']
    _desc=request.form['txtdesc']
    _cant=request.form['txtcant']

    sql="INSERT INTO `equipo_elec`(`id_equipoelec`, `tipo`, `descripcion`, `id_ambiente`, `catidad`) VALUES (NULL,%s,%s,%s,%s);"
    datos=(_tipo,_desc,_id,_cant)    
    cursor=db.database.cursor()
    cursor.execute(sql,datos)
    db.database.commit()
    

    return redirect('/control/ambientes')

@app.route('/control/ambientes/guardar_rud',methods=['POST'])
def login_control_amb_guardarrud():
    _id=request.form['txtid']
    _tipo=request.form['txttipoeq']
    _desc=request.form['txtdesc']
    _cant=request.form['txtcant']

    sql="INSERT INTO `rudimentario`(`id_rudi`, `tipo`, `descripcion`, `id_ambiente`, `catidad`) VALUES (NULL,%s,%s,%s,%s);"
    datos=(_tipo,_desc,_id,_cant)    
    cursor=db.database.cursor()
    cursor.execute(sql,datos)
    db.database.commit()
    return redirect('/control/ambientes')
    
@app.route('/control/ambientes/borrar_eq',methods=['POST'])
def login_control_ambiente_borrar_eq():
    _id=request.form['txtID']
    
    cursor=db.database.cursor()
    #cursor.execute("INSERT INTO evento_eliminado ( id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador) SELECT id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador FROM evento_academico WHERE id_evento = %s", (_id,))
    cursor.execute("DELETE FROM `equipo_elec` WHERE id_equipoelec=%s",(_id,))
    db.database.commit() 
    
    return redirect('/control/ambientes')

@app.route('/control/ambientes/borrar_rud',methods=['POST'])
def login_control_ambiente_borrar_rud():
    _id=request.form['txtID']
    
    cursor=db.database.cursor()
    #cursor.execute("INSERT INTO evento_eliminado ( id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador) SELECT id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador FROM evento_academico WHERE id_evento = %s", (_id,))
    cursor.execute("DELETE FROM `rudimentario` WHERE id_rudi=%s",(_id,))
    db.database.commit() 
    
    return redirect('/control/ambientes')

@app.route('/control/ambientes/borrar',methods=['POST'])
def login_control_ambiente_borrar():
    _id=request.form['txtID']
    
    cursor=db.database.cursor()
    #cursor.execute("INSERT INTO evento_eliminado ( id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador) SELECT id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador FROM evento_academico WHERE id_evento = %s", (_id,))
    cursor.execute("DELETE FROM `ambiente` WHERE id_ambiente=%s",(_id,))
    cursor.execute("DELETE FROM `rudimentario` WHERE id_ambiente=%s",(_id,))
    cursor.execute("DELETE FROM `equipo_elec` WHERE id_ambiente=%s",(_id,))
    db.database.commit() 
    
    return redirect('/control/ambientes')

@app.route('/control/ambientes/editar/<string:id>',methods=['POST'])
def login_control_ambiente_editar(id):
 
    _tipo=request.form['txttipo']
    _capmax=request.form['txtcapmax']
    _ubicacion=request.form['txtubi']

    
    if  _tipo and _capmax :
        cursor = db.database.cursor()
        sql="UPDATE `ambiente` SET `tipo_ambiente`=%s,`capacidadmax`=%s,`ubicacion`=%s  WHERE id_ambiente=%s"
        datos=(_tipo, _capmax,_ubicacion,id)
        cursor.execute(sql,datos)
        db.database.commit()
        
    return redirect('/control/ambientes')


# GESTION RESERVAS:
@app.route('/control/gestion_reservas')
def login_control_gestion_reservas():
    if not 'login' in session or session["tipo_usuario"]!="control":
        return redirect("/control/login")
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM usuario")
    myresult = cursor.fetchall()
    # convertimos los datos a diccionario
    insertObject=[]
    columNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close()
    
    return render_template('control/gestion_reservas.html',data=insertObject)

# GESTION INSCRIPCIONES:
@app.route('/control/gestion_inscripciones')
def login_control_gestion_inscripciones():
    if not 'login' in session or session["tipo_usuario"]!="control":
        return redirect("/control/login")
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM usuario")
    myresult = cursor.fetchall()
    # convertimos los datos a diccionario
    insertObject=[]
    columNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close()
    
    return render_template('control/gestion_inscripciones.html',data=insertObject)





# cerrar el ussuario control:
@app.route('/control/cerrar')
def admin_control_cerrar():
    session.clear()
    return redirect('/control/login')


# =================== EXPOSITOR ===================

@app.route('/expositor/')
def expositor():
    if not 'login' in session  or session["tipo_usuario"]!="expositor":
        return redirect("/expositor/login")
    return render_template('expositor/index.html')        

# creacion de login para el usuario expositor

@app.route('/expositor/login')
def login_expositor():

    return render_template('expositor/login.html')

@app.route('/expositor/login', methods=['POST'])
def login_expositor_post():
    _usuario=request.form['txtusuarioControl']
    _password=request.form['txtpasswordControl']
    cursor=db.database.cursor()
    
    cursor.execute("SELECT usuario, contrasena,tipo,id_usuario FROM usuario WHERE usuario= %s", (_usuario,))
    usuario = cursor.fetchone()
    db.database.commit()

    if usuario is not None:
        usuario_c = str(usuario[0])
        pass_c = str(usuario[1])
        tipo_usuario = str(usuario[2])
        id_usuario= str(usuario[3])

        if _password == pass_c and tipo_usuario=='expositor':
            # Autenticación exitosa, establecer variables de sesión
            session['login'] = True
            session['usuario'] = usuario_c
            session['tipo_usuario'] = tipo_usuario
            session['id_usuario'] = id_usuario
            return redirect('/expositor/perfil')
        else:
            mensaje = "Contraseña incorrecta"
    else:
        mensaje = "Usuario no encontrado"
        
    return render_template('/expositor/login.html', mensaje=mensaje)

#perfil:

@app.route('/expositor/perfil')
def expositor_perfil():
    if not 'login' in session  or session["tipo_usuario"]!="expositor":
        return redirect("/expositor/login")
    id_usuario = session.get('id_usuario') 
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s",(id_usuario,))
    usuario = cursor.fetchone()
    db.database.commit()

    resultado = {'perfil': usuario}
    
    mensaje = request.args.get('mensaje')
    mensaje2 = request.args.get('mensaje2')

    return render_template('expositor/perfil.html',resultado=resultado,mensaje=mensaje, mensaje2=mensaje2)

@app.route('/expositor/perfil/editar/<string:id>',methods=['POST'])
def login_expositor_perfil_editar(id):
 
    _usuario=request.form['txtusuario']
    _apPat=request.form['txtappat']
    _apMat=request.form['txtapmat']
    _nombre=request.form['txtnom']
    _correo=request.form['txtemail']
    _celu=request.form['txtcel']
    _ci=request.form['txtci']

    
    if  _usuario and _apPat and _apMat and _nombre and _correo and _celu and _ci :
        cursor = db.database.cursor()
        sql="UPDATE `usuario` SET `ci`=%s,`correo_elec`=%s,`nombre`=%s,`apellido_p`=%s,`apellido_m`=%s,`usuario`=%s,`celular`=%s  WHERE id_usuario=%s"
        datos=(_ci, _correo,_nombre,_apPat,_apMat,_usuario,_celu,id)
        cursor.execute(sql,datos)
        db.database.commit()
        
    return redirect('/expositor/perfil')

@app.route('/expositor/perfil/editarPass/<string:id>',methods=['POST'])
def login_expositor_perfil_editarPass(id):
 
    _pass=request.form['txtpass']
    _passsnueva=request.form['txtpassnueva']

    cursor = db.database.cursor()
    cursor.execute("SELECT contrasena FROM usuario WHERE id_usuario= %s", (id,))
    usuario = cursor.fetchone()
    db.database.commit()
    contra= str(usuario[0])
    mensaje = ""
    mensaje2 = ""
    if  _pass and _passsnueva :
        if _pass == contra:
            cursor = db.database.cursor()
            sql="UPDATE `usuario` SET `contrasena`=%s  WHERE id_usuario=%s"
            datos=(_passsnueva,id)
            cursor.execute(sql,datos)
            db.database.commit()
            mensaje2 = "Contraseña Guardada Exitosamente"
        else:
            mensaje = "Contraseña incorrecta"
    else:
        mensaje = "Contraseña incorrecta"
        
    
    return redirect(url_for('expositor_perfil', mensaje=mensaje, mensaje2=mensaje2))


# cerrar el ussuario expositor:
@app.route('/expositor/cerrar')
def expositor_cerrar():
    if not 'login' in session  or session["tipo_usuario"]!="expositor":
        return redirect("/expositor/login")
    
    session.clear()
        
    return redirect('/expositor/login')

# ________________________________________________________
if __name__ == '__main__':
    app.run(debug=True,port=4000)

