from ROOT import *
import sys

#*******input files*********#
fullname = sys.argv[1]
filename = sys.argv[2]

# Open in binary mode
with open(fullname, "rb") as f:
    board_id = bytes.decode(f.read(2), "ascii")
    time_start = int.from_bytes(f.read(4), "big")
    
    temp_citi_start = float(int.from_bytes(f.read(2), "big"))
    temp_citi_start = ((2.7 - (temp_citi_start*2)/1e3)/8e-3)
    
    temp_hvps_start = float(int.from_bytes(f.read(2), "big"))
    temp_hvps_start = (temp_hvps_start*1.907e-5 - 1.035) / (-5.5e-3)
    
    hvps_volt_start = float(int.from_bytes(f.read(2), "big"))
    hvps_volt_start *= 1.812e-3
    
    hvps_curr_start = float(int.from_bytes(f.read(2), "big"))
    hvps_curr_start *= 5.194e-3
    
    f.read(114)
    
    daq_time = int.from_bytes(f.read(2), "big")
    daq_time /= 256
    act_daq_time = int.from_bytes(f.read(2), "big")
    act_daq_time /= 256
    
    trig_count_0 = int.from_bytes(f.read(4), "big")
    trig_count_16 = int.from_bytes(f.read(4), "big")
    trig_count_31 = int.from_bytes(f.read(4), "big")
    trig_count_or32 = int.from_bytes(f.read(4), "big")
    
    temp_citi_end = float(int.from_bytes(f.read(2), "big"))
    temp_citi_end = ((2.7 - (temp_citi_end*2)/1e3)/8e-3)
    
    temp_hvps_end = float(int.from_bytes(f.read(2), "big"))
    temp_hvps_end = (temp_hvps_end*1.907e-5 - 1.035) / (-5.5e-3)
    
    hvps_volt_end = float(int.from_bytes(f.read(2), "big"))
    hvps_volt_end *= 1.812e-3
    
    hvps_curr_end = float(int.from_bytes(f.read(2), "big"))
    hvps_curr_end *= 5.194e-3
    
    f.read(93)
    
    conf_id = f.read(1)
    bin_cfg = f.read(6)
    
    hist = [[] for i in range(6)]
    
    for i in range(0,6):
        dat = f.read(4096) #Default Byte for CitirocUI 4096 for each histogram
        for j in range(0, len(dat), 2): #Every 2 elements
            hist[i].append((dat[j]<<8)|(dat[j+1]))

    #Try to separate bins to be a single element        
    data_hist = [[] for i in range(6)] 
    
    for i1 in range(len(hist)):
        for j1 in range(len(hist[i1])):
            data_hist[i1] = data_hist[i1] + hist[i1][j1]*[j1+1]   
    
    #Plot
    print("**********---------------------------------------*********")
    print("**********             Plotting                  *********")
    print("**********---------------------------------------*********")

    #Histogram Plot
    h1 = TH1F('h1','Histogram of data Ch. 0, HG', 2048, 0, 2048)
    h2 = TH1F('h2','Histogram of data Ch. 0, LG', 2048, 0, 2048)
    h3 = TH1F('h3','Histogram of data Ch. 16, HG', 2048, 0, 2048) 
    h4 = TH1F('h4','Histogram of data Ch. 16, LG', 2048, 0, 2048)
    h5 = TH1F('h5','Histogram of data Ch. 31, HG', 2048, 0, 2048)
    h6 = TH1F('h6','Histogram of data Ch. 31, LG', 2048, 0, 2048)

    #Fill data into histogram
    for i2 in range(len(data_hist[0])):
        h1.Fill(data_hist[0][i2])
        h2.Fill(data_hist[1][i2])

    for i3 in range(len(data_hist[2])):
        h3.Fill(data_hist[2][i3])
        h4.Fill(data_hist[3][i3])

    for i4 in range(len(data_hist[4])):
        h5.Fill(data_hist[4][i4])
        h6.Fill(data_hist[5][i4])

