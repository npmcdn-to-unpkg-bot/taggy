# Taggy
Tag based resources server


## Data security
While https can protect your data from unwanted eyes during transfer between the server and your computer, anyone with access to the database can read your deepest secrets.

As **Taggy** can be used both hosted or installed on a company server, you want to avoid that these secrets can be read by the database administrator.
As a single shared encryption key would be useless, data is encrypted using a user specific encryption key.
 
But because **Taggy** is a system where resources are meant to be shared between multiple persons, secrets entered by one user, need to be accessible by others (while you don't know their password). To get around this, asymmetric encryption is used and shared, encrypted resources are encrypted using the public key of everyone that needs access.

When accessing an encrypted resource, it is decrypted using your own private key. This private key is saved in the database in encrypted form using a symmetric encryption algorithm. 
Upon loading of the **Taggy** application, your encrypted private key is downloaded to your local machine. When it's required, you will be prompted for your encryption password 
(different from your account password) and the private key is decrypted locally, and then used to decrypt the secret you wanted to access.

The private key will stay unencrypted in your local machine's memory for a configurable amount of time, or until you manually lock it again.

- The private key is never unencrypted on the server.
- Your secrets are never sent to the server in clear text, nor are they ever unencrypted on the server.
- The password you use to encrypt your private key is never sent to the server.
- It is not possible to reset this password if you forget it (we can't recover your private key without it).
- Secrets shared with other users can be made available again after generating a new private-public key pair, but requires the intervention of another user.
- Encrypted data is not indexed for the search function, as such, it's not possible to use search for the content of encrypted data.

## Requirements
**Taggy** is a Python 2.7 web-application, while it might work with Python 2.6 this is untested and unsupported. The same is valid for python 3.x.

Any required Python libraries will be installed with the installation of **Taggy**.

For storage of data **Taggy** depends on a MySql server, either on the same host or on a different system. 
While other database systems could be used, they are not supported. 
And libraries to communicate with the database will need to be installed manually, as they will not be installed by following the installation guide.

## Installation
Start with checking out the code from the git repository.

We recommend running in a virtual environment. If you have never used it look at the [installation and user guide](https://virtualenv.pypa.io/en/stable/).

To install a library, activate the virtual environment (if used) and then run the given commands.

Install the OS dependant libraries:

#### Windows
Move to the setup/windows directory

- `pip install MySQL_python-1.2.5-cp27-none-win32.whl`

#### All platforms
After the installation of the OS dependant libraries, if any, continue with installing the rest of the required python libraries.

`pip install -r requirements.txt`
