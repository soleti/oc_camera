#Préparer les données pour 1867:

rm(list=ls())
library(oc);library(car);
data<-read.csv("camera.csv", header = TRUE)
votes <- data[,12:dim(data)[2]]
votes[votes==0] <-2 #important to change here
name <- paste(data$Last.Name,data$ID,sep="_")
partyCode <- recode(data$Party,"'PD'=1;'M5S'=2;'FI-PdL'=3;'Lega'=4;'Misto'=5;'AP-NCD-CPI'=6;'SI-SEL'=7; 'CLP-MAIE'=8")
partyCode <- as.numeric(as.character(partyCode))
#partyName <- recode(data$Party,"'Liberal Party of Canada'='Liberal';'Conservative (1867-1942)'='Conservative';'Liberal-Conservative'='Conservative';'Independent'='Independent';'Independent Conservative'='Independent';'Independent Liberal'='Independent'; 'Liberal (Reformer)'='Independent'")

legdata1 <- data.frame(data$CONSTITUENCY, data$Party,partyCode,'province',1,1)
names(legdata1) <- c("Constituency","party","partycode","province","provincecode","religion")
row.names(legdata1) <- name
rcv <- rollcall(votes,yea=1,nay=2,notInLegis=9,legis.name=name,legis.data=legdata1)

#1. Analyse Optimal Classification

#OCresults1 <- oc(rcv,minvotes=1993,d=1,polarity=c("FEDRIGA_332717"))
OCresults1d2 <- oc(rcv,minvotes=1993,polarity=c("ROSATO_177665","FEDRIGA_332717"))

#Par partis

symbol<-OCresults1d2$legislators$partycode
symbol[OCresults1d2$legislators$partycode =="3"]<-16
symbol[OCresults1d2$legislators$partycode =="2"]<-16
symbol[OCresults1d2$legislators$partycode =="4"]<-16
symbol[OCresults1d2$legislators$partycode =="1"]<-16
symbol[OCresults1d2$legislators$partycode =="5"]<-16
symbol[OCresults1d2$legislators$partycode =="6"]<-16
symbol[OCresults1d2$legislators$partycode =="7"]<-16
symbol[OCresults1d2$legislators$partycode =="8"]<-16
color<-OCresults1d2$legislators$partycode
color[OCresults1d2$legislators$partycode =="3"]<-"darkblue"
color[OCresults1d2$legislators$partycode =="2"]<-"yellow"
color[OCresults1d2$legislators$partycode =="4"]<-"green"
color[OCresults1d2$legislators$partycode =="1"]<-"red"
color[OCresults1d2$legislators$partycode =="5"]<-"black"
color[OCresults1d2$legislators$partycode =="6"]<-"blue"
color[OCresults1d2$legislators$partycode =="7"]<-"darkred"
color[OCresults1d2$legislators$partycode =="8"]<-"grey"

plot(0,0,type="n",main="XVII Legislatura",xlab="Sinistra - Destra",ylab="Supporto al governo")
print(OCresults1d2$legislators$coord1D)
print(OCresults1d2$legislators$coord2D)
print(OCresults1d2$legislators$partycode)

write.csv(OCresults1d2$legislators,file="plot.csv")
points(x=OCresults1d2$legislators$coord2D,y=OCresults1d2$legislators$coord1D,pch=symbol,col=color)
legend("bottomright", c("PD","Forza Italia","M5S","Lega","SEL","Scelta Civica","Misto"), pch=c(16,16,16,16,16,16,16),col=c("red","darkblue","yellow","green","darkred","grey","black"))