c1 = TCanvas('c1')
h1.SetLineColor(4)
h1.SetFillColor(4)
h1.Draw()
# h1.GetYaxis().SetRangeUser(0,100)
# h1.GetXaxis().SetRangeUser(100,600)
h1.GetXaxis().SetTitle("ADC channel")
h1.GetXaxis().CenterTitle() #Make it center
h1.GetYaxis().SetTitle('Count')
h1.GetYaxis().CenterTitle() #Make it center
c1.Update()

c2 = TCanvas('c2')
h2.SetLineColor(4)
h2.SetFillColor(4)
h2.Draw()
# h2.GetYaxis().SetRangeUser(0,100)
# h2.GetXaxis().SetRangeUser(100,600)
h2.GetXaxis().SetTitle("ADC channel")
h2.GetXaxis().CenterTitle() #Make it center
h2.GetYaxis().SetTitle('Count')
h2.GetYaxis().CenterTitle() #Make it center
c2.Update()

c3 = TCanvas('c3')
h3.SetLineColor(4)
h3.SetFillColor(4)
h3.Draw()
# h3.GetYaxis().SetRangeUser(0,100)
# h3.GetXaxis().SetRangeUser(100,600)
h3.GetXaxis().SetTitle("ADC channel")
h3.GetXaxis().CenterTitle() #Make it center
h3.GetYaxis().SetTitle('Count')
h3.GetYaxis().CenterTitle() #Make it center
c3.Update()

c4 = TCanvas('c4')
h4.SetLineColor(4)
h4.SetFillColor(4)
h4.Draw()
# h4.GetYaxis().SetRangeUser(0,100)
# h4.GetXaxis().SetRangeUser(100,600)
h4.GetXaxis().SetTitle("ADC channel")
h4.GetXaxis().CenterTitle() #Make it center
h4.GetYaxis().SetTitle('Count')
h4.GetYaxis().CenterTitle() #Make it center
c4.Update()

c5 = TCanvas('c5')
h5.SetLineColor(4)
h5.SetFillColor(4)
h5.Draw()
# h5.GetYaxis().SetRangeUser(0,100)
# h5.GetXaxis().SetRangeUser(100,600)
h5.GetXaxis().SetTitle("ADC channel")
h5.GetXaxis().CenterTitle() #Make it center
h5.GetYaxis().SetTitle('Count')
h5.GetYaxis().CenterTitle() #Make it center
c5.Update()

c6 = TCanvas('c6')
h6.SetLineColor(4)
h6.SetFillColor(4)
h6.Draw()
# h6.GetYaxis().SetRangeUser(0,100)
# h6.GetXaxis().SetRangeUser(100,600)
h6.GetXaxis().SetTitle("ADC channel")
h6.GetXaxis().CenterTitle() #Make it center
h6.GetYaxis().SetTitle('Count')
h6.GetYaxis().CenterTitle() #Make it center
c6.Update()

#Total Graphs of HG
cAll_HG = TCanvas('AllHG','All Graphs for HG',600,800)
cAll_HG.Divide(1,3)
cAll_HG.cd(1)
h1.Draw()
cAll_HG.cd(2)
h3.Draw("colz")
cAll_HG.cd(3)
h5.Draw()
cAll_HG.Update()

#Total Graphs of HG
cAll_LG = TCanvas('AllLG','All Graphs for LG',600,800)
cAll_LG.Divide(1,3)
cAll_LG.cd(1)
h2.Draw()
cAll_LG.cd(2)
h4.Draw("colz")
cAll_LG.cd(3)
h6.Draw()
cAll_LG.Update()

output = "output_"+ filename + ".root"

oFile = TFile(output, 'recreate')
c1.Write()
c2.Write()
c3.Write()
c4.Write()
c5.Write()
c6.Write()
cAll_HG.Write()
cAll_LG.Write()
oFile.Close()

input()
