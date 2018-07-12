# -*- coding: utf-8 -*-
import psycopg2, psycopg2.extras
import pymysql
import cx_Oracle

class Conectar:

    def __init__(self):

        self.db_host = ''
        self.db_user = '' 
        self.db_pass = '' 
        self.db_port = '' 

    # Para conectar a PostgreSQL
    def conectarPostgres(self,usuario,pss,host,port):
        bds=[]
        try:    
            self.db_host = host
            self.db_user = usuario 
            self.db_pass = pss 
            self.db_port = port 
      
            conn = psycopg2.connect(user=self.db_user,password=self.db_pass,host=self.db_host,port=self.db_port)
      
            cursor = conn.cursor() 

            sql="SELECT datname FROM pg_database PD,pg_user PU WHERE usename= '%s' AND PD.datdba=PU.usesysid" %(usuario)
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            for row in rows:
                bds.append(row[0])
        except:
            bds=['error postgres'+ ' ' +self.db_user + ' '+ self.db_pass + ' '+ self.db_host + ' '+ self.db_port]
            #bds=['error postgres']

        return bds
        cursor.close ()
        conn.close()

    # Para conectar a MySQL
    def conectarMysql(self,usuario,pss,host,port):
        bds=[]
        try:      
            self.db_host = host
            self.db_user = usuario 
            self.db_pass = pss 
            self.db_port = port 
      
            #conn = MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=int(self.db_port))
            conn = pymysql.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=int(self.db_port))
            #conn = mysql.connector.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=self.db_port)
            cursor = conn.cursor() 
            sql="show databases" 
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            for row in rows:
                bds.append(row[0])
                
        except Exception as inst:
            #bds=['error mysql'+ ' '+ self.db_host + ' '+  self.db_user + ' '+ self.db_pass + ' '+  self.db_port]
            bds=['error mysql' + str(inst)]

        return bds
        cursor.close ()
        conn.close()
  
    #Para conectar a Oracle
    def conectarOracle(self,usuario,pss,host):
        bds=[]
        try:
            self.db_user = usuario 
            self.db_pass = pss 
            self.db_host = host
      
            s=str(self.db_user+"/"+self.db_pass+"@"+self.db_host)
            conn=cx_Oracle.connect(s)
  
            cursor = conn.cursor() 
            sql="select * from all_users" 
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            for row in rows:
                bds.append(row[0])
        except Exception as inst:
            bds=['error oracle' + str(inst) ]
        return bds
        cursor.close ()
        conn.close()  
        
    #Ejecutar servicios
    def ejecutarServicios(self, usuario,pss,host,port,db,sql,motor):
        estudiantes=[]
        try:      
            self.db_host = host
            self.db_user = usuario 
            self.db_pass = pss 
            self.db_port = port 
            self.db_db = db
            self.db_sql = sql
    
    
            if(motor=="postgres"):
                conn = psycopg2.connect(database=self.db_db,user=self.db_user,password=self.db_pass,host=self.db_host,port=self.db_port)
            elif(motor=="mysql"):
                conn = pymysql.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=int(self.db_port),db=self.db_db)
            elif(motor=="oracle"):                     
                s=str(self.db_user+"/"+self.db_pass+"@"+self.db_host)
                conn=cx_Oracle.connect(s)
                
            cursor = conn.cursor() 
            sql=self.db_sql

            cursor.execute(sql)
            rows = cursor.fetchall()
            
            for row in rows:                        
                estudiantes.append(row)
            
        except Exception as inst:
            
            estudiantes=['error postgres----->'+ ' ' +self.db_user + ' '+ self.db_pass + ' '+ self.db_host + ' '+ self.db_port]
        return estudiantes
        cursor.close ()
        conn.close() 