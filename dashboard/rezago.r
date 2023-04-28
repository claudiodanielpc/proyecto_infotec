
##Borrar datos del entorno
rm(list=ls())


#Directorio
setwd("D:/")

##Crear folders de almacenamiento
dir.create("microdatos", showWarnings = F)

#Paquetería
if(!require('pacman')) install.packages('pacman')
pacman::p_load(tidyverse,srvyr)

#url enigh
url_enigh <- "https://www.inegi.org.mx/contenidos/programas/enigh/nc/2020/microdatos/enigh2020_ns_viviendas_csv.zip"

#Descargar y descomprimir
download.file(url_enigh, destfile = "microdatos/enigh2020_ns_viviendas_csv.zip")
unzip("microdatos/enigh2020_ns_viviendas_csv.zip", exdir = "microdatos")

#Cargar datos
enigh <- read.csv("microdatos/viviendas.csv")%>%
  janitor::clean_names()%>%
  #Convertir a numeric
  mutate(mat_pared=as.numeric(mat_pared),
         mat_pisos=as.numeric(mat_pisos),
         mat_techos=as.numeric(mat_techos),
         #Crear variable de rezago habitacional
         rezago=case_when((tot_resid/num_cuarto)>2.5 | 
                            mat_pared %in% c(1,2,3,4,5,6) | 
                            mat_pisos %in% c(1) |
                            mat_techos %in% c(1,2,3,4,6,7,9) |
                            excusado==2
                          ~ "En rezago", 
                          
                          TRUE ~ "Fuera de rezago"),
          #Crear variable de entidad. Si el folioviv tiene 10 caracteres, extraer los primeros dos caracteres si no, solo 1 caracter
          entidad=case_when(nchar(folioviv)==10 ~ substr(folioviv,1,2),
                            TRUE ~ substr(folioviv,1,1)))



print((enigh%>%
  #Diseño muestral
  as_survey(weights=factor, strata=est_dis, ids=upm)%>%
  #Estimación de rezago por entidad
  group_by(entidad,rezago)%>%
  summarise(viviendas=survey_prop(vartype="cv"))%>%
  filter(rezago=="En rezago")%>%
  ungroup()),n=32)
