library(tidyverse)
library(leaflet)
molini <- read.csv("MOLINI lng and lat.csv", 
                  stringsAsFactors = FALSE,
                  encoding = "UTF-8")
leaflet(data = molini)%>%
  addTiles() %>%  
  addMarkers(lng = ~-lng, lat = ~lat, popup = ~text)