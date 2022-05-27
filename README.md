# E-Transcript Management System Using Blockchain


- Creating a blockchain 4-04-22

## IPFS installation docs
[https://docs.ipfs.io/install/command-line/#official-distributions])(https://docs.ipfs.io/install/command-line/#official-distributions)

### To run ipfs using python make sure that IPFS version and ipfshttpclient version is same.

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
- if    
-` res = client.add("C:\Users\priya\Downloads\adbms.pdf")
                                                         ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
`

then put r before the path and it converts normal string to raw string
`res = client.add(r"C:\Users\priya\Downloads\adbms.pdf")
`
![image](https://user-images.githubusercontent.com/53931644/167351221-1eb40173-6ff6-4d95-8d08-a6f25e16abba.png)
- To access the file do
```
http://localhost:8080/ipfs/QmP7Aq8v9way3Yg5outFhYoNLbH3rztzHsVLFLqM1M2eea
```


# DAG 
[https://dag.ipfs.io/](https://dag.ipfs.io/)

# Accessing Link
[https://ipfs.io/ipfs/QmPQx6wpxnNXm6jUMp7UvMskK6W4SXzzpNP9fZ6brxSukn?filename=Welcome%20to%20Marvel%20Madness%20event.pdf](https://ipfs.io/ipfs/QmPQx6wpxnNXm6jUMp7UvMskK6W4SXzzpNP9fZ6brxSukn?filename=Welcome%20to%20Marvel%20Madness%20event.pdf)

[https://ipfs.io/ipfs/QmPQx6wpxnNXm6jUMp7UvMskK6W4SXzzpNP9fZ6brxSukn](https://ipfs.io/ipfs/QmPQx6wpxnNXm6jUMp7UvMskK6W4SXzzpNP9fZ6brxSukn)

# Accssing content
```
ipfs cat QmPQx6wpxnNXm6jUMp7UvMskK6W4SXzzpNP9fZ6brxSukn
```

## References:
- [Both ipfs and ipfshttpclient should have same version](https://github.com/ipfs-shipyard/py-ipfs-http-client/issues/218)
- [https://github.com/ipfs-shipyard/py-ipfs-http-client#usage](https://github.com/ipfs-shipyard/py-ipfs-http-client#usage)  
- [https://medium.com/python-pandemonium/getting-started-with-python-and-ipfs-94d14fdffd10](https://medium.com/python-pandemonium/getting-started-with-python-and-ipfs-94d14fdffd10)
