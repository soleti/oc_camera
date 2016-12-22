#!/usr/bin/env python3.4

from ROOT import TGraph, TH1F, TCanvas, TColor
from ROOT import kRed, kGreen, kBlue, kAzure, kYellow, kGray
from numpy import array
f = open("plot.csv","r")

pd_x = []
pd_y = []
m5s_x = []
m5s_y = []
ncd_x = []
ncd_y = []
fi_x = []
fi_y = []
lega_x = []
lega_y = []
sel_x = []
sel_y = []
dscd_x = []
dscd_y = []
fdi_x = []
fdi_y = []
sc_x = []
sc_y = []
misto_x = []
misto_y = []

for line in f.readlines()[1:]:
    party = line.split(",")[2].replace('"','')
    if "NA" in line.split(",")[13]: continue

    x_cord = float(line.split(",")[13].replace('"',''))
    y_cord = float(line.split(",")[14].replace('"',''))

    if party == "PD":
        pd_x.append(x_cord)
        pd_y.append(y_cord)

    if party == "M5S":
        m5s_x.append(x_cord)
        m5s_y.append(y_cord)

    if party == "AP-NCD-CPI":
        ncd_x.append(x_cord)
        ncd_y.append(y_cord)

    if party == "FI-PdL":
        fi_x.append(x_cord)
        fi_y.append(y_cord)

    if party == "Lega":
        lega_x.append(x_cord)
        lega_y.append(y_cord)

    if party == "SI-SEL":
        sel_x.append(x_cord)
        sel_y.append(y_cord)

    if party == "DS-CD":
        dscd_x.append(x_cord)
        dscd_y.append(y_cord)

    if party == "CLP-MAIE":
        sc_x.append(x_cord)
        sc_y.append(y_cord)

    if party == "Misto":
        misto_x.append(x_cord)
        misto_y.append(y_cord)

    if party == "FdI":
        fdi_x.append(x_cord)
        fdi_y.append(y_cord)

g_pd = TGraph(len(pd_x),array(pd_y),array(pd_x))
g_pd.SetMarkerStyle(24)
g_pd.SetMarkerColor(TColor.GetColor("#F0001C"))

g_m5s = TGraph(len(m5s_x),array(m5s_y),array(m5s_x))
g_m5s.SetMarkerStyle(24)
g_m5s.SetMarkerColor(kYellow)

g_ncd = TGraph(len(ncd_x),array(ncd_y),array(ncd_x))
g_ncd.SetMarkerStyle(24)
g_ncd.SetMarkerColor(TColor.GetColor("#05517e"))

g_fi = TGraph(len(fi_x),array(fi_y),array(fi_x))
g_fi.SetMarkerStyle(24)
g_fi.SetMarkerColor(TColor.GetColor("#007fff"))

g_lega = TGraph(len(lega_x),array(lega_y),array(lega_x))
g_lega.SetMarkerStyle(24)
g_lega.SetMarkerColor(kGreen)

g_sel = TGraph(len(sel_x),array(sel_y),array(sel_x))
g_sel.SetMarkerStyle(24)
g_sel.SetMarkerColor(TColor.GetColor("#B00000"))

g_dscd = TGraph(len(dscd_x),array(dscd_y),array(dscd_x))
g_dscd.SetMarkerStyle(24)
g_dscd.SetMarkerColor(TColor.GetColor("#DDADAF"))

g_sc = TGraph(len(sc_x),array(sc_y),array(sc_x))
g_sc.SetMarkerStyle(24)
g_sc.SetMarkerColor(TColor.GetColor("#3366FF"))

g_fdi = TGraph(len(fdi_x),array(fdi_y),array(fdi_x))
g_fdi.SetMarkerStyle(24)
g_fdi.SetMarkerColor(TColor.GetColor("#00005A"))

g_misto = TGraph(len(misto_x),array(misto_y),array(misto_x))
g_misto.SetMarkerStyle(24)
g_misto.SetMarkerColor(kGray)

c_g = TCanvas("c_g","",600,600)
g_pd.Draw("AP")
g_pd.GetXaxis().SetLimits(-1,1)
g_pd.GetYaxis().SetRangeUser(-1,1)
g_m5s.Draw("P")
g_ncd.Draw("P")
g_fi.Draw("P")
g_lega.Draw("P")
g_sel.Draw("P")
g_dscd.Draw("P")
g_sc.Draw("P")
g_misto.Draw("P")
g_fdi.Draw("P")
g_pd.Draw("P")

c_g.Update()

input()
