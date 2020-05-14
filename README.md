# USMC-PFT

A calculator for the USMC's PFT and CFT events.

# Setup for development and testing

## Frontend

Running the frontend requires Node and NPM, which is automatically installed alongside Node.

Node can be installed from: https://nodejs.org/en/

Follow your operating sysystem sepcific instructions to install Node.

Once Node is installed, navigate to your local repository base and run the following commands to start the frontend:

```
cd usmc-pft/usmc-pft-ui/       //Navigate to the root of the frontend.
npm i                 //Install application dependencies.
npm start             //Launch the development server.
```

The frontend should automatically start in your browser. If it doesn't, open your browser and navigate to:

```
http://localhost:3000/
```

## Backend

Running the backend in development requires Python 3.6.x, and several dependencies which will be installed.

Python 3 can be installed from: https://www.python.org/downloads/

Follow your operating system specific instructions to install Python 3, to at least 3.6.x. The SDM backend currently uses Python 3.6.9.

Once Python is installed, navigate to your local repository base and run the following commands to start the backend:

### POSIX-based OS

```
cd usmc-pft/usmc-pft-backend/usmc_backend/
python3 -m venv env
source env/bin/activate
```

### Windows

```
cd usmc-pft\usmc-pft-backend\usmc_pft
python3 -m venv c:\path\to\usmc-pft\env\
c:\path\to\usmc-pft\env\Scripts\activate.bat
```

Once the Python virtual environment is activated the dependencies included in requirements.txt can be installed.

```
cd usmc-pft/usmc-pft-backend/
pip3 install -r ./requirements.txt
python3 run.py
```

The backend should now be running and application development/testing can begin.
