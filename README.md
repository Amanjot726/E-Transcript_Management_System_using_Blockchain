# E-Transcript Management System Using Blockchain


- Creating a blockchain 4-04-22
- If facing this error during installation of Command Prompt IPFS:)
[https://peter-whyte.com/ps1-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system-powershell/](https://peter-whyte.com/ps1-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system-powershell/)
- 
## Uploading file on IPFS and then accessing it.
- Initialize ipfs using command
```
ipfs daemon
```
![image](https://user-images.githubusercontent.com/53931644/167350698-3d371dc6-7843-41dd-b9e0-fbe57a1912b5.png)

- Open another powershell window with daemon initialized on first powershell window.
- Run following commands:
```
python
import ipfshttpclient
client = ipfshttpclient.connect("/dns/localhost/tcp/5001/http")
res = client.add("D:\epilight_cpp_new.pdf")
print(res)
```
![image](https://user-images.githubusercontent.com/53931644/167351221-1eb40173-6ff6-4d95-8d08-a6f25e16abba.png)
- To access the file do
```
http://localhost:8080/ipfs/QmP7Aq8v9way3Yg5outFhYoNLbH3rztzHsVLFLqM1M2eea
```

## References:
[https://github.com/ipfs-shipyard/py-ipfs-http-client#usage](https://github.com/ipfs-shipyard/py-ipfs-http-client#usage)  
[https://medium.com/python-pandemonium/getting-started-with-python-and-ipfs-94d14fdffd10](https://medium.com/python-pandemonium/getting-started-with-python-and-ipfs-94d14fdffd10)
