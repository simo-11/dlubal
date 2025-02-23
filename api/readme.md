# Installation
 adapted from https://apidocs.dlubal.com/installation_python_env.html#installation-python-env

```
 github\dlubal\api [main ≡ +1 ~0 -0 !]> uv venv
Using CPython 3.12.9
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate
C:\Users\simon\github\dlubal\api [main ≡ +1 ~0 -0 !]> .venv\Scripts\activate
(api) C:\Users\simon\github\dlubal\api [main ≡ +1 ~0 -0 !]> uv pip install dlubal.api
Resolved 11 packages in 1.32s
      Built dlubal-api==2.9.6
Prepared 8 packages in 32.49s
Installed 11 packages in 1.28s
 + dlubal-api==2.9.6
 + grpcio==1.68.0
 + grpcio-tools==1.68.0
 + numpy==2.2.3
 + pandas==2.2.3
 + protobuf==5.29.3
 + python-dateutil==2.9.0.post0
 + pytz==2025.1
 + setuptools==75.8.0
 + six==1.17.0
 + tzdata==2025.1
>  uv pip install spyder-kernels==3.0.*
```

# Running using spyder

Allow spyder to access network if not already configured

https://apidocs.dlubal.com/quick_start.html
 * RFEM - Options - Program Options settings gRPC at port 9000 (as default on)
```
(api) C:\Users\simon\github\dlubal\api [main ≡ +1 ~0 -0 !]> C:\ProgramData\spyder-6\envs\spyder-runtime\Scripts\spyder.exe
```
 * preferences / Python C:/Users/simon/github/dlubal/api/.venv/Scripts/python.exe
 * first start is quite slow
 * config.ini location checked using debugger
```
!p self.config_loc
WindowsPath('C:/Users/simon/github/dlubal/api/.venv/Lib/site-packages/dlubal/api/config.ini')
```
 * No subscription
```
RuntimeError: gRPC Error: UNAUTHENTICATED - Connected client does not have API service subscription.
```
 
