pt = "IHOPEYOUAREHAVINGLOTSOFFANINTRYINGTOCATCHMETHATWASNTMEONTHETVSHOWWHICHBRINGOUPAPOINTABOUTMEIAMNOTAFRAIDOFTHEGASCHAMBERBECAASEITWILLSENDMETOPAYALLCEALLTHE"
ct = ["HER>pl^VPk|1LTG2d",
      "Np+B(#O%DWY.<*Kf)",
      "By:cM+UZGW()L#zHJ",
      "Spp7^l8*V3pO++RK2",
      "_9M+ztjd|5FP+&4k/",
      "p8R^FlO-*dCkF>2D(",
      "#5+Kq%;2UcXGV.zL|",
      "(G2Jfj#O+_NYz+@L9",
      "d<M+b+ZR2FBcyA64K"]

def make_key(ct, pt):
    key = {}
    for i in range(len(pt)):
        char = ct[i%9][(2*i)%17]

        if pt[i] in key.keys():
            if char not in key[pt[i]]:
                key[pt[i]].append(char)
        else:
            key[pt[i]] = [char]
    return key

print(make_key(ct, pt))
