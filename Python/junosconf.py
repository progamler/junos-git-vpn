import csv
import sys
print(sys.argv[1])
with open(sys.argv[1], 'r') as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    for row in reader:
        i = i+1
        if i == 1:
            pass
        else:
            print("####################### " + row[0] + " ###############################")
## Interface IP and route for tunnel traffic
            print("set interfaces " + row[3] + " family inet")
            print("set routing-options static route " + row[6] + "/32 next-hop " + row[3] + "")
            print("set security zones security-zone vpn interfaces "+ row[3] )
            print("set interfaces " + row[16] + " family inet address " + row[5])
            print("set security zones security-zone gre interfaces "+ row[16] )
## IKE policy
            print("set security ike policy " + row[0] + " mode main")
            print("set security ike policy " + row[0] + " pre-shared-key ascii-text  \"" + row[7] + "\"")
## IKE gateway with peer IP address, IKE policy and outgoing interface
            print("set security ike gateway " + row[0] + " ike-policy " + row[0])
            print("set security ike gateway " + row[0] + " address " + row[4])
            print("set security ike gateway " + row[0] + " external-interface " + row[1])
## IKE authentication, encryption, DH group, and Lifetime
            print("set security ike policy " + row[0] + " proposals g" + row[9] + "-" + row[8] + "-" + row[10])
## IPsec policy
            print("set security ipsec policy ipsec-policy-cfgr proposal-set userDefined")
## IPsec vpn
            print("set security ipsec vpn " + row[0] + " ike gateway " + row[0] + "")
            print("set security ipsec vpn " + row[0] + " ike ipsec-policy " + row[0] + "")
            print("set security ipsec vpn " + row[0] + " bind-interface " + row[3] + "")
            print("set security ipsec vpn " + row[0] + " establish-tunnels immediately")
## IPsec authentication and encryption
            print("set security ipsec proposal ipsec-proposal-cfgr protocol esp")
            print("set security ipsec policy ipsec-policy-cfgr proposals " + row[11] + "-" + row[13])
            print("set security ipsec policy ipsec-policy-cfgr perfect-forward-secrecy keys group" + row[12])
## GRE Tunnel Settings
            print("set interfaces " + row[17] + " tunnel source " + row[5])
            print("set interfaces " + row[17] + " tunnel destination " + row[6])
            print("set interfaces " + row[17] + " family inet address " + row[14])
            print("set security zones security-zone " + row[2] + " interfaces "+ row[17] )
