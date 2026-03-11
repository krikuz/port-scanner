{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Times-Roman;\f2\fmodern\fcharset0 Courier;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Network Scanner\
## Made by Krikuz\
\
A multithreaded Python port scanner that detects open ports, identifies services, and performs basic banner grabbing.\
\
## Features\
\
- Multithreaded scanning\
- Custom port range\
- Service detection\
- Banner grabbing\
- Results saved to file\
\
## Requirements\
\
- Python 3.x\
\
## Usage\
\
Run the script:\
\pard\pardeftab720\sa240\partightenfactor0

\f1 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 python3 script.py\
\pard\pardeftab720\partightenfactor0

\f2 \cf2 \
\
Example:\
\
\pard\pardeftab720\sa240\partightenfactor0

\f1 \cf2 Enter the target IP or domain below\uc0\u8232 scanme.nmap.org\
Enter starting port below\uc0\u8232 1\
Enter ending port below\uc0\u8232 1000\
\pard\pardeftab720\partightenfactor0

\f2 \cf2 \
\
Results will be saved in:\
\
\pard\pardeftab720\sa240\partightenfactor0

\f1 \cf2 scan_results.txt\
\pard\pardeftab720\partightenfactor0

\f2 \cf2 \
\
## Example Output\
\
\pard\pardeftab720\sa240\partightenfactor0

\f1 \cf2 Port 22:ssh is open\uc0\u8232 Banner: SSH-2.0-OpenSSH_6.6.1\
Port 80:http is open\uc0\u8232 Banner: HTTP/1.1 200 OK\
\pard\pardeftab720\partightenfactor0

\f2 \cf2 \
\
## Disclaimer\
\
This tool is for educational and authorized testing purposes only.\
\
}